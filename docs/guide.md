# Rome Battle AI - modes and commands

[Polski](guide.pl.md) · [Commanders catalogue](commanders.md)

A short cheat sheet: which modes this fork has and how to start them. Type every command in PowerShell, in the
mod's folder:

```powershell
cd C:\rome-battle-ai
```

The AI server must be running before the battle starts. Leave its window open while you play and stop it with
**Ctrl+C**. Changed options take effect only after the server is started again.

## 1. Who commands which side

| Mode | Command | What happens |
|---|---|---|
| **You against Claude** | `.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium` | Claude commands the computer's side, you command yours. |
| **Claude against Claude** | `.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all` | Every side of the battle gets its own Claude. You only watch. |
| **3-4 teams** | the same command with `--sides all` | Every team of the custom battle gets its own Claude. All fight all. |

With `--sides all`, do not give orders to your own units - you would fight Claude for them. Move the camera as
much as you like. Pausing the game pauses the generals.

A team is not an army: if a team has two armies, one Claude commands both.

## 2. The general's character (`--personality`)

Every general, the standard one too, knows which faction he leads, whom he fights and how such armies fought each
other in history. `--personality` adds the style of a particular commander. Without it, the general follows the
standard tactics of `strategy.md`.

| What you want | Add to the server command |
|---|---|
| The standard general | nothing |
| The standard general who **never retreats** and, once the battle cannot be won, kills as many enemies as he can | `--personality no_retreat` |
| The Berserker: fights to the death from the start, only the kills count | `--personality berserker` |
| One commander for every side | `--personality hannibal` |
| Different commanders for different sides | `--personality 0=hannibal 1=scipio` |
| Each general chooses a commander for his army and his enemy | `--personality auto` |
| A mix | `--personality 0=caesar 1=auto` |

**Side numbers:** 0 is the first team, 1 the second, and so on. When the battle starts, the server prints
`took control of alliance N` and a line `[alliance N] army: ...; personality: ...` - there you can see which side
has which number and whom it got.

**The commanders** with their descriptions are in the [catalogue](commanders.md). Just the names:

```powershell
.venv\Scripts\python -m rome_ai.recruit --list
```

## 3. Model and thinking time

| Option | What it does |
|---|---|
| `--model claude-sonnet-5-5` | The default model. Fast and good. |
| `--model claude-opus-5-5` | Stronger, slower, uses up the usage limit faster. |
| `--effort low` / `medium` / `high` | How long the general thinks before each plan. |

The battle does not wait for the general: a high `effort` means longer thinking while the units fight without
new orders. Two sensible settings: Sonnet with `medium`, or Opus with `low`.

Usage: every side with Claude is a separate general, so `--sides all` with two teams uses the limit twice as fast,
with four teams four times as fast. When the limit runs out, the game's own AI takes the army; the general tries
to come back every minute.

## 4. Picking an army before the battle

Claude picks an army within the custom battle budget and writes a sheet you click it together from.

```powershell
.venv\Scripts\python -m rome_ai.recruit --faction macedon --enemy romans_julii --budget 15000 --battle field
```

| Option | Meaning |
|---|---|
| `--faction` | Your faction, e.g. `macedon`, `carthage`, `romans_julii` (full list: `--list`) |
| `--enemy` | The enemy faction, or several: `--enemy romans_scipii gauls` |
| `--budget` | Denarii, as set in the custom battle |
| `--battle` | `field` (field battle), `siege-attack` (you attack a town), `siege-defense` (you defend a town) |
| `--personality` | A commander, or `auto` (the default). The commander decides which units are picked. |
| `--units` | Most units in the army (default 20, what an army holds) |
| `--lang` | Language of the sheet: `pl` (default) or `en` |
| `--model`, `--effort` | Model for the picking (default Sonnet, `medium`) |

The result goes to `C:\rome-battle-ai\armies\`, as `.html` and `.md`. The sheet has:
- the units with their names as in the game's menu, counts and prices,
- the chosen commander and why,
- how to use the army,
- a ready server command with the same commander.

Prices are the basic level, without weapon, armour or experience upgrades - check the total in the game's menu.

## 5. Ready setups

**You against a Claude who never gives up:**

```powershell
.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --personality no_retreat
```

**Hannibal against Scipio:**

```powershell
.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all --personality 0=hannibal 1=scipio
```

**Four teams, each general chooses his commander:**

```powershell
.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all --personality auto
```

**The full cycle: Claude picks both armies and fights with them:**

1. Pick an army for each side:
   ```powershell
   .venv\Scripts\python -m rome_ai.recruit --faction carthage --enemy romans_scipii --budget 12000 --battle field --lang en
   .venv\Scripts\python -m rome_ai.recruit --faction romans_scipii --enemy carthage --budget 12000 --battle field --lang en
   ```
2. Click both armies together in the custom battle from the sheets in `armies\`.
3. Start the server with the commanders from the sheets, e.g.:
   ```powershell
   .venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all --personality 0=hannibal 1=scipio
   ```
4. Start the battle and watch.

## 6. Where things are

| File or folder | What is in it |
|---|---|
| `strategy.md` | The standard tactics every general follows. You can edit them. |
| `rules.md` | Hard facts about the game. |
| `personalities.md` | Army types, their factions and the commanders. Add your own commander here. |
| `battles.md` | The battles of antiquity. |
| `docs\commanders.html` | The catalogue of commanders, army types and battles, to read. |
| `armies\` | The army sheets from the picker. |
| `logs\` | A record of every battle: what the general saw and what he decided. |

The server reads every `.md` file before each battle, so no restart is needed. After editing
`personalities.md` or `battles.md`, check them and rebuild the catalogue:

```powershell
.venv\Scripts\python -m rome_ai.personalities check
.venv\Scripts\python -m rome_ai.personalities docs
```

## 7. When something does not work

| Symptom | What to do |
|---|---|
| No `hello: rome-remastered v1` line in the server window | Check that `dinput8.dll` is in the game's folder, next to `Total War ROME REMASTERED.exe`. |
| `general failed: You've hit your session limit` | The Claude usage limit ran out. The game's AI commands the army; the general comes back by itself when the limit resets. |
| Units stand without orders | Look at the server window's log. |
| You want the original mod back | Copy `C:\rome-battle-ai\hook-windows\dinput8.dll` (v0.3) into the game's folder and start the server without `--sides` and `--personality`. |

Tests without the game (they use no Claude limit):

```powershell
.venv\Scripts\python -m rome_ai.personalities check
.venv\Scripts\python -m rome_ai.recruit --check
```
