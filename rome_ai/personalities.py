"""Army types, commanders (personalities) and the battles of antiquity (personalities.md, battles.md).

    python -m rome_ai.personalities check    # are both files consistent with each other and with the game's data?
    python -m rome_ai.personalities docs     # the catalogue in docs/ (commanders.md / .pl.md / .html / .pl.html)

At the start of a battle the server tells each general which army he leads and which he fights (recognised from
the unit types: export_descr_unit.txt says which factions may have each type), the battles between such armies,
and - with --personality - the commander whose style he follows.
"""

from __future__ import annotations

import html
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from . import units_db

ROOT = Path(__file__).resolve().parents[1]
PERSONALITIES_FILE = ROOT / "personalities.md"
BATTLES_FILE = ROOT / "battles.md"
DOCS_DIR = ROOT / "docs"

FACTIONS = {  # id: (English, Polish)
    "romans_julii": ("the Julii", "Juliusze"), "romans_brutii": ("the Brutii", "Brutusowie"),
    "romans_scipii": ("the Scipii", "Scypionowie"), "romans_senate": ("the Senate", "Senat"),
    "macedon": ("Macedon", "Macedonia"), "greek_cities": ("the Greek Cities", "Miasta greckie"),
    "seleucid": ("the Seleucid Empire", "Imperium Seleukidów"), "thrace": ("Thrace", "Tracja"),
    "parthia": ("Parthia", "Partia"), "pontus": ("Pontus", "Pont"), "armenia": ("Armenia", "Armenia"),
    "scythia": ("Scythia", "Scytia"), "gauls": ("Gaul", "Galia"), "germans": ("Germania", "Germania"),
    "britons": ("Britannia", "Brytania"), "dacia": ("Dacia", "Dacja"), "carthage": ("Carthage", "Kartagina"),
    "numidia": ("Numidia", "Numidia"), "spain": ("Spain", "Hiszpania"), "egypt": ("Egypt", "Egipt"),
}
MAX_LESSONS = 6  # battles shown to a general (the system prompt is cached, but it is read on every plan)


@dataclass
class Entry:
    id: str
    name: str
    name_pl: str
    fields: dict[str, str] = field(default_factory=dict)
    lines: list[str] = field(default_factory=list)  # the "- " lines: what goes to the model

    def list(self, key: str) -> list[str]:
        return [x.strip() for x in self.fields.get(key, "").split(",") if x.strip()]


def _parse(path: Path) -> dict[str, dict[str, Entry]]:
    """`## Section` -> `### id | English | Polish` entries with `key: value` fields and `- ` lines."""
    out: dict[str, dict[str, Entry]] = {}
    section, cur = "", None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("### "):
            parts = [p.strip() for p in line[4:].split("|")] + ["", ""]
            cur = Entry(parts[0], parts[1] or parts[0], parts[2] or parts[1] or parts[0])
            out.setdefault(section, {})[cur.id] = cur
        elif line.startswith("## "):
            section, cur = line[3:].strip().lower(), None
        elif cur is not None and line.startswith("- "):
            cur.lines.append(line[2:].strip())
        elif cur is not None and (m := re.match(r"^([a-z_]+):\s*(.*)$", line)):
            cur.fields[m.group(1)] = m.group(2).strip()
    return out


def army_types() -> dict[str, Entry]:
    return _parse(PERSONALITIES_FILE).get("army types", {})


def commanders() -> dict[str, Entry]:
    return _parse(PERSONALITIES_FILE).get("commanders", {})


def battles() -> dict[str, Entry]:
    return _parse(BATTLES_FILE).get("battles", {})


def sides(b: Entry) -> tuple[str, str, bool]:
    """(winner, loser, draw) of a battle."""
    s = b.fields.get("sides", "")
    draw = "=" in s
    a, _, c = s.partition("=" if draw else ">")
    return a.strip(), c.strip(), draw


# --- which army a side leads ---------------------------------------------------------------------------------


@dataclass
class Army:
    type: str | None  # army type id, None if the units do not tell
    factions: list[str]  # the most likely factions (all of them when the units fit several equally)

    def describe(self, types: dict[str, Entry], pl: bool = False) -> str:
        if self.type is None:
            return "nierozpoznana" if pl else "not recognised from its units"
        t = types[self.type]
        names = [FACTIONS.get(f, (f, f))[1 if pl else 0] for f in self.factions]
        who = (" lub " if pl else " or ").join(names)
        return f"{t.name_pl if pl else t.name} ({who})" if who else (t.name_pl if pl else t.name)


def identify(unit_names: list[str], types: dict[str, Entry] | None = None) -> Army:
    """The army type and factions of one side, from its unit types: each unit counts for every faction that may
    have it; the factions that may have the most of them win."""
    types = army_types() if types is None else types
    of_type = {f: t for t, e in types.items() for f in e.list("factions")}
    db = units_db.database()
    score: Counter = Counter()
    for name in unit_names:
        for f in units_db.owners(db.get(name, {})):
            if f in of_type:  # rebels ("slave") and unknown owners say nothing
                score[f] += 1
    if not score:
        return Army(None, [])
    best = max(score.values())
    top = sorted(f for f, s in score.items() if s == best)
    kind = Counter(of_type[f] for f in top).most_common(1)[0][0]
    return Army(kind, [f for f in top if of_type[f] == kind])


# --- what a general is told --------------------------------------------------------------------------------


def lessons(mine: str | None, foes: list[str | None], all_battles: dict[str, Entry] | None = None) -> list[Entry]:
    """Battles between the general's army type and each enemy type: direct ones first, then analogies (`also`)."""
    all_battles = battles() if all_battles is None else all_battles
    picked: list[Entry] = []
    for foe in dict.fromkeys(f for f in foes if f):
        if mine is None:
            continue
        direct, similar = [], []
        for b in all_battles.values():
            a, c, _ = sides(b)
            if {a, c} == {mine, foe}:
                direct.append(b)
            elif (mine in (a, c) and foe in b.list("also")) or (foe in (a, c) and mine in b.list("also")):
                similar.append(b)
        picked += [b for b in direct + similar if b not in picked][: max(2, MAX_LESSONS // max(1, len(foes)))]
    return picked[:MAX_LESSONS]


def _battle_text(b: Entry, types: dict[str, Entry]) -> str:
    a, c, draw = sides(b)
    an, cn = (types[x].name if x in types else x for x in (a, c))
    result = f"{an} and {cn} fought to a draw" if draw else f"{an} beat {cn}"
    return f"{b.name} ({b.fields.get('year', '')}), {result}: {b.fields.get('summary', '')} Lessons: " + " ".join(b.lines)


def doctrine(mine: Army, foes: list[tuple[int, Army]], commander: str | None = None, reason: str | None = None) -> str:
    """The block of the system prompt about this battle: who you are, who you fight, your personality, history."""
    types, cmds = army_types(), commanders()
    out = [f"YOUR ARMY: {mine.describe(types)}" + (f" - {types[mine.type].fields.get('summary', '')}" if mine.type else "")]
    for alliance, a in foes:
        tag = f" (side #{alliance + 1}xxxx)" if len(foes) > 1 else ""
        out.append(f"ENEMY{tag}: {a.describe(types)}" + (f" - {types[a.type].fields.get('summary', '')}" if a.type else ""))
    c = cmds.get(commander) if commander else None
    if c is not None:
        out.append(
            f"\nYOUR PERSONALITY - you command in the style of {c.name}: {c.fields.get('summary', '')}"
            + (f" (Chosen because: {reason})" if reason else "")
            + "\nThe STRATEGY above is the standard craft of this game that every commander follows. Keep to it, "
              "except where these orders of yours deliberately depart from it or put something else first - there, "
              "these orders win:\n" + "\n".join(f"- {x}" for x in c.lines))
    hist = lessons(mine.type, [a.type for _, a in foes])
    if hist:
        out.append("\nHISTORY - battles between armies like yours and your enemy's. Learn from the winners and the "
                   "losers alike; your units in this game are not exactly theirs:\n"
                   + "\n".join(f"- {_battle_text(b, types)}" for b in hist))
    return "\n".join(out)


def autopick_choices() -> dict[str, Entry]:
    """The commanders --personality auto chooses from: the historical ones (those with suggested army types)."""
    return {k: c for k, c in commanders().items() if c.list("types")}


def fallback_pick(mine: Army) -> str | None:
    """auto without a model that can choose: the first commander suggested for the army type."""
    for k, c in autopick_choices().items():
        if mine.type in c.list("types"):
            return k
    return None


def catalogue_for_model() -> str:
    types = army_types()
    return "\n".join(
        f"- {k}: {c.name}" + (f" (suits {', '.join(types[t].name for t in c.list('types') if t in types)} armies)"
                              if c.list("types") else "") + f" - {c.fields.get('summary', '')}"
        for k, c in autopick_choices().items())


PICK_SYSTEM = (
    "You choose the commander whose style an AI general will follow in a battle of Rome: Total War. Every commander "
    "can lead any army; the armies he suits are only a hint. Choose the one whose style gives THIS army the best "
    "chance against THIS enemy, given the units on both sides, the kind of battle and the lessons of history. "
    "Answer with the commander's id and one or two sentences why.")


async def pick(general, mine: Army, foes: list[tuple[int, Army]], my_units: list[str], foe_units: list[str],
               situation: str) -> tuple[str | None, str]:
    """--personality auto: the general's own model chooses a commander (claude-code backend); other backends take
    the first commander suggested for the army type."""
    choices = autopick_choices()
    ask = getattr(general, "ask", None)
    if ask is None:  # ponytail: only claude-code can ask; add ask() to the API backends when they need auto
        return fallback_pick(mine), "first commander suggested for this army type (this backend cannot choose)"
    types = army_types()
    hist = lessons(mine.type, [a.type for _, a in foes])

    def counted(names: list[str]) -> str:
        return ", ".join(f"{n} x{k}" for n, k in Counter(names).most_common())

    user = (f"Battle: {situation}\nYour army: {mine.describe(types)}. Your units: {counted(my_units)}\n"
            + "\n".join(f"Enemy: {a.describe(types)}" for _, a in foes) + f". Enemy units: {counted(foe_units)}\n"
            + ("History of such battles:\n" + "\n".join(f"- {_battle_text(b, types)}" for b in hist) + "\n" if hist else "")
            + "\nCommanders to choose from:\n" + catalogue_for_model())
    schema = {"type": "object", "additionalProperties": False, "required": ["personality", "reason"],
              "properties": {"personality": {"type": "string", "enum": list(choices)},
                             "reason": {"type": "string"}}}
    res = await ask(PICK_SYSTEM, user, schema)
    k = res.get("personality")
    return (k if k in choices else fallback_pick(mine)), str(res.get("reason", ""))


# --- the catalogue for people (docs/) ----------------------------------------------------------------------

T = {  # interface words of the catalogue
    "en": dict(title="Commanders and army types", intro=(
        "Generated from personalities.md and battles.md (python -m rome_ai.personalities docs). strategy.md is the "
        "standard craft every general follows; a commander only adds his deliberate departures from it. Every "
        "commander can lead any army - the army types only suggest who fits. Start the server with "
        "--personality <id> (e.g. 0=hannibal 1=scipio), or --personality auto to let each general choose."),
        types="Army types", factions="Factions", fits="Suggested commanders", commanders="Commanders",
        id="id", suits="Suits", universal="any army", recruits="Preferred units", history="Battles",
        orders="Orders the general follows", battles="Battles of antiquity", beat="beat", draw="draw with",
        lessons="Lessons", other="Other lang", other_link="commanders.pl.html", other_md="commanders.pl.md",
        other_label="Polski"),
    "pl": dict(title="Dowódcy i typy armii", intro=(
        "Wygenerowane z personalities.md i battles.md (python -m rome_ai.personalities docs). strategy.md to "
        "wspólne rzemiosło, którego trzyma się każdy wódz; dowódca dodaje tylko swoje celowe odstępstwa. Każdy "
        "dowódca może prowadzić dowolną armię - typy armii tylko podpowiadają, kto pasuje. Serwer uruchamiasz z "
        "--personality <id> (np. 0=hannibal 1=scipio) albo --personality auto, żeby każdy wódz wybrał sam."),
        types="Typy armii", factions="Państwa", fits="Podpowiadani dowódcy", commanders="Dowódcy",
        id="id", suits="Pasuje do", universal="każda armia", recruits="Preferowane jednostki", history="Bitwy",
        orders="Rozkazy, które czyta wódz (po angielsku)", battles="Bitwy starożytności", beat="pokonała",
        draw="remis z", lessons="Lekcje (po angielsku, dla wodza)", other="Inny język",
        other_link="commanders.html", other_md="commanders.md", other_label="English"),
}


def _year(y: str, pl: bool) -> str:
    return y.replace("BC", "p.n.e.").replace("AD", "n.e.") if pl else y


def catalogue(lang: str) -> dict:
    """Everything the catalogue shows, in one language: plain data both renderers use."""
    pl = lang == "pl"
    types, cmds, bats = army_types(), commanders(), battles()
    tname = {k: (t.name_pl if pl else t.name) for k, t in types.items()}

    def nm(e: Entry) -> str:
        return e.name_pl if pl else e.name

    def f(e: Entry, key: str) -> str:
        return e.fields.get(f"{key}_pl" if pl else key, "") or e.fields.get(key, "")

    rows = [dict(name=nm(t), factions=", ".join(FACTIONS.get(x, (x, x))[1 if pl else 0] for x in t.list("factions")),
                 summary=f(t, "summary"), fits=", ".join(nm(c) for c in cmds.values() if k in c.list("types")))
            for k, t in types.items()]
    people = [dict(id=k, name=nm(c), suits=", ".join(tname.get(t, t) for t in c.list("types")) or T[lang]["universal"],
                   summary=f(c, "summary"), recruits=f(c, "recruits"),
                   battles=", ".join(nm(bats[b]) for b in c.list("battles") if b in bats), orders=c.lines)
              for k, c in cmds.items()]
    fights = []
    for b in bats.values():
        a, c, draw = sides(b)
        fights.append(dict(name=nm(b), year=_year(b.fields.get("year", ""), pl),
                           result=f"{tname.get(a, a)} {T[lang]['draw'] if draw else T[lang]['beat']} {tname.get(c, c)}",
                           summary=f(b, "summary"), lessons=b.lines))
    return dict(types=rows, commanders=people, battles=fights)


def render_md(lang: str) -> str:
    w, d = T[lang], catalogue(lang)
    out = [f"# {w['title']}", "", f"[{w['other_label']}]({w['other_md']})", "", w["intro"], "", f"## {w['types']}", "",
           f"| | {w['factions']} | {w['fits']} |", "|---|---|---|"]
    out += [f"| **{r['name']}** | {r['factions']} | {r['fits']} |" for r in d["types"]]
    for r in d["types"]:
        out += ["", f"**{r['name']}** - {r['summary']}"]
    out += ["", f"## {w['commanders']}"]
    for c in d["commanders"]:
        out += ["", f"### {c['name']} (`{c['id']}`)", "", f"*{w['suits']}: {c['suits']}*", "", c["summary"], "",
                f"- **{w['recruits']}:** {c['recruits']}"]
        if c["battles"]:
            out.append(f"- **{w['history']}:** {c['battles']}")
        out += ["", f"<details><summary>{w['orders']}</summary>", ""] + [f"- {x}" for x in c["orders"]] + ["", "</details>"]
    out += ["", f"## {w['battles']}"]
    for b in d["battles"]:
        out += ["", f"### {b['name']} ({b['year']})", "", f"*{b['result']}*", "", b["summary"], "",
                f"{w['lessons']}:"] + [f"- {x}" for x in b["lessons"]]
    return "\n".join(out) + "\n"


CSS = """
:root{--bg:#f7f4ee;--panel:#fffdf8;--ink:#2b2420;--muted:#6f645a;--line:#e3dbcf;--accent:#8c2f1b;--chip:#efe6d8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17130f;--panel:#211b16;--ink:#eee6da;
--muted:#ab9f91;--line:#3a3129;--accent:#e08a63;--chip:#2e261f}}
:root[data-theme="dark"]{--bg:#17130f;--panel:#211b16;--ink:#eee6da;--muted:#ab9f91;--line:#3a3129;--accent:#e08a63;--chip:#2e261f}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Georgia,"Times New Roman",serif}
main{max-width:980px;margin:0 auto;padding:24px 16px 64px}h1{font-size:2rem;margin:.2em 0}h2{margin-top:2.2em;
border-bottom:2px solid var(--accent);padding-bottom:.2em}h3{margin:0 0 .2em}a{color:var(--accent)}
.intro{color:var(--muted)}.wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;min-width:560px}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}th{color:var(--muted);font-weight:normal}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:12px 0}
.meta{color:var(--muted);font-size:.92em}.chip{display:inline-block;background:var(--chip);border-radius:999px;padding:1px 10px;
font:13px/1.6 ui-monospace,Consolas,monospace}details{margin-top:8px}summary{cursor:pointer;color:var(--accent)}
pre{white-space:pre-wrap;overflow-wrap:anywhere}ul{margin:.4em 0;padding-left:1.2em}.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}
code{font:14px ui-monospace,Consolas,monospace;background:var(--chip);padding:1px 5px;border-radius:4px}
pre.code{font:14px/1.5 ui-monospace,Consolas,monospace;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px}
ol{margin:.3em 0}
"""


def page(title: str, body: str, lang: str) -> str:
    """A self-contained page in the catalogue's style (also used for the recruit sheets)."""
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" '
            f'content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style>'
            f"</head><body><main>{body}</main></body></html>\n")


def render_html(lang: str) -> str:
    w, d = T[lang], catalogue(lang)
    e = html.escape
    b = [f"<h1>{e(w['title'])}</h1>", f'<p><a href="{w["other_link"]}">{e(w["other_label"])}</a></p>',
         f'<p class="intro">{e(w["intro"])}</p>', f"<h2>{e(w['types'])}</h2>",
         f'<div class="wrap"><table><tr><th></th><th>{e(w["factions"])}</th><th>{e(w["fits"])}</th></tr>']
    b += [f"<tr><td><b>{e(r['name'])}</b><div class=meta>{e(r['summary'])}</div></td><td>{e(r['factions'])}</td>"
          f"<td>{e(r['fits'])}</td></tr>" for r in d["types"]]
    b += ["</table></div>", f"<h2>{e(w['commanders'])}</h2>", '<div class="grid">']
    for c in d["commanders"]:
        b.append(f'<div class="card"><h3>{e(c["name"])}</h3><span class="chip">{e(c["id"])}</span>'
                 f'<div class="meta">{e(w["suits"])}: {e(c["suits"])}</div><p>{e(c["summary"])}</p>'
                 f'<div class="meta"><b>{e(w["recruits"])}:</b> {e(c["recruits"])}</div>'
                 + (f'<div class="meta"><b>{e(w["history"])}:</b> {e(c["battles"])}</div>' if c["battles"] else "")
                 + f'<details><summary>{e(w["orders"])}</summary><ul>'
                 + "".join(f"<li>{e(x)}</li>" for x in c["orders"]) + "</ul></details></div>")
    b += ["</div>", f"<h2>{e(w['battles'])}</h2>"]
    for x in d["battles"]:
        b.append(f'<div class="card"><h3>{e(x["name"])} <span class="meta">({e(x["year"])})</span></h3>'
                 f'<div class="meta">{e(x["result"])}</div><p>{e(x["summary"])}</p>'
                 f'<details><summary>{e(w["lessons"])}</summary><ul>'
                 + "".join(f"<li>{e(y)}</li>" for y in x["lessons"]) + "</ul></details></div>")
    return page(w["title"], "\n".join(b), lang)


def _md_inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\[([^\]]+)\]\(([^)]+?)(\.md)?\)", lambda m: f'<a href="{m.group(2)}{".html" if m.group(3) else ""}">'
                  f"{m.group(1)}</a>", s)


def md_to_html(text: str) -> str:
    """The little markdown the guides use (docs/guide*.md): headings, paragraphs, lists, tables, code blocks,
    `code`, **bold** and links (to .md files -> .html). ponytail: no markdown library in requirements.txt."""
    lines, out, para, i = text.splitlines(), [], [], 0

    def flush() -> None:
        if para:
            out.append(f"<p>{_md_inline(' '.join(para))}</p>")
            para.clear()

    while i < len(lines):
        raw, s = lines[i], lines[i].strip()
        if s.startswith("```"):  # a code block, also one indented under a list item
            flush()
            indent, code = len(raw) - len(raw.lstrip()), []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i][indent:] if not lines[i][:indent].strip() else lines[i])
                i += 1
            out.append(f'<pre class="code">{html.escape(chr(10).join(code))}</pre>')
        elif not s:
            flush()
        elif m := re.match(r"^(#{1,3}) (.*)", s):
            flush()
            out.append(f"<h{len(m.group(1))}>{_md_inline(m.group(2))}</h{len(m.group(1))}>")
        elif s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not re.match(r"^\|[\s\-:|]+\|$", lines[i].strip()):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="wrap"><table><tr>' + "".join(f"<th>{_md_inline(c)}</th>" for c in rows[0]) + "</tr>"
                       + "".join("<tr>" + "".join(f"<td>{_md_inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
                       + "</table></div>")
            continue
        elif s.startswith("- "):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append("<ul>" + "".join(f"<li>{_md_inline(x)}</li>" for x in items) + "</ul>")
            continue
        elif m := re.match(r"^(\d+)\. (.*)", s):
            flush()
            out.append(f'<ol start="{m.group(1)}"><li>{_md_inline(m.group(2))}</li></ol>')
        else:
            para.append(s)
        i += 1
    flush()
    return "\n".join(out)


def write_docs() -> list[Path]:
    DOCS_DIR.mkdir(exist_ok=True)
    out = []
    for lang, suffix in (("en", ""), ("pl", ".pl")):
        for ext, render in (("md", render_md), ("html", render_html)):
            p = DOCS_DIR / f"commanders{suffix}.{ext}"
            p.write_text(render(lang), encoding="utf-8", newline="\n")
            out.append(p)
        guide = DOCS_DIR / f"guide{suffix}.md"  # written by hand; its page is made from it
        if guide.is_file():
            text = guide.read_text(encoding="utf-8")
            title = next((x[2:] for x in text.splitlines() if x.startswith("# ")), "Rome Battle AI")
            p = guide.with_suffix(".html")
            p.write_text(page(title, md_to_html(text), lang), encoding="utf-8", newline="\n")
            out.append(p)
    return out


# --- checks ------------------------------------------------------------------------------------------------

# a real battle's units (2026-11-15: Macedon against a Roman family), for the identify() check
SAMPLE_MACEDON = ["greek archer", "greek heavy cavalry", "greek medium cavalry", "greek pikemen", "greek royal cavalry",
                  "greek royal pikemen", "merc cretan archers"]
SAMPLE_ROMAN = ["roman archer auxillia", "roman generals guard cavalry", "roman legionary cohort i", "roman princeps",
                "roman samnite gladiator", "roman triarii", "roman wardogs"]


def check() -> list[str]:
    """Problems in personalities.md / battles.md, or with the game's data; empty when all is well."""
    errors: list[str] = []
    types, cmds, bats = army_types(), commanders(), battles()
    of_type = {f: t for t, e in types.items() for f in e.list("factions")}
    for f in FACTIONS:
        if f not in of_type:
            errors.append(f"faction {f} has no army type")
    for f in of_type:
        if f not in FACTIONS:
            errors.append(f"army types name an unknown faction {f}")
    for k, c in cmds.items():
        for t in c.list("types"):
            if t not in types:
                errors.append(f"commander {k}: unknown army type {t}")
        for b in c.list("battles"):
            if b not in bats:
                errors.append(f"commander {k}: unknown battle {b}")
        for key in ("summary", "summary_pl", "recruits", "recruits_pl"):
            if not c.fields.get(key):
                errors.append(f"commander {k}: no {key}")
        if not c.lines:
            errors.append(f"commander {k}: no orders")
    for k, b in bats.items():
        a, c, _ = sides(b)
        for t in (a, c, *b.list("also")):
            if t not in types:
                errors.append(f"battle {k}: unknown army type {t!r}")
        for key in ("year", "summary", "summary_pl"):
            if not b.fields.get(key):
                errors.append(f"battle {k}: no {key}")
    edu = units_db.GAME_DATA / units_db.EDU_FILES[0]
    if edu.is_file():  # every base-game faction that owns units has an army type
        base = units_db._parse(edu.read_text(encoding="latin-1"))
        owned = set().union(*(units_db.owners(u) for u in base.values())) - {"slave"}
        for f in sorted(owned - set(of_type)):
            errors.append(f"faction {f} owns units in the game but has no army type")
        m, r = identify(SAMPLE_MACEDON, types), identify(SAMPLE_ROMAN, types)
        if (m.type, m.factions) != ("hellenistic", ["macedon"]):
            errors.append(f"sample Macedonian army identified as {m}")
        if r.type != "roman":
            errors.append(f"sample Roman army identified as {r}")
    else:
        errors.append(f"game data not found at {units_db.GAME_DATA} - set ROME_DATA (army recognition not checked)")
    return errors


def find_game_data() -> None:
    """The scripts run without the game's hook: look for the game's data in the usual Steam folders."""
    import os

    if os.environ.get("ROME_DATA") or (units_db.GAME_DATA / units_db.EDU_FILES[0]).is_file():
        return
    for p in (Path("C:/Program Files (x86)/Steam/steamapps/common/Total War ROME REMASTERED/Contents/Resources/Data"),
              Path.home() / ".steam/steam/steamapps/common/Total War ROME REMASTERED/share/data"):
        if (p / units_db.EDU_FILES[0]).is_file():
            units_db.GAME_DATA = p
            units_db.database.cache_clear()
            units_db.display_names.cache_clear()
            return


def main() -> None:
    find_game_data()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "docs":
        for p in write_docs():
            print("written", p)
    elif cmd == "check":
        errors = check()
        print("\n".join(errors) if errors else
              f"OK: {len(army_types())} army types, {len(commanders())} commanders, {len(battles())} battles")
        sys.exit(1 if errors else 0)
    else:
        sys.exit(f"unknown command {cmd!r}: use check or docs")


if __name__ == "__main__":
    main()
