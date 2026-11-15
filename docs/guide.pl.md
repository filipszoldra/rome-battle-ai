# Rome Battle AI - tryby i komendy

[English](guide.md) · [Katalog dowódców](commanders.pl.md)

Krótka ściąga: jakie tryby ma ten fork i jak je uruchomić. Wszystkie komendy wpisujesz w PowerShell, w folderze
moda:

```powershell
cd C:\rome-battle-ai
```

Serwer AI musi działać, zanim zacznie się bitwa. Okno serwera zostaw otwarte do końca gry. Zatrzymujesz go
klawiszami **Ctrl+C**. Zmiany w kodzie albo w opcjach działają dopiero po ponownym uruchomieniu serwera.

## 1. Kto dowodzi którą stroną

| Tryb | Komenda | Co się dzieje |
|---|---|---|
| **Ty kontra Claude** | `.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium` | Claude dowodzi stroną komputera, Ty swoją. |
| **Claude kontra Claude** | `.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all` | Każda strona bitwy ma osobnego Claude. Ty tylko oglądasz. |
| **3-4 drużyny** | ta sama komenda z `--sides all` | Każda drużyna z custom battle ma osobnego Claude. Wszystkie walczą ze wszystkimi. |

Przy `--sides all` nie wydawaj rozkazów swoim oddziałom, bo będziesz się kłócić z Claude. Kamerą możesz
latać, jak chcesz. Pauza wstrzymuje wodzów.

Drużyna to nie armia: jeśli w jednej drużynie są 2 armie, jeden Claude dowodzi obiema.

## 2. Charakter wodza (`--personality`)

Każdy wódz, także domyślny, wie, jakim państwem gra, z kim walczy i jak takie armie walczyły ze sobą w
historii. Opcja `--personality` dodaje do tego styl konkretnego dowódcy. Bez tej opcji wódz gra według
standardowej taktyki z `strategy.md`.

| Co chcesz | Dopisz do komendy serwera |
|---|---|
| Domyślny wódz | nic |
| Domyślny wódz, który **nigdy się nie wycofuje**, a gdy bitwy nie da się wygrać, zabija jak najwięcej wrogów | `--personality no_retreat` |
| Szaleniec: od początku walczy do końca, liczy się tylko liczba zabitych | `--personality berserker` |
| Jeden dowódca dla wszystkich stron | `--personality hannibal` |
| Różni dowódcy dla różnych stron | `--personality 0=hannibal 1=scipio` |
| Każdy wódz sam wybiera dowódcę dla swojej armii i swojego wroga | `--personality auto` |
| Mieszanie | `--personality 0=caesar 1=auto` |

**Numery stron:** 0 to pierwsza drużyna, 1 druga i tak dalej. Na początku bitwy serwer wypisuje
`took control of alliance N` i linię `[alliance N] army: ...; personality: ...`. Tam sprawdzisz, która strona
ma który numer i kogo dostała.

**Lista dowódców** z opisami jest w [katalogu](commanders.pl.md). Same nazwy wypisuje:

```powershell
.venv\Scripts\python -m rome_ai.recruit --list
```

## 3. Model i namysł

| Opcja | Co robi |
|---|---|
| `--model claude-sonnet-5-5` | Domyślny model. Szybki i dobry. |
| `--model claude-opus-5-5` | Mocniejszy, wolniejszy, szybciej zużywa limit. |
| `--effort low` / `medium` / `high` | Jak długo wódz myśli przed każdym planem. |

Bitwa nie czeka na wodza: wysoki `effort` oznacza dłuższe myślenie, a oddziały w tym czasie walczą bez nowych
rozkazów. Rozsądne są dwa ustawienia: Sonnet z `medium` albo Opus z `low`.

Zużycie limitu: każda strona z Claude to osobny wódz, więc `--sides all` przy 2 drużynach zużywa limit 2 razy
szybciej, a przy 4 drużynach 4 razy szybciej. Gdy limit się skończy, armią przejmuje zwykłe AI gry. Wódz co
minutę próbuje wrócić.

## 4. Dobór armii przed bitwą

Claude dobiera armię w budżecie custom battle i zapisuje kartę, z której ją wyklikasz w menu gry.

```powershell
.venv\Scripts\python -m rome_ai.recruit --faction macedon --enemy romans_julii --budget 15000 --battle field
```

| Opcja | Znaczenie |
|---|---|
| `--faction` | Twoje państwo, np. `macedon`, `carthage`, `romans_julii` (pełna lista: `--list`) |
| `--enemy` | Państwo wroga, albo kilka: `--enemy romans_scipii gauls` |
| `--budget` | Budżet w denarach, taki jak w custom battle |
| `--battle` | `field` (zwykła bitwa), `siege-attack` (atakujesz miasto), `siege-defense` (bronisz miasta) |
| `--personality` | Konkretny dowódca albo `auto` (domyślnie). Dowódca decyduje, jakie jednostki wybiera. |
| `--units` | Najwięcej oddziałów (domyślnie 20, tyle mieści armia) |
| `--lang` | Język karty: `pl` (domyślnie) albo `en` |
| `--model`, `--effort` | Model do doboru (domyślnie Sonnet, `medium`) |

Wynik ląduje w `C:\rome-battle-ai\armies\`, w plikach `.html` i `.md`. Karta zawiera:
- listę jednostek z nazwami jak w menu gry, liczbą i ceną,
- wybranego dowódcę i powód wyboru,
- plan użycia armii,
- gotową komendę serwera z tym samym dowódcą.

Ceny to poziom podstawowy, bez ulepszeń broni, zbroi i doświadczenia. Sprawdź sumę w menu gry.

## 5. Gotowe zestawy

**Grasz sam przeciw Claude, który się nie poddaje:**

```powershell
.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --personality no_retreat
```

**Hannibal kontra Scypion:**

```powershell
.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all --personality 0=hannibal 1=scipio
```

**4 drużyny, każdy wódz sam wybiera dowódcę:**

```powershell
.venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all --personality auto
```

**Pełny cykl: Claude dobiera obie armie i nimi walczy:**

1. Dobierz armię dla każdej strony:
   ```powershell
   .venv\Scripts\python -m rome_ai.recruit --faction carthage --enemy romans_scipii --budget 12000 --battle field
   .venv\Scripts\python -m rome_ai.recruit --faction romans_scipii --enemy carthage --budget 12000 --battle field
   ```
2. Wyklikaj obie armie w custom battle według kart z folderu `armies\`.
3. Uruchom serwer z dowódcami z kart, np.:
   ```powershell
   .venv\Scripts\python -m rome_ai.server --backend claude-code --effort medium --sides all --personality 0=hannibal 1=scipio
   ```
4. Włącz bitwę i oglądaj.

## 6. Gdzie co jest

| Plik albo folder | Co w nim jest |
|---|---|
| `strategy.md` | Standardowa taktyka, której trzyma się każdy wódz. Możesz ją edytować. |
| `rules.md` | Twarde fakty o grze. |
| `personalities.md` | Typy armii, przypisane do nich państwa i dowódcy. Tu dopiszesz własnego dowódcę. |
| `battles.md` | Kompendium bitew starożytności. |
| `docs\commanders.pl.html` | Katalog dowódców, typów armii i bitew do czytania. |
| `armies\` | Karty armii z doboru. |
| `logs\` | Zapis każdej bitwy: co wódz widział i co postanowił. |

Wszystkie pliki `.md` serwer czyta przed każdą bitwą, więc restart nie jest potrzebny. Po edycji
`personalities.md` albo `battles.md` sprawdź, czy wszystko się zgadza, i odśwież katalog:

```powershell
.venv\Scripts\python -m rome_ai.personalities check
.venv\Scripts\python -m rome_ai.personalities docs
```

## 7. Gdy coś nie działa

| Objaw | Co zrobić |
|---|---|
| W oknie serwera brak linii `hello: rome-remastered v1` | Sprawdź, czy `dinput8.dll` leży w folderze gry, obok `Total War ROME REMASTERED.exe`. |
| `general failed: You've hit your session limit` | Skończył się limit Claude. Armią dowodzi AI gry; wódz wróci sam, gdy limit się odnowi. |
| Oddziały stoją bez rozkazów | Wklej log z okna serwera. |
| Chcesz wrócić do oryginalnego moda | Skopiuj `C:\rome-battle-ai\hook-windows\dinput8.dll` (wersja v0.3) do folderu gry i uruchamiaj serwer bez `--sides` i `--personality`. |

Testy bez gry (nie zużywają limitu):

```powershell
.venv\Scripts\python -m rome_ai.personalities check
.venv\Scripts\python -m rome_ai.recruit --check
```
