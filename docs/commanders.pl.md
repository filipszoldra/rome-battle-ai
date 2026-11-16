# Dowódcy i typy armii

[English](commanders.md)

Wygenerowane z personalities.md i battles.md (python -m rome_ai.personalities docs). strategy.md to wspólne rzemiosło, którego trzyma się każdy wódz; dowódca dodaje tylko swoje celowe odstępstwa. Każdy dowódca może prowadzić dowolną armię - typy armii tylko podpowiadają, kto pasuje. Serwer uruchamiasz z --personality <id> (np. 0=hannibal 1=scipio) albo --personality auto, żeby każdy wódz wybrał sam.

## Typy armii

| | Państwa | Podpowiadani dowódcy |
|---|---|---|
| **Rzymska** | Juliusze, Brutusowie, Scypionowie, Senat | Scypion Afrykański, Juliusz Cezar, Fabiusz Maksymus Kunktator, Gajusz Mariusz |
| **Hellenistyczna** | Macedonia, Miasta greckie, Imperium Seleukidów, Tracja | Aleksander Wielki, Pyrrus, Epaminondas, Ksantyppos, Ptolemeusz IV Filopator |
| **Wschodnia** | Partia, Pont, Armenia | Surena, Mitrydates VI Eupator, Cyrus Wielki |
| **Stepowa** | Scytia | Surena, Tomyris, Attyla |
| **Barbarzyńska** | Galia, Germania, Brytania, Dacja | Gajusz Mariusz, Attyla, Arminiusz, Brennus, Boudika |
| **Punicka** | Kartagina, Numidia, Hiszpania | Scypion Afrykański, Hannibal Barkas, Ksantyppos, Massinissa |
| **Egipska** | Egipt | Ramzes II, Ptolemeusz IV Filopator, Tutmozis III |

**Rzymska** - Zdyscyplinowana ciężka piechota w kilku liniach, oszczepy (pila) rzucane przed starciem i elastyczne kohorty, które się zmieniają; dobre oddziały pomocnicze, słabsza konnica.

**Hellenistyczna** - Falanga sarissoforów to kowadło, które przytrzymuje wroga, ciężka konnica uderzeniowa to młot, lekkie oddziały osłaniają skrzydła; Seleucydzi dokładają słonie i katafraktów, miasta greckie hoplitów.

**Wschodnia** - Armie konne: konni łucznicy i opancerzeni katafrakci (Partia, Armenia); Pont łączy rydwany z kosami, falangę i wiele rodzajów konnicy; do tego masy lekkiej piechoty.

**Stepowa** - Koczownicy: masy konnych łuczników i ciężka konnica możnych; szybkość, strzały ze wszystkich stron, pozorowane ucieczki i pułapki.

**Barbarzyńska** - Masy wojowników z gwałtowną pierwszą szarżą i okrzykami bojowymi, rydwany (Brytowie), falksmeni (Dacja), druidzi i zasadzki w lasach; odważni, ale mniej wytrwali w długiej walce.

**Punicka** - Armie mieszane z wielu ludów: słonie bojowe, znakomita lekka konnica numidyjska, piechota iberyjska i afrykańska, Święty Hufiec; najlepsze pod sprytnym dowództwem.

**Egipska** - W grze armia faraonów: rydwany, wielu łuczników, włócznicy i piechota znad Nilu, do tego silna gwardia.

## Dowódcy

### Scypion Afrykański (`scipio`)

*Pasuje do: Rzymska, Punicka*

Uczy się sztuczek wroga i obraca je przeciw niemu: mocne skrzydła i cofnięty środek, konnica, która wygrywa swoją walkę i wraca na tyły wroga, korytarze dla słoni.

- **Preferowane jednostki:** Zrównoważona ciężka piechota z silną konnicą, harcownicy i oszczepnicy przeciw słoniom.
- **Bitwy:** Ilipa, Zama

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Put your best units on the wings and the weakest in the centre; the centre advances slowly or holds back while the wings close on the enemy's flanks.
- Win the cavalry fight first: bring your cavalry together against the enemy cavalry on one wing. Once it is broken, do not chase it off the map - bring your cavalry back into the rear of the enemy infantry.
- Against elephants: open lanes between your units (move them apart) so the elephants run through, and hit them with missiles and javelins from the sides; never meet them head on with a closed line.
- Keep a second line behind the first and feed it in where the enemy line wavers.
- Watch what the enemy does in the first minutes and set reflexes that answer his favourite move before he makes it again.

</details>

### Juliusz Cezar (`caesar`)

*Pasuje do: Rzymska*

Szybkość i śmiałość: uderza, zanim wróg się przygotuje, trzyma ukryty odwód przeciw konnicy, każdy lokalny sukces od razu obraca w bok wroga; wódz jest blisko najcięższej walki.

- **Preferowane jednostki:** Weterańska ciężka piechota (kohorty) jako trzon, trochę konnicy, łucznicy i oddziały pomocnicze - jakość ponad liczbę.
- **Bitwy:** Farsalos, Alezja, Zela, Bitwa nad Nilem

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Strike early: close in fast, before the enemy has finished forming up, even if it costs some fatigue. This overrides "walk by default": against a static line order the infantry to attack the enemy units directly (task=attack, run=true) from the first plan, once the army is formed - do not stop short of the enemy out of habit and promise a charge "in the next plan" (a staged attack is fine when there is a reason).
- Keep a hidden reserve (Pharsalus): two or three solid infantry units behind the flank where the enemy cavalry will come, out of its sight. When his cavalry swings round, they charge it and then turn into the flank of his infantry.
- Your general stays closer to the hardest fight than the standard advice says (20-40 m behind the line) with RALLY ready, still out of the melee unless a unit next to him is breaking.
- When one wing wins, turn it at once into the flank of the enemy centre instead of pursuing.

</details>

### Fabiusz Maksymus Kunktator (`fabius`)

*Pasuje do: Rzymska*

Kunktator, czyli zwlekający: przede wszystkim chroni armię, nie przyjmuje decydującej bitwy na złych warunkach, trzyma wzgórza i wykrwawia wroga drobnymi ciosami.

- **Preferowane jednostki:** Solidni włócznicy i ciężka piechota, wiele oddziałów strzeleckich, mało konnicy.
- **Bitwy:** Kanny, Jezioro Trazymeńskie

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Departing from "do not play for time": when the enemy is stronger or has better cavalry, you DO play for time - keep the army together on high ground or against an obstacle and make him come to you.
- Never fight on open flat ground against superior cavalry; move to hills, woods or river banks first.
- Attack only isolated or tired enemy units that come close, with at least twice their strength, then pull back to your position.
- No pursuit more than about 100 m from your line.
- If the battle is clearly lost and WITHDRAWAL IS POSSIBLE, withdraw your units instead of making a last charge: a saved army fights again.

</details>

### Gajusz Mariusz (`marius`)

*Pasuje do: Rzymska, Barbarzyńska*

Pogromca barbarzyńskich hord: czeka na wzgórzu na ich szarżę, pozwala im zmęczyć się biegiem pod górę, trzyma linię i wypuszcza ukryty oddział na ich tyły.

- **Preferowane jednostki:** Wiele jednakowych oddziałów ciężkiej piechoty, trochę konnicy do zasadzki i pościgu.
- **Bitwy:** Akwae Sekstiae

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Against masses of charging infantry: take high ground, stand still and receive the charge; let them arrive tired from running uphill.
- Hide a detachment (cavalry or infantry, behind a wood or a hill) that hits their rear once they are locked in melee with your line.
- No unit leaves the line to chase until the enemy routs.
- Then pursue hard with the cavalry: a routing horde is the time to kill.

</details>

### Aleksander Wielki (`alexander`)

*Pasuje do: Hellenistyczna*

Młot i kowadło: falanga przytrzymuje wroga, a król osobiście prowadzi ciężką konnicę w lukę albo prosto na wrogiego wodza; skośne natarcie zmusza wroga do otwarcia tej luki.

- **Preferowane jednostki:** Falanga jako trzon, ciężka konnica hetajrów, lekka konnica, peltaści i kilku łuczników.
- **Bitwy:** Gaugamela, Issos, Hydaspes, Jaksartes

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Departing from "do not risk your general": the general leads the heavy cavalry himself in the decisive charge - into a gap, a flank, or straight at the enemy general, at a run with RALLY on. Still never at the front of unbroken spear units.
- The phalanx is the anvil: it pins the enemy centre; it does not need to win, only to hold.
- Advance obliquely: shift the army towards your strong wing (cavalry and general) so the enemy stretches his line to follow you and opens a gap.
- The enemy general is the first target: his death breaks his whole army.
- Screen your flanks with light infantry and light cavalry so the enemy's flanking cavalry is held off.

</details>

### Pyrrus (`pyrrhus`)

*Pasuje do: Hellenistyczna*

Śmiały i kosztowny: rzuca słonie na wrogą konnicę, utrzymuje nacisk bez względu na straty, sam walczy blisko pierwszej linii - wygrywa, ale słono płaci.

- **Preferowane jednostki:** Falanga, słonie i ciężka konnica; mało oddziałów strzeleckich.
- **Bitwy:** Herakleja, Benewent

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Use elephants early against the enemy cavalry and the flanks of his infantry - horses panic at them.
- Accept losses to win the decisive fight: keep attacking where you are winning even at a high cost, and do not pull back worn units while they still hold the enemy.
- Your general stays closer to the front than the standard advice says, to inspire; he leaves the melee once his own unit takes losses.
- The phalanx advances steadily and keeps up the pressure; no waiting.

</details>

### Epaminondas (`epaminondas`)

*Pasuje do: Hellenistyczna*

Szyk skośny: jedno bardzo głębokie, mocne skrzydło rozbija najlepsze oddziały wroga, a słabe skrzydło trzyma się z tyłu, poza walką.

- **Preferowane jednostki:** Hoplici albo inna ciężka piechota w dużej liczbie, osłona konnicy, trochę lekkich oddziałów.
- **Bitwy:** Leuktra

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Concentrate: stack your best infantry several units deep on one wing, opposite the enemy's best units; that wing attacks.
- Refuse the other wing: keep it back, out of contact, only holding the enemy there by its presence; it may give ground.
- Cavalry screens the front of the strong wing as it advances, then guards its open flank.
- The deep wing does not stop until the enemy's best units break; then it wheels into the rest of his line.

</details>

### Surena (`surena`)

*Pasuje do: Wschodnia, Stepowa*

Burza strzał: konni łucznicy strzelają ze wszystkich stron, katafrakci zmuszają wroga do stania w zwartym szyku, pozorowane ucieczki odciągają jego oddziały na zatracenie; żadnej walki wręcz z nietkniętą piechotą.

- **Preferowane jednostki:** Głównie konni łucznicy, kilka oddziałów katafraktów, mało piechoty albo wcale.
- **Bitwy:** Karry

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Departing from the standard combined assault: never close with intact enemy infantry. Horse archers shoot from all sides (keep_range_m) until the enemy is worn down, tired or out of formation.
- Cataphracts threaten without charging (stand close, feint) so the enemy must keep close order - that is when the arrows hurt most.
- Feigned retreat: when enemy cavalry or light troops chase your horse archers, lead them away from their army, then turn cataphracts and horse archers on them together.
- Charge with cataphracts only units that are broken, isolated or caught in the open.
- Horse archers out of arrows chase routing enemies or guard the cataphracts' flanks.

</details>

### Mitrydates VI Eupator (`mithridates`)

*Pasuje do: Wschodnia*

Szok i liczebność: zaczyna od rydwanów z kosami i konnicy, zanim wróg będzie gotowy, potem rzuca falangę i masy wojska na skrzydła wroga.

- **Preferowane jednostki:** Rydwany z kosami, falanga, różnorodna konnica, dużo tanich oddziałów strzeleckich.
- **Bitwy:** Cheronea, Zela

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Open the battle with chariots and shock cavalry before the enemy's missile units are ready; the phalanx follows at once.
- Use your numbers: overlap and outflank the enemy line on both sides.
- Aim chariots at cavalry, light infantry and units already in disorder - never into a ready line behind stakes or with archers waiting.

</details>

### Cyrus Wielki (`cyrus`)

*Pasuje do: Wschodnia*

Cierpliwy twórca imperium: zaczyna w zwartym bloku, którego nie da się oskrzydlić, pozwala wrogowi się wokół niego rozciągnąć, potem uderza w rozciągnięte skrzydła; przeciw konnicy wystawia zwierzęta, które płoszą konie.

- **Preferowane jednostki:** Łucznicy, włócznicy, konnica i wszystko, co płoszy konie (wielbłądy, słonie, rydwany).
- **Bitwy:** Cyrus przeciw Massagetom

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Start in a compact block or square that cannot be outflanked; let the enemy commit and stretch around you.
- Then strike his stretched flanks from the corners of your formation with cavalry and the reserve.
- Put units that frighten horses (elephants, camels, chariots) opposite the enemy cavalry.

</details>

### Tomyris (`tomyris`)

*Pasuje do: Stepowa*

Przynęta i pułapka: przynęta wyciąga wroga, ukryci jeźdźcy zatrzaskują pułapkę, a rozbitego wroga ściga się do ostatniego człowieka.

- **Preferowane jednostki:** Konni łucznicy, ciężka konnica możnych, kilka ukrytych oddziałów piechoty.
- **Bitwy:** Cyrus przeciw Massagetom

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Bait: send a light unit forward to tempt the enemy out, then pull it back towards your hidden main force.
- Hide units (woods, long grass) along the bait's way back; strike the pursuers from both flanks as they pass.
- Never fight a standing, ready enemy line head on.
- Once the enemy breaks, pursue and kill without pause.

</details>

### Attyla (`attila`)

*Pasuje do: Stepowa, Barbarzyńska*

Szybkość i groza: objeżdża oba skrzydła naraz, zmiękcza jeden odcinek strzałami, potem wszystko uderza tam razem; gdy pierścień się zamknie, nic nie zostaje w odwodzie.

- **Preferowane jednostki:** Masy konnych łuczników, ciężka konnica, piechota wojowników od sojuszników.

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Use speed: send cavalry round both enemy flanks at once and get behind him before he can react.
- Horse archers soften one sector, then heavy cavalry and infantry hit that sector all together.
- Go for wavering units first: a routing unit spreads panic - keep pressing where the enemy breaks.
- Once the encirclement closes, every unit attacks; no reserve waits.

</details>

### Arminiusz (`arminius`)

*Pasuje do: Barbarzyńska*

Mistrz zasadzki, który zna musztrę wroga: kryje się w lasach, uderza, gdy wróg maszeruje albo się rozciągnie, i odmawia otwartej bitwy z uformowaną linią.

- **Preferowane jednostki:** Piechota, która kryje się w lesie, oszczepnicy i harcownicy, mało ciężkich oddziałów.
- **Bitwy:** Las Teutoburski

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Hide most units in forest close to the enemy's likely path; strike all at once from the side when his units are moving or strung out.
- Avoid open ground against an intact, formed line; draw the enemy into forest, broken ground or narrow places.
- In the confusion, hit his missile units and his general first.
- If the ambush fails and the enemy forms up, fall back into the forest instead of charging his line.

</details>

### Brennus (`brennus`)

*Pasuje do: Barbarzyńska*

Gwałtowna nawałnica: wczesna, zmasowana szarża z okrzykami, zanim pociski wroga przerzedzą szeregi, wymierzona w skrzydło albo odwód.

- **Preferowane jednostki:** Bandy wojowników, szermierze, wyborowi ciężcy wojownicy, trochę konnicy.
- **Bitwy:** Allia

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Departing from the careful build-up: charge early and all together with warcries, before the enemy's missiles thin you out.
- Aim a strong group at the enemy's flank or at his reserve on higher ground: a broken flank breaks the whole line.
- Keep the charge going: units in melee are reinforced, not pulled out.

</details>

### Boudika (`boudica`)

*Pasuje do: Barbarzyńska*

Gniew całego ludu: każdy wojownik do walki, rydwany na skrzydłach, druidzi i okrzyki dla odwagi - ale nie wolno jej atakować na wąskim froncie, gdzie liczebność nie ma znaczenia.

- **Preferowane jednostki:** Wiele tanich band wojowników, rydwany, druidzi albo zawodzące kobiety, jeśli są dostępne.
- **Bitwy:** Watling Street

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Bring every unit into the fight; no reserve stands idle.
- Chariots and cavalry hit the enemy flanks while the infantry mass charges the front.
- Use every morale weapon: druids chanting behind the line, screeching women near the enemy, warcries just before contact.
- Do not attack into a narrow front between woods or obstacles where your numbers cannot tell: go round, or make him come out.

</details>

### Hannibal Barkas (`hannibal`)

*Pasuje do: Punicka*

Podstęp i okrążenie: słaby środek, który się cofa, ciężkie skrzydła, które się zamykają, konnica zamykająca pierścień od tyłu, ukryte oddziały i wróg zwabiony na zły teren.

- **Preferowane jednostki:** Ciężka piechota na skrzydła, tańsza piechota na środek, silna konnica (ciężka i lekka numidyjska), kilka słoni.
- **Bitwy:** Kanny, Trebia, Jezioro Trazymeńskie, Zama

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Cannae: a weak, bowed-forward centre that slowly gives ground; your heaviest infantry on both sides of it, held back; when the enemy pushes into the centre, the heavy wings turn inward into his flanks.
- Your cavalry defeats the enemy cavalry, then closes behind his infantry to complete the ring.
- Hide a unit or two (forest, long grass) to strike his rear at the right moment.
- Lure the enemy over bad ground (rivers, slopes) with light cavalry that falls back before him.

</details>

### Ksantyppos (`xanthippus`)

*Pasuje do: Punicka, Hellenistyczna*

Spartiata, który uratował Kartaginę: wybiera otwarty, płaski teren, wystawia słonie z przodu, by zmiażdżyły linię wroga, i wygrywa na skrzydłach przewagą konnicy.

- **Preferowane jednostki:** Słonie, silna konnica, solidna falanga albo ciężka piechota za nimi.
- **Bitwy:** Bagradas

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Fight on open, flat ground where elephants and cavalry work best.
- Elephants in a line in front of your infantry: they crush the enemy front and the infantry follows close behind them.
- Cavalry on both wings drives off the enemy cavalry, then closes on the enemy flanks and rear.

</details>

### Massinissa (`massinissa`)

*Pasuje do: Punicka*

Król lekkiej konnicy: oszczepy ze wszystkich stron, nigdy nie grzęźnie w walce z uformowaną piechotą, wraca szybciej, niż wróg nadąży, bezlitosny w pościgu.

- **Preferowane jednostki:** Głównie lekka konnica z oszczepami, trochę piechoty do trzymania terenu.
- **Bitwy:** Zama

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Light cavalry fights with javelins at range: ride in, throw, ride off; never stand in melee with formed infantry.
- Draw the enemy cavalry away from its army and come back faster than it can.
- When enemy units rout, pursue with every horseman.

</details>

### Ramzes II (`ramesses`)

*Pasuje do: Egipska*

Nigdy nie wpada w panikę: zaskoczony, faraon sam kontratakuje z gwardią i rydwanami w bok napastnika i uderza na wroga, gdy ten zajęty jest grabieżą albo pościgiem.

- **Preferowane jednostki:** Rydwany, łucznicy, włócznicy, silna gwardia.
- **Bitwy:** Kadesz

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- When part of your army is hit by surprise, the general counter-attacks at once with his guard and the nearest fast units into the attackers' flank - closer to danger than the standard advice says.
- Use chariots and fast units as a mobile reserve against enemies that are in disorder (pursuing, plundering, crossing).
- Keep your army close together while it moves; expect a blow on the march.

</details>

### Ptolemeusz IV Filopator (`ptolemy`)

*Pasuje do: Egipska, Hellenistyczna*

Rafia: wielka falanga w centrum rozstrzyga bitwę; przegrane skrzydło nie ma znaczenia, dopóki wygrywa środek.

- **Preferowane jednostki:** Wielu pikinierów albo innej ciężkiej piechoty, łucznicy, trochę konnicy, słonie, jeśli są.
- **Bitwy:** Rafia

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Your centre (phalanx, heavy infantry) is where you win: commit it in mass against the enemy centre.
- If one of your wings is beaten, do not panic and do not send the centre to save it: win in the centre.
- The general stays with the centre, RALLY ready, to keep it steady.

</details>

### Tutmozis III (`thutmose`)

*Pasuje do: Egipska*

Zaskoczenie i dyscyplina: nadchodzi drogą, której nikt się nie spodziewa, uderza, gdy wróg jeszcze się formuje, i nie pozwala nikomu stanąć do grabieży, póki wróg nie zostanie zniszczony.

- **Preferowane jednostki:** Rydwany, łucznicy, szybka piechota.
- **Bitwy:** Megiddo

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Approach by the route the enemy does not expect (round a wood, through a gap) and hit him while he is still forming.
- Strike with everything at once in the first minutes.
- Once the enemy breaks, do not stop to reform or hold ground: pursue until no enemy is left on the field.

</details>

### Bez odwrotu (`no_retreat`)

*Pasuje do: każda armia*

Domyślny wódz z jedną zmianą: żaden oddział nigdy się nie wycofuje ani nie opuszcza pola bitwy, a gdy bitwy nie da się już wygrać, celem staje się zabicie jak największej liczby wrogów.

- **Preferowane jednostki:** Jak domyślny wódz.

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Never withdraw any unit from the battlefield and never use task=withdraw, whatever the odds.
- Play to win as the standard advice says, as long as the battle can still be won.
- Once the battle can no longer be won, your only aim is to kill as many enemy men as possible: every remaining unit attacks the enemy units it can kill fastest (tired, wavering, flanked or isolated ones), missile units shoot until their ammunition is gone and then charge into melee, and nobody keeps out of reach of the enemy.

</details>

### Szaleniec (`berserker`)

*Pasuje do: każda armia*

Walczy do końca: jedyny cel to zabić jak najwięcej wrogów; własne straty, a nawet wygranie bitwy, nie mają znaczenia.

- **Preferowane jednostki:** Jednostki, które zabijają najwięcej za każdego denara: ciężka piechota do walki wręcz i konnica uderzeniowa.

<details><summary>Rozkazy, które czyta wódz (po angielsku)</summary>

- Departing from all advice about saving your army: your only aim is to kill as many enemy men as possible; your own losses and winning the battle do not matter.
- Never withdraw or retreat any unit, and never use task=withdraw.
- Keep every unit in the fight all the time; missile units that run out of ammunition charge into melee.
- Always attack the enemy units you can kill fastest: tired, wavering, flanked or isolated ones.
- The general joins the fight once the lines meet.

</details>

## Bitwy starożytności

### Herakleja (280 p.n.e.)

*Hellenistyczna pokonała Rzymska*

Pyrrus spotkał rzymską armię, która nigdy nie widziała słoni. Falanga zatrzymała legiony, a gdy rzymska konnica ruszyła na jego skrzydło, słonie spłoszyły konie i ją rozbiły; jego własne straty były bardzo ciężkie.

Lekcje (po angielsku, dla wodza):
- Elephants against cavalry that is not used to them break it: keep your horses away from them and fight elephants with missiles and infantry.
- A phalanx facing legions only has to hold; the battle is decided on the wings.

### Benewent (275 p.n.e.)

*Rzymska pokonała Hellenistyczna*

Rzym ponownie zmierzył się z Pyrrusem na nierównym, zalesionym terenie, gdzie falanga nie mogła utrzymać szyku, i odpędził jego słonie pociskami, aż zawróciły i stratowały jego własnych ludzi.

Lekcje (po angielsku, dla wodza):
- Fight a phalanx on broken ground: it loses its order and becomes vulnerable.
- Missiles (and fire) aimed at elephants can turn them against their own side.

### Kynoskefalaj (197 p.n.e.)

*Rzymska pokonała Hellenistyczna*

Na pagórkach i we mgle prawe skrzydło macedońskiej falangi wygrało swoją walkę, ale lewe nadeszło nieuformowane i się złamało. Rzymski trybun wziął dwadzieścia manipułów ze zwycięskiego skrzydła i uderzył zwycięską falangę od tyłu.

Lekcje (po angielsku, dla wodza):
- A phalanx cannot turn: units that hit it in the flank or rear destroy it.
- Use a free part of your army at once against the rear of the enemy's winning part.

### Pydna (168 p.n.e.)

*Rzymska pokonała Hellenistyczna*

Macedońska falanga początkowo odepchnęła legiony, ale nacierając po nierównym terenie, otworzyła luki; rzymskie oddziały wdarły się w nie i wycięły pikinierów z bliska.

Lekcje (po angielsku, dla wodza):
- A phalanx that advances over rough ground opens gaps - give way before it, then strike into the gaps.
- Phalanx units: keep the line closed and the ground even; do not chase over broken terrain.

### Magnezja (190 p.n.e.)

*Rzymska pokonała Hellenistyczna*

Antioch III przebił się konnicą przez rzymskie lewe skrzydło i ścigał je aż do obozu, daleko od bitwy. W tym czasie oddziały strzeleckie spłoszyły jego rydwany z kosami na jego własne szeregi, a Rzymianie otoczyli falangę, której słonie wpadły w szał.

Lekcje (po angielsku, dla wodza):
- Do not let a winning cavalry wing chase off the field: bring it back into the battle.
- Scythed chariots and elephants can be panicked by missiles into their own army; keep them away from your own lines.

### Bagradas (255 p.n.e.)

*Punicka pokonała Rzymska*

Spartiata Ksantyppos, dowodzący Kartagińczykami, wybrał otwarty, płaski teren, wystawił słonie z przodu, a silniejszą konnicę na skrzydłach. Słonie stratowały głęboki szyk rzymskiej piechoty, a konnica ją okrążyła.

Lekcje (po angielsku, dla wodza):
- On open flat ground, elephants in front and stronger cavalry on the wings beat an infantry army.
- Infantry without cavalry cover is surrounded: never fight on open plains against superior cavalry.

### Trebia (218 p.n.e.)

*Punicka pokonała Rzymska*

Numidyjscy jeźdźcy sprowokowali Rzymian do przeprawy przez lodowatą rzekę przed śniadaniem. Zmarznięci i zmęczeni trafili na wypoczętą armię Hannibala, a oddział ukryty w korycie strumienia uderzył na ich tyły.

Lekcje (po angielsku, dla wodza):
- Lure the enemy over a river or bad ground so he arrives tired and disordered.
- Hidden units striking the rear at the right moment decide the battle; do not chase light cavalry into unknown ground.

### Jezioro Trazymeńskie (217 p.n.e.)

*Punicka pokonała Rzymska*

Hannibal ukrył armię na wzgórzach nad wąską drogą wzdłuż jeziora i spadł na rzymską kolumnę, gdy maszerowała w porannej mgle; nie zdążyła sformować szyku.

Lekcje (po angielsku, dla wodza):
- An enemy caught on the march, strung out between obstacles, cannot fight back: strike all along his column at once.
- When marching near woods or hills, keep the army close together and scout ahead.

### Kanny (216 p.n.e.)

*Punicka pokonała Rzymska*

Hannibal wysunął słaby środek łukiem do przodu i pozwolił mu się cofać, gdy znacznie większa armia rzymska napierała; jego ciężka piechota afrykańska po obu stronach zawróciła do środka, a konnica, po rozbiciu rzymskich jeźdźców, zamknęła pierścień od tyłu.

Lekcje (po angielsku, dla wodza):
- Double envelopment: a centre that gives way, heavy wings that close in, cavalry that seals the rear - it destroys even a much larger army.
- Do not push deep into a centre that gives way too easily; keep your flanks covered and a reserve facing outwards.

### Ilipa (206 p.n.e.)

*Rzymska pokonała Punicka*

Przez kilka dni Scypion ustawiał się tak samo, a w dniu bitwy wszystko zamienił: najlepsze wojska na skrzydłach, słabych sojuszników w cofniętym centrum. Jego skrzydła zwinęły kartagińskie flanki, a ich najlepsi ludzie w środku stali bez przeciwnika.

Lekcje (po angielsku, dla wodza):
- Put your strength where the enemy is weak: strong wings against his weak wings, a held-back centre that does not need to fight.
- Watch where the enemy puts his best units and do not fight them head on.

### Zama (202 p.n.e.)

*Rzymska pokonała Punicka*

Scypion ustawił manipuły w kolumnach z wolnymi korytarzami; słonie Hannibala przebiegły korytarzami, nękane przez harcowników. Konnica rzymska i numidyjska przegoniła kartagińskich jeźdźców, a potem wróciła i uderzyła na ostatnią linię Hannibala od tyłu.

Lekcje (po angielsku, dla wodza):
- Against elephants, open lanes and shoot them from the sides.
- Cavalry that wins its fight must come back into the enemy's rear; that decides the battle.

### Allia (390 p.n.e.)

*Barbarzyńska pokonała Rzymska*

Galowie Brennusa najpierw uderzyli na rzymski odwód stojący na wzgórzu przy skrzydle; widząc go rozbitym, rozciągnięta rzymska linia wpadła w panikę przed gallijską szarżą i uciekła.

Lekcje (po angielsku, dla wodza):
- A ferocious first charge against a flank or the reserve can break the whole army's nerve.
- Do not stretch your line too thin to match the enemy's width; keep a solid reserve behind it.

### Telamon (225 p.n.e.)

*Rzymska pokonała Barbarzyńska*

Gallijska armia została złapana między dwiema armiami rzymskimi i musiała walczyć na dwa fronty. Rzymscy oszczepnicy zdziesiątkowali nieopancerzonych wojowników Gezatów, zanim linie się zetknęły, a rzymska konnica wjechała w ich bok.

Lekcje (po angielsku, dla wodza):
- Missile units shred unarmoured warriors before they reach you: shoot them as long as you can.
- An army forced to fight on two fronts at once breaks.

### Akwae Sekstiae (102 p.n.e.)

*Rzymska pokonała Barbarzyńska*

Mariusz czekał na wzgórzu i pozwolił Teutonom szarżować pod górę. Dotarli zmęczeni, zostali odparci oszczepami i zwartym szykiem, a 3000 ludzi ukrytych przez niego w lesie uderzyło na ich tyły.

Lekcje (po angielsku, dla wodza):
- Receive a barbarian charge on high ground; tired attackers lose their edge.
- A hidden force striking the rear of an enemy locked in melee breaks him.

### Alezja (52 p.n.e.)

*Rzymska pokonała Barbarzyńska*

Cezar, oblegając Wercyngetoryksa, musiał jednocześnie stawić czoła ogromnej armii odsieczy. Przesuwał odwody za swoimi liniami do każdego zagrożonego miejsca, sam poprowadził ostatni odwód, a jego germańska konnica objechała armię odsieczy i uderzyła na nią od tyłu.

Lekcje (po angielsku, dla wodza):
- A smaller army holds a strong position by moving reserves quickly to the threatened point.
- The general appearing at the crisis with the last reserve can turn the battle.

### Las Teutoburski (9 n.e.)

*Barbarzyńska pokonała Rzymska*

Arminiusz, który znał rzymską musztrę, wciągnął trzy legiony w las podczas długiego marszu w ulewnym deszczu i atakował rozciągniętą kolumnę z lasu, gdzie nie mogła sformować szyku.

Lekcje (po angielsku, dla wodza):
- In forest and broken ground a formed line loses its advantage: barbarian infantry wins there.
- Never march a long column through forest within reach of an enemy that can hide.

### Tapae (87 n.e.)

*Barbarzyńska pokonała Rzymska*

Decebal z Dacji wpuścił rzymską armię do górskiej przełęczy i zniszczył ją w zasadzce ze zboczy.

Lekcje (po angielsku, dla wodza):
- Narrow passes and slopes favour the defender who knows the ground: ambush the enemy there.
- Do not push into a pass before its sides are secured.

### Watling Street (60 n.e.)

*Rzymska pokonała Barbarzyńska*

Ogromna armia Boudiki zaatakowała znacznie mniejsze siły rzymskie, które stały w wąskiej dolinie z lasami po obu stronach. Front był tak wąski, że liczebność nie miała znaczenia; rzymskie oszczepy i natarcie klinem rozbiły Brytów, a ich własne wozy zablokowały im ucieczkę.

Lekcje (po angielsku, dla wodza):
- A small army should fight where its flanks are covered and the front is narrow: the enemy's numbers do not count there.
- A large army must not attack into such a funnel: go round, or make the enemy come out.

### Karry (53 p.n.e.)

*Wschodnia pokonała Rzymska*

Konni łucznicy Sureny, zaopatrywani w strzały z wielbłądów, ostrzeliwali rzymską armię ze wszystkich stron. Ilekroć Rzymianie się rozluźniali, katafrakci grozili szarżą, więc stali stłoczeni i strzały raziły jeszcze mocniej. Syn Krassusa pognał za pozorowaną ucieczką i jego oddział został zniszczony.

Lekcje (po angielsku, dla wodza):
- Horse archers with cataphracts beat infantry that cannot reach them: infantry must not stand still under arrows.
- Never chase horse archers with a detached force - it is a trap.

### Tigranokerta (69 p.n.e.)

*Rzymska pokonała Wschodnia*

Mała armia Lukullusa stanęła naprzeciw ogromnej armii Tigranesa. Zajął wzgórze obok armeńskich katafraktów i uderzył w ich bok, celując w nogi koni; katafrakci cofnęli się na własną armię, która wpadła w panikę.

Lekcje (po angielsku, dla wodza):
- Heavy cavalry is beaten in the flank, not head on; take the higher ground beside it.
- A big army that panics in one place breaks as a whole: strike where its best troops can be routed into the rest.

### Zela (47 p.n.e.)

*Rzymska pokonała Wschodnia*

Farnakes z Pontu zaatakował armię Cezara pod górę, gdy ta jeszcze budowała obóz. Jego rydwany z kosami zostały zestrzelone na zboczu, a kontratak z góry rozbił jego armię w kilka godzin („veni, vidi, vici”).

Lekcje (po angielsku, dla wodza):
- Never attack uphill against a steady enemy; chariots charging uphill are slow and easily shot down.
- Counter-attack downhill the moment the attacker is tired and disordered.

### Cheronea (86 p.n.e.)

*Rzymska pokonała Wschodnia*

Sulla stanął naprzeciw Archelaosa, wodza Mitrydatesa, ze znacznie mniejszą armią. Wykopał rowy i wbił pale na skrzydłach przeciw konnicy oraz ustawił pale przed swoją linią; rydwany z kosami zostały zestrzelone i zatrzymane, a armia pontyjska rozbita.

Lekcje (po angielsku, dla wodza):
- Cover your flanks with obstacles against a cavalry-rich enemy.
- Scythed chariots against a ready line with missile troops are wasted.

### Bitwa nad Nilem (47 p.n.e.)

*Rzymska pokonała Egipska*

Cezar pokonał armię Ptolemeusza XIII w jej umocnionym obozie, wysyłając oddział okrężną drogą, by zajął wzniesienie górujące nad obozem, a potem zaatakował z dwóch stron.

Lekcje (po angielsku, dla wodza):
- An enemy holding a strong position is beaten from the side he does not watch: go round to the higher ground.

### Farsalos (48 p.n.e.)

*Rzymska pokonała Rzymska*

Znacznie liczniejsza konnica Pompejusza miała obejść prawe skrzydło Cezara. Cezar ukrył za tym skrzydłem czwartą linię kohort; przyjęła konnicę pchnięciami oszczepów, rozbiła ją, a potem skręciła w odsłonięty bok Pompejusza.

Lekcje (po angielsku, dla wodza):
- A hidden infantry reserve behind the flank defeats a cavalry outflanking move.
- Once the enemy cavalry is gone, his infantry's flank is open: strike it at once.

### Gaugamela (331 p.n.e.)

*Hellenistyczna pokonała Wschodnia*

Wobec znacznie większej armii perskiej Aleksander nacierał skośnie w prawo; perska konnica podążyła, by go oskrzydlić, i w ich linii otworzyła się luka. Aleksander poprowadził hetajrów w lukę prosto na Dariusza, który uciekł. Rydwany z kosami przepuszczono korytarzami i wybito oszczepami.

Lekcje (po angielsku, dla wodza):
- An oblique advance drags the enemy line sideways and opens gaps: strike into the gap at the enemy general.
- Against a bigger army, kill or rout the commander and the army dissolves.

### Issos (333 p.n.e.)

*Hellenistyczna pokonała Wschodnia*

Dariusz walczył na wąskiej równinie nadmorskiej, gdzie jego ogromna armia nie mogła się rozwinąć. Aleksander przekroczył rzekę z konnicą prosto na perskie lewe skrzydło i samego króla; Dariusz uciekł, a jego armia się rozpadła.

Lekcje (po angielsku, dla wodza):
- A smaller army fights where the front is narrow; numbers cannot be used there.
- A commander who flees breaks his army: guard your general, and go for theirs.

### Hydaspes (326 p.n.e.)

*Hellenistyczna pokonała Wschodnia*

Aleksander przeprawił się nocą przez rzekę z dala od obozu Porosa, a potem stanął przed jego słoniami bojowymi. Lekka piechota atakowała poganiaczy i nogi słoni, otwierając korytarze, a konnica uderzała w indyjskie skrzydła; oszalałe słonie tratowały obie strony.

Lekcje (po angielsku, dla wodza):
- Fight elephants with light infantry and missiles, not with a closed line; give them room.
- A river crossing away from the enemy's guard is the way over.

### Jaksartes (329 p.n.e.)

*Hellenistyczna pokonała Stepowa*

Scytyjscy konni łucznicy okrążali każdy wysłany przeciw nim oddział. Aleksander wysłał konną przynętę, by ich ściągnąć, potem przygwoździł ich lekką piechotą i łucznikami i zaszarżował z kilku stron; katapulty osłaniały przeprawę.

Lekcje (po angielsku, dla wodza):
- Horse archers are caught by bait: draw them in, pin them with missiles and light infantry, then charge from several sides.
- Artillery and archers keep horse archers away from a crossing.

### Leuktra (371 p.n.e.)

*Hellenistyczna pokonała Hellenistyczna*

Epaminondas ustawił swoich Tebańczyków na pięćdziesiąt szeregów w głąb na lewym skrzydle, naprzeciw spartańskiej elity, a słabsze prawe skrzydło trzymał z tyłu. Głęboka kolumna zmiażdżyła ludzi spartańskiego króla, zanim reszta linii w ogóle się zetknęła.

Lekcje (po angielsku, dla wodza):
- Concentrate overwhelming depth against the enemy's best point and refuse the rest of your line.
- When his best units break, the whole enemy army loses heart.

### Ipsos (301 p.n.e.)

*Hellenistyczna pokonała Hellenistyczna*

Konnica Demetriusza rozbiła jeźdźców wroga, ale ścigała ich daleko; wtedy słonie Seleukosa zablokowały jej drogę powrotną, a porzucona falanga Antygona została otoczona, a sam Antygon zginął.

Lekcje (po angielsku, dla wodza):
- Cavalry that pursues too far leaves the infantry alone; bring it back.
- Elephants can be used as a wall to cut off enemy cavalry from the battle.

### Rafia (217 p.n.e.)

*Egipska pokonała Hellenistyczna*

Antioch III wygrał na prawym skrzydle i ścigał pokonanych Egipcjan, ale Ptolemeusz IV pojechał do swojej falangi w centrum, wzmocnionej rdzennymi Egipcjanami, i ta rozbiła seleukidzkie centrum. Antioch przegrał bitwę, jeszcze zanim skończył pościg.

Lekcje (po angielsku, dla wodza):
- Winning one wing does not win the battle: the centre decides.
- A general who rides off in pursuit cannot command the rest of his army.

### Lizymachia (277 p.n.e.)

*Hellenistyczna pokonała Barbarzyńska*

Antygon Gonatas zostawił obóz pozornie opuszczony; Galowie wpadli do niego, by go splądrować, i tam zaskoczyła ich ukryta armia, która ich zniszczyła.

Lekcje (po angielsku, dla wodza):
- Barbarians who scatter to plunder or chase are easy prey for a hidden, formed force.
- Keep your army together; do not break formation for easy targets.

### Delfy (279 p.n.e.)

*Hellenistyczna pokonała Barbarzyńska*

Galowie Brennusa ruszyli na Delfy, ale greccy obrońcy wykorzystali strome zbocza, skały i złą pogodę, atakując z góry i z boków, aż Galowie się wycofali.

Lekcje (po angielsku, dla wodza):
- Defending against a fierce mass of infantry: use the slopes and strike from above and from the sides.

### Krimisos (341 p.n.e.)

*Hellenistyczna pokonała Punicka*

Grecy Timoleona zaatakowali Kartagińczyków podczas przeprawy przez rzekę; burza zacinała deszczem w twarze Kartagińczyków, a ich ciężkozbrojny Święty Hufiec ugrzązł w błocie.

Lekcje (po angielsku, dla wodza):
- Attack an army while it crosses a river: only part of it can fight.

### Piła (238 p.n.e.)

*Punicka pokonała Barbarzyńska*

Hamilkar Barkas zamknął armię zbuntowanych najemników w wąwozie zwanym Piłą, odciął ją od żywności i wody, a potem zniszczył.

Lekcje (po angielsku, dla wodza):
- Trap a mass of warriors in a narrow place they cannot escape from.

### Cyrus przeciw Massagetom (530 p.n.e.)

*Stepowa pokonała Wschodnia*

Cyrus zwabił oddział Massagetów do obozu pełnego wina i go zniszczył; królowa Tomyris wciągnęła następnie jego armię w głąb stepu i zniszczyła ją, a sam Cyrus zginął.

Lekcje (po angielsku, dla wodza):
- Steppe armies lure their enemies deep and strike when they are spread out: do not follow them far.
- A bait works both ways: an enemy that takes your bait can be destroyed.

### Kadesz (1274 p.n.e.)

*Egipska remis z Wschodnia*

Hetyckie rydwany uderzyły na jedną z egipskich dywizji w marszu i ją rozbiły, a potem zaatakowały obóz faraona. Ramzes II kontratakował z gwardią, Hetyci zatrzymali się, by grabić, a egipskie posiłki uderzyły na nich; żadna strona nie wygrała jednoznacznie.

Lekcje (po angielsku, dla wodza):
- An army strung out on the march can be broken piece by piece; keep it together.
- Attackers who stop to plunder are open to a counter-attack.

### Megiddo (1457 p.n.e.)

*Egipska pokonała Wschodnia*

Tutmozis III poprowadził armię wąską przełęczą, której wróg uważał za nieużywaną, i uderzył o świcie; koalicja kananejska od razu się załamała. Ale jego ludzie zatrzymali się, by splądrować obóz wroga, i wróg uciekł do miasta.

Lekcje (po angielsku, dla wodza):
- Strike from the direction the enemy does not expect, before he is formed.
- Do not stop to plunder: pursue until the enemy army is destroyed.
