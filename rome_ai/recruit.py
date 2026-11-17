"""Claude picks an army for a custom battle; you click it together in the game's menu.

    python -m rome_ai.recruit --faction macedon --enemy romans_julii --budget 15000 --battle field
    python -m rome_ai.recruit --faction carthage --enemy romans_scipii gauls --budget 12000 --battle siege-defense --personality hannibal
    python -m rome_ai.recruit --list        # factions and commanders

Knows the units the faction may pick in a custom battle and their prices (export_descr_unit.txt), the units the
enemy may have, the kind of battle, the commanders (personalities.md) and the battles of history (battles.md).
Writes armies/<faction>-vs-<enemy>-<battle>.html and .md: the list to click, the commander, how to use the army.
"""

from __future__ import annotations

import argparse
import re
import asyncio
import html
import sys
from collections import Counter
from pathlib import Path

from . import personalities as P
from . import units_db
from .general import ClaudeCodeGeneral, rule_lines

ROOT = Path(__file__).resolve().parents[1]
BATTLES = {  # --battle: (for the model, Polish, English)
    "field": ("a field battle on open ground", "zwykła bitwa w polu", "field battle"),
    "siege-attack": ("a siege: you ATTACK a walled town - you have to break in (artillery against walls and towers, "
                     "infantry for the breaches and the streets) and take the town square",
                     "oblężenie - atak", "siege - attack"),
    "siege-defense": ("a siege: you DEFEND a walled town - walls, gates, narrow streets and the town square; "
                      "missile units on the walls and solid infantry (spears, phalanx) to block the streets",
                      "oblężenie - obrona", "siege - defence"),
}
SYSTEM = (
    "You pick an army for a custom battle of Rome: Total War (Remastered) and the commander who will lead it. The "
    "army's general - an AI like you - will follow the GAME RULES and STRATEGY below and the chosen commander's "
    "style. Use every denarius of the budget well, never more. Pick units that fit the commander's style AND that "
    "answer what this enemy is likely to field. Exactly the unit types listed are available, at the listed prices.")


def roster_lines(roster: list[dict]) -> str:
    return "\n".join(f"- {u['type']} (menu: {u['name']}) - {u['cost']} denarii; {u['category']}"
                     f"{'; GENERAL BODYGUARD' if u['general'] else ''}; {u['stats']}" for u in roster)


def validate(roster: list[dict], picks: list[tuple[str, int]], budget: int, max_units: int) -> list[str]:
    """What is wrong with an army: unknown units, over the budget or the unit limit, no general."""
    by_type = {u["type"]: u for u in roster}
    errors = [f"{t} is not available to this faction" for t, _ in picks if t not in by_type]
    if errors:
        return errors
    cost = sum(by_type[t]["cost"] * n for t, n in picks)
    count = sum(n for _, n in picks)
    if cost > budget:
        errors.append(f"the army costs {cost}, over the budget of {budget}")
    if count > max_units:
        errors.append(f"{count} units, over the limit of {max_units}")
    if any(n < 1 for _, n in picks):
        errors.append("every count must be at least 1")
    if any(u["general"] for u in roster) and not any(by_type[t]["general"] for t, _ in picks):
        errors.append("the army has no general's bodyguard unit")
    return errors


def trim(roster: list[dict], picks: list[tuple[str, int]], budget: int, max_units: int) -> list[tuple[str, int]]:
    """Last resort after a wrong answer: drop units (the most expensive non-general first) until the army fits."""
    by_type = {u["type"]: u for u in roster}
    left: Counter = Counter()
    for t, n in picks:
        if t in by_type and n > 0:
            left[t] += n

    def cost() -> int:
        return sum(by_type[t]["cost"] * n for t, n in left.items())

    while left and (cost() > budget or sum(left.values()) > max_units):
        drop = max([t for t in left if not by_type[t]["general"]] or list(left), key=lambda t: by_type[t]["cost"])
        left[drop] -= 1
        left = +left
    return [(t, left[t]) for t in dict.fromkeys(t for t, _ in picks) if left.get(t)]


MIX_TOLERANCE = 15  # percentage points a role may stray from the commander's historical mix


def role(u: dict) -> str:
    """infantry / missile / cavalry / handler (elephants, dogs) - the general's bodyguard and siege are left out."""
    if u["general"] or u["category"] == "siege":
        return ""
    if u["category"] == "infantry" and " missile" in " " + str(u.get("class", "")):
        return "missile"
    return u["category"]


def parse_mix(text: str) -> dict[str, float]:
    return {k: float(v) for k, v in re.findall(r"(\w+)\s+(\d+(?:\.\d+)?)", text or "")}


def mix_errors(roster: list[dict], picks: list[tuple[str, int]], mix: dict[str, float], who: str) -> list[str]:
    """Share of units per role against the commander's historical mix (roles the faction cannot field are dropped)."""
    by_type = {u["type"]: role(u) for u in roster}
    have = {role(u) for u in roster} - {""}
    want = {k: v for k, v in mix.items() if k in have}
    total = sum(want.values())
    n = sum(c for t, c in picks if by_type.get(t))
    if not total or not n:
        return []
    errs = []
    for k, v in want.items():
        target, got = v * 100 / total, sum(c for t, c in picks if by_type.get(t) == k) * 100 / n
        if abs(got - target) > MIX_TOLERANCE:
            errs.append(f"{who} wants about {target:.0f}% {k} units (+-{MIX_TOLERANCE}), your army has {got:.0f}%")
    return errs


def cap_errors(roster: list[dict], picks: list[tuple[str, int]], caps: dict[str, int]) -> list[str]:
    """Hard limits on the number of units of a role (e.g. missile=5)."""
    by = {u["type"]: role(u) for u in roster}
    return [f"{k}: {n} units, over the limit of {caps[k]}" for k in caps
            if (n := sum(c for t, c in picks if by.get(t) == k)) > caps[k]]


def apply_caps(roster: list[dict], picks: list[tuple[str, int]], caps: dict[str, int]) -> list[tuple[str, int]]:
    """Cut units from the end of the list until every role is within its limit."""
    by, picks = {u["type"]: role(u) for u in roster}, [list(p) for p in picks]
    for k, cap in caps.items():
        over = sum(c for t, c in picks if by.get(t) == k) - cap
        for p in reversed(picks):
            cut = min(over, p[1]) if by.get(p[0]) == k and over > 0 else 0
            p[1] -= cut
            over -= cut
    return [(t, c) for t, c in picks if c > 0]


def selftest() -> None:
    """validate() and trim() on the real Macedonian roster - no model call."""
    roster = units_db.custom_roster("macedon")
    assert roster, "no game data"
    gen = next(u["type"] for u in roster if u["general"])
    pike = next(u for u in roster if u["name"] == "Phalanx Pikemen")["type"]
    ok = [(gen, 1), (pike, 4)]
    assert validate(roster, ok, 100000, 20) == [], validate(roster, ok, 100000, 20)
    assert any("not available" in e for e in validate(roster, ok + [("roman triarii", 1)], 100000, 20))
    assert any("over the budget" in e for e in validate(roster, ok, 1000, 20))
    assert any("over the limit" in e for e in validate(roster, [(gen, 1), (pike, 20)], 10 ** 6, 20))
    assert any("no general" in e for e in validate(roster, [(pike, 2)], 10 ** 6, 20))
    cut = trim(roster, [(gen, 1), (pike, 30)], 5000, 20)
    assert validate(roster, cut, 5000, 20) == [] and cut[0] == (gen, 1), cut
    assert not mix_errors(roster, [(gen, 1), (pike, 10)], parse_mix("infantry 100"), "x")
    assert mix_errors(roster, [(gen, 1), (pike, 10)], parse_mix("cavalry 100"), "x")
    assert cap_errors(roster, [(gen, 1), (pike, 10)], {"infantry": 5}) and not cap_errors(roster, [(pike, 5)], {"infantry": 5})
    assert apply_caps(roster, [(gen, 1), (pike, 10)], {"infantry": 4}) == [(gen, 1), (pike, 4)]
    print("recruit selftest OK:", cut)


async def recruit(faction: str, enemies: list[str], budget: int, battle: str, personality: str, max_units: int,
                  model: str, effort: str, lang: str, caps: dict[str, int] | None = None) -> dict:
    caps = caps or {}
    roster = units_db.custom_roster(faction)
    if not roster:
        raise SystemExit(f"no custom battle units found for {faction} (game data at {units_db.GAME_DATA})")
    types, cmds = P.army_types(), P.commanders()

    def army(f: str) -> P.Army:
        return P.Army(next((t for t, e in types.items() if f in e.list("factions")), None), [f])

    mine, foes = army(faction), [army(f) for f in enemies]
    hist = P.lessons(mine.type, [a.type for a in foes])
    choices = P.autopick_choices() if personality == "auto" else {personality: cmds[personality]}
    rules = rule_lines((ROOT / "rules.md").read_text(encoding="utf-8"))
    strategy = rule_lines((ROOT / "strategy.md").read_text(encoding="utf-8"))
    system = f"{SYSTEM}\n\nGAME RULES:\n{rules}\n\nSTRATEGY (the standard craft):\n{strategy}"
    language = "Polish (with proper Polish letters)" if lang == "pl" else "English"
    commanders_text = "\n\n".join(
        f"{k}: {c.name} - {c.fields.get('summary', '')}\nPreferred units: {c.fields.get('recruits', '')}\n"
        f"Historical mix (share of units, general excluded): {c.fields.get('mix') or 'no preference'}\nOrders:\n"
        + "\n".join(f"- {x}" for x in c.lines) for k, c in choices.items())
    user = (
        f"Battle: {BATTLES[battle][0]}.\nBudget: {budget} denarii. At most {max_units} units"
        + (", including one general's bodyguard unit" if any(u["general"] for u in roster) else "") + ".\n"
        f"Your army: {mine.describe(types)}" + (f" - {types[mine.type].fields.get('summary', '')}" if mine.type else "")
        + "\nEnemy: " + "; ".join(a.describe(types) for a in foes)
        + " - you do not know his army, only what he may field:\n"
        + "\n".join(f"Units {P.FACTIONS.get(f, (f,))[0]} may field:\n" + "\n".join(
            f"- {u['name']} ({u['cost']}): {u['stats']}" for u in units_db.custom_roster(f)) for f in enemies)
        + ("\n\nHistory of such battles:\n" + "\n".join(f"- {P._battle_text(b, types)}" for b in hist) if hist else "")
        + f"\n\n{'Choose the commander from these' if personality == 'auto' else 'The commander'}:\n{commanders_text}"
        + "\n\nThe commander's historical mix and preferred units are binding: build the army the way HE would have, "
          f"keeping each role's share within {MIX_TOLERANCE} points of his mix; put the cheap units where he put cheap "
          "troops (a weak centre, screens) and the expensive elite where he put his strength."
        + ("\n\nHARD LIMITS on unit counts: " + ", ".join(f"at most {n} {k} units" for k, n in caps.items()) + "."
           if caps else "")
        + f"\n\nUnits you may pick (type id first):\n{roster_lines(roster)}"
        + f"\n\nWrite 'reason', 'plan' and 'why' in {language}. 'plan': how the army deploys and fights, 3-5 "
          "sentences. 'why': why this army should beat this enemy, 2-3 sentences.")
    schema = {"type": "object", "additionalProperties": False,
              "required": ["personality", "reason", "units", "plan", "why"],
              "properties": {
                  "personality": {"type": "string", "enum": list(choices)},
                  "reason": {"type": "string"},
                  "units": {"type": "array", "items": {
                      "type": "object", "additionalProperties": False, "required": ["type", "count"],
                      "properties": {"type": {"type": "string", "enum": [u["type"] for u in roster]},
                                     "count": {"type": "integer", "minimum": 1, "maximum": max_units}}}},
                  "plan": {"type": "string"}, "why": {"type": "string"}}}
    general = ClaudeCodeGeneral(model=model, effort=effort)
    res = await general.ask(system, user, schema, effort=effort, timeout=400)
    picks = [(x["type"], int(x["count"])) for x in res.get("units", [])]
    def problems(pk):
        cmd = cmds.get(res.get("personality"))
        return validate(roster, pk, budget, max_units) + cap_errors(roster, pk, caps) + (
            mix_errors(roster, pk, parse_mix(cmd.fields.get("mix")), cmd.name) if cmd else [])

    errors = problems(picks)
    if errors:  # one correction, then the army is cut to fit
        print("first answer broke the rules:", "; ".join(errors), "- asking for a correction")
        res = await general.ask(system, user + "\n\nYour previous answer was wrong: " + "; ".join(errors)
                                + f". Previous units: {picks}. Answer again within the rules.", schema,
                                effort=effort, timeout=400)
        picks = [(x["type"], int(x["count"])) for x in res.get("units", [])]
        if validate(roster, picks, budget, max_units):
            picks = trim(roster, picks, budget, max_units)
    res["units"] = apply_caps(roster, picks, caps) if caps else picks
    res["roster"] = roster
    return res


def render(res: dict, faction: str, enemies: list[str], budget: int, battle: str, max_units: int, lang: str) -> tuple[str, str]:
    """(markdown, html) of the army sheet."""
    pl = lang == "pl"
    by_type = {u["type"]: u for u in res["roster"]}
    cmd = P.commanders().get(res["personality"])
    fname = P.FACTIONS.get(faction, (faction, faction))[1 if pl else 0]
    enames = ", ".join(P.FACTIONS.get(f, (f, f))[1 if pl else 0] for f in enemies)
    rows = [(by_type[t]["name"], t, n, by_type[t]["cost"], by_type[t]["cost"] * n) for t, n in res["units"]]
    total, count = sum(r[4] for r in rows), sum(r[2] for r in rows)
    W = dict(title=f"Armia: {fname} · wróg: {enames}" if pl else f"Army: {fname} against {enames}",
             battle=BATTLES[battle][1 if pl else 2], commander="Dowódca" if pl else "Commander",
             why_c="Dlaczego on" if pl else "Why him", units="Jednostki do wyklikania" if pl else "Units to pick",
             cols=("Jednostka (menu)", "typ w plikach gry", "Ile", "Cena", "Suma") if pl else
             ("Unit (menu)", "type in the game files", "Count", "Price", "Total"),
             total="Razem" if pl else "Total", plan="Plan użycia" if pl else "How to use it",
             why="Dlaczego ta armia" if pl else "Why this army", server="Komenda serwera" if pl else "Server command",
             note=("N to numer Twojej drużyny w custom battle, liczony od 0 (pierwsza drużyna = 0). "
                   "Ceny to poziom podstawowy, bez ulepszeń broni, zbroi i doświadczenia - sprawdź sumę w menu gry."
                   if pl else "N is your team's number in the custom battle, counting from 0 (first team = 0). Prices "
                   "are the basic level, without weapon, armour or experience upgrades - check the total in the menu."),
             units_n="oddziałów" if pl else "units")
    server_cmd = (".venv\\Scripts\\python -m rome_ai.server --backend claude-code --effort medium --sides all "
                  f"--personality N={res['personality']}")
    head = f"{W['battle']} · {total} / {budget} ({total * 100 // max(budget, 1)}%) · {count} / {max_units} {W['units_n']}"
    cname = (cmd.name_pl if pl else cmd.name) if cmd else res["personality"]
    md = [f"# {W['title']}", "", f"*{head}*", "", f"## {W['commander']}: {cname} (`{res['personality']}`)", "",
          f"**{W['why_c']}:** {res.get('reason', '')}", "", f"## {W['units']}", "",
          "| # | " + " | ".join(W["cols"]) + " |", "|---|---|---|---|---|---|"]
    md += [f"| {i} | **{a}** | {b} | {n} | {c} | {s} |" for i, (a, b, n, c, s) in enumerate(rows, 1)]
    md += [f"| | **{W['total']}** | | **{count}** | | **{total}** |", "", f"## {W['plan']}", "", res.get("plan", ""), "",
           f"## {W['why']}", "", res.get("why", ""), "", f"## {W['server']}", "", "```powershell", server_cmd, "```", "",
           f"*{W['note']}*", ""]
    e = html.escape
    body = [f"<h1>{e(W['title'])}</h1>", f'<p class="meta">{e(head)}</p>',
            f'<div class="card"><h3>{e(W["commander"])}: {e(cname)} <span class="chip">{e(res["personality"])}</span></h3>'
            f'<p><b>{e(W["why_c"])}:</b> {e(res.get("reason", ""))}</p></div>', f"<h2>{e(W['units'])}</h2>",
            '<div class="wrap"><table><tr><th>#</th>' + "".join(f"<th>{e(c)}</th>" for c in W["cols"]) + "</tr>"]
    body += [f"<tr><td>{i}</td><td><b>{e(a)}</b></td><td class=meta>{e(b)}</td><td>{n}</td><td>{c}</td><td>{s}</td></tr>"
             for i, (a, b, n, c, s) in enumerate(rows, 1)]
    body += [f"<tr><td></td><td><b>{e(W['total'])}</b></td><td></td><td><b>{count}</b></td><td></td><td><b>{total}</b>"
             f"</td></tr></table></div>", f"<h2>{e(W['plan'])}</h2><p>{e(res.get('plan', ''))}</p>",
             f"<h2>{e(W['why'])}</h2><p>{e(res.get('why', ''))}</p>", f"<h2>{e(W['server'])}</h2>",
             f'<pre class="card">{e(server_cmd)}</pre>', f'<p class="meta">{e(W["note"])}</p>']
    return "\n".join(md), P.page(W["title"], "\n".join(body), lang)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--faction", help="your faction, e.g. macedon (see --list)")
    p.add_argument("--enemy", nargs="+", help="the enemy faction(s)")
    p.add_argument("--budget", type=int, help="denarii, as set in the custom battle")
    p.add_argument("--battle", choices=list(BATTLES), default="field")
    p.add_argument("--personality", default="auto", help="a commander's id, or auto (Claude chooses)")
    p.add_argument("--units", type=int, default=20, help="most units in the army (the game allows 20)")
    p.add_argument("--cap", nargs="+", default=[], metavar="ROLE=N",
                   help="hard limit on units of a role, e.g. missile=5 (roles: infantry missile cavalry handler)")
    p.add_argument("--model", default="claude-sonnet-5-5")
    p.add_argument("--effort", default="medium")
    p.add_argument("--lang", choices=["pl", "en"], default="pl", help="language of the army sheet")
    p.add_argument("--out", type=Path, default=ROOT / "armies")
    p.add_argument("--list", action="store_true", help="list the factions and commanders")
    p.add_argument("--check", action="store_true", help="test the army rules (no model call)")
    a = p.parse_args()
    P.find_game_data()
    if a.check:
        selftest()
        return
    if a.list:
        types = P.army_types()
        for k, t in types.items():
            print(f"{t.name}: " + ", ".join(f"{f} ({P.FACTIONS[f][0]})" for f in t.list("factions")))
        print("\nCommanders: auto, " + ", ".join(P.commanders()))
        return
    if not (a.faction and a.enemy and a.budget):
        p.error("--faction, --enemy and --budget are needed (or --list)")
    for f in [a.faction, *a.enemy]:
        if f not in P.FACTIONS:
            p.error(f"unknown faction {f!r} - see --list")
    if a.personality != "auto" and a.personality not in P.commanders():
        p.error(f"unknown commander {a.personality!r} - see --list")
    res = asyncio.run(recruit(a.faction, a.enemy, a.budget, a.battle, a.personality, a.units, a.model, a.effort, a.lang,
                             {k: int(v) for k, _, v in (s.partition('=') for s in a.cap)}))
    md, page = render(res, a.faction, a.enemy, a.budget, a.battle, a.units, a.lang)
    a.out.mkdir(parents=True, exist_ok=True)
    stem = a.out / f"{a.faction}-vs-{'-'.join(a.enemy)}-{a.battle}"
    stem.with_suffix(".md").write_text(md, encoding="utf-8", newline="\n")
    stem.with_suffix(".html").write_text(page, encoding="utf-8", newline="\n")
    sys.stdout.reconfigure(errors="replace")  # a Windows console may not show every Polish letter
    print(md)
    print(f"written {stem}.html and .md")


if __name__ == "__main__":
    main()
