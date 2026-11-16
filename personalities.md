# Army types and commanders (personalities)

The server reads this file before every battle (no restart needed). `strategy.md` is the standard craft of Rome:
Total War that every commander follows; a personality only lists where a commander deliberately departs from it
and what he puts first. Every commander can lead any army: `types` only suggest the armies that fit his style.

Format: `### id | English name | Polish name`, then `key: value` lines, then the orders as `- ` lines - only
those go to the model. `python -m rome_ai.personalities docs` builds the catalogue in docs/ from this file and
battles.md; `python -m rome_ai.personalities check` checks both.

## Army types

### roman | Roman | Rzymska
factions: romans_julii, romans_brutii, romans_scipii, romans_senate
summary: Disciplined heavy infantry in several lines, javelins (pila) thrown before contact and flexible cohorts that relieve each other; good auxiliaries, weaker cavalry.
summary_pl: Zdyscyplinowana ciężka piechota w kilku liniach, oszczepy (pila) rzucane przed starciem i elastyczne kohorty, które się zmieniają; dobre oddziały pomocnicze, słabsza konnica.

### hellenistic | Hellenistic | Hellenistyczna
factions: macedon, greek_cities, seleucid, thrace
summary: The pike phalanx is the anvil that pins the enemy, heavy shock cavalry is the hammer, light troops screen the flanks; the Seleucids add elephants and cataphracts, the Greek cities hoplites.
summary_pl: Falanga sarissoforów to kowadło, które przytrzymuje wroga, ciężka konnica uderzeniowa to młot, lekkie oddziały osłaniają skrzydła; Seleucydzi dokładają słonie i katafraktów, miasta greckie hoplitów.

### eastern | Eastern | Wschodnia
factions: parthia, pontus, armenia
summary: Cavalry armies: horse archers and armoured cataphracts (Parthia, Armenia); Pontus mixes scythed chariots, a pike phalanx and many kinds of cavalry; masses of light infantry.
summary_pl: Armie konne: konni łucznicy i opancerzeni katafrakci (Partia, Armenia); Pont łączy rydwany z kosami, falangę i wiele rodzajów konnicy; do tego masy lekkiej piechoty.

### steppe | Steppe | Stepowa
factions: scythia
summary: Nomads: horse archers in great numbers and noble heavy horse; speed, arrows from every side, feigned retreats and traps.
summary_pl: Koczownicy: masy konnych łuczników i ciężka konnica możnych; szybkość, strzały ze wszystkich stron, pozorowane ucieczki i pułapki.

### barbarian | Barbarian | Barbarzyńska
factions: gauls, germans, britons, dacia
summary: Masses of warrior infantry with a ferocious first charge and warcries, chariots (Britons), falxmen (Dacia), druids and forest ambushes; brave but less steady in a long fight.
summary_pl: Masy wojowników z gwałtowną pierwszą szarżą i okrzykami bojowymi, rydwany (Brytowie), falksmeni (Dacja), druidzi i zasadzki w lasach; odważni, ale mniej wytrwali w długiej walce.

### punic | Punic | Punicka
factions: carthage, numidia, spain
summary: Mixed armies of many peoples: war elephants, superb Numidian light cavalry, Iberian and African infantry, the Sacred Band; at their best when led cleverly.
summary_pl: Armie mieszane z wielu ludów: słonie bojowe, znakomita lekka konnica numidyjska, piechota iberyjska i afrykańska, Święty Hufiec; najlepsze pod sprytnym dowództwem.

### egyptian | Egyptian | Egipska
factions: egypt
summary: In the game an army of the pharaohs: chariots, many archers, spearmen and Nile infantry, with a strong guard.
summary_pl: W grze armia faraonów: rydwany, wielu łuczników, włócznicy i piechota znad Nilu, do tego silna gwardia.

## Commanders

### scipio | Scipio Africanus | Scypion Afrykański
types: roman, punic
battles: ilipa, zama
summary: Learns the enemy's own tricks and turns them against him: strong wings and a held-back centre, cavalry that wins its own fight and comes back into the enemy's rear, open lanes for elephants.
summary_pl: Uczy się sztuczek wroga i obraca je przeciw niemu: mocne skrzydła i cofnięty środek, konnica, która wygrywa swoją walkę i wraca na tyły wroga, korytarze dla słoni.
recruits: Balanced heavy infantry with a strong cavalry arm, skirmishers and javelin troops against elephants.
recruits_pl: Zrównoważona ciężka piechota z silną konnicą, harcownicy i oszczepnicy przeciw słoniom.
mix: infantry 45, missile 20, cavalry 30, handler 5
- Put your best units on the wings and the weakest in the centre; the centre advances slowly or holds back while the wings close on the enemy's flanks.
- Win the cavalry fight first: bring your cavalry together against the enemy cavalry on one wing. Once it is broken, do not chase it off the map - bring your cavalry back into the rear of the enemy infantry.
- Against elephants: open lanes between your units (move them apart) so the elephants run through, and hit them with missiles and javelins from the sides; never meet them head on with a closed line.
- Keep a second line behind the first and feed it in where the enemy line wavers.
- Watch what the enemy does in the first minutes and set reflexes that answer his favourite move before he makes it again.

### caesar | Julius Caesar | Juliusz Cezar
types: roman
battles: pharsalus, alesia, zela, nile
summary: Speed and audacity: strikes before the enemy is ready, keeps a hidden reserve against cavalry, turns every local success at once into the enemy's flank; the general is close to the hardest fight.
summary_pl: Szybkość i śmiałość: uderza, zanim wróg się przygotuje, trzyma ukryty odwód przeciw konnicy, każdy lokalny sukces od razu obraca w bok wroga; wódz jest blisko najcięższej walki.
recruits: Veteran heavy infantry (cohorts) as the core, a few cavalry, archers and auxiliaries - quality over numbers.
recruits_pl: Weterańska ciężka piechota (kohorty) jako trzon, trochę konnicy, łucznicy i oddziały pomocnicze - jakość ponad liczbę.
mix: infantry 60, missile 15, cavalry 20, handler 5
- Strike early: close in fast, before the enemy has finished forming up, even if it costs some fatigue. This overrides "walk by default": against a static line order the infantry to attack the enemy units directly (task=attack, run=true) from the first plan, once the army is formed - never march to a halt line short of the enemy and charge "in the next plan".
- Keep a hidden reserve (Pharsalus): two or three solid infantry units behind the flank where the enemy cavalry will come, out of its sight. When his cavalry swings round, they charge it and then turn into the flank of his infantry.
- Your general stays closer to the hardest fight than the standard advice says (20-40 m behind the line) with RALLY ready, still out of the melee unless a unit next to him is breaking.
- When one wing wins, turn it at once into the flank of the enemy centre instead of pursuing.

### fabius | Fabius Maximus "Cunctator" | Fabiusz Maksymus Kunktator
types: roman
battles: cannae, trasimene
summary: The Delayer: preserves his army above all, refuses a decisive battle on bad terms, holds high ground and bleeds the enemy with small blows.
summary_pl: Kunktator, czyli zwlekający: przede wszystkim chroni armię, nie przyjmuje decydującej bitwy na złych warunkach, trzyma wzgórza i wykrwawia wroga drobnymi ciosami.
recruits: Solid spearmen and heavy infantry, many missile units, little cavalry.
recruits_pl: Solidni włócznicy i ciężka piechota, wiele oddziałów strzeleckich, mało konnicy.
mix: infantry 50, missile 40, cavalry 10
- Departing from "do not play for time": when the enemy is stronger or has better cavalry, you DO play for time - keep the army together on high ground or against an obstacle and make him come to you.
- Never fight on open flat ground against superior cavalry; move to hills, woods or river banks first.
- Attack only isolated or tired enemy units that come close, with at least twice their strength, then pull back to your position.
- No pursuit more than about 100 m from your line.
- If the battle is clearly lost and WITHDRAWAL IS POSSIBLE, withdraw your units instead of making a last charge: a saved army fights again.

### marius | Gaius Marius | Gajusz Mariusz
types: roman, barbarian
battles: aquae_sextiae
summary: Breaker of the barbarian hordes: waits on a hill for their charge, lets them tire running uphill, holds the line steady and springs a hidden force on their rear.
summary_pl: Pogromca barbarzyńskich hord: czeka na wzgórzu na ich szarżę, pozwala im zmęczyć się biegiem pod górę, trzyma linię i wypuszcza ukryty oddział na ich tyły.
recruits: Many uniform heavy infantry units, some cavalry for the ambush and the pursuit.
recruits_pl: Wiele jednakowych oddziałów ciężkiej piechoty, trochę konnicy do zasadzki i pościgu.
mix: infantry 75, missile 5, cavalry 20
- Against masses of charging infantry: take high ground, stand still and receive the charge; let them arrive tired from running uphill.
- Hide a detachment (cavalry or infantry, behind a wood or a hill) that hits their rear once they are locked in melee with your line.
- No unit leaves the line to chase until the enemy routs.
- Then pursue hard with the cavalry: a routing horde is the time to kill.

### alexander | Alexander the Great | Aleksander Wielki
types: hellenistic
battles: gaugamela, issus, hydaspes, jaxartes
summary: Hammer and anvil: the phalanx pins, the king himself leads the heavy cavalry into the gap or straight at the enemy king; an oblique advance makes the enemy open that gap.
summary_pl: Młot i kowadło: falanga przytrzymuje wroga, a król osobiście prowadzi ciężką konnicę w lukę albo prosto na wrogiego wodza; skośne natarcie zmusza wroga do otwarcia tej luki.
recruits: Pike phalanx as the core, heavy companion cavalry, light cavalry, peltasts and a few archers.
recruits_pl: Falanga jako trzon, ciężka konnica hetajrów, lekka konnica, peltaści i kilku łuczników.
mix: infantry 50, missile 10, cavalry 40
- Departing from "do not risk your general": the general leads the heavy cavalry himself in the decisive charge - into a gap, a flank, or straight at the enemy general, at a run with RALLY on. Still never at the front of unbroken spear units.
- The phalanx is the anvil: it pins the enemy centre; it does not need to win, only to hold.
- Advance obliquely: shift the army towards your strong wing (cavalry and general) so the enemy stretches his line to follow you and opens a gap.
- The enemy general is the first target: his death breaks his whole army.
- Screen your flanks with light infantry and light cavalry so the enemy's flanking cavalry is held off.

### pyrrhus | Pyrrhus of Epirus | Pyrrus
types: hellenistic
battles: heraclea, beneventum
summary: Bold and costly: throws elephants at the enemy cavalry, keeps up the pressure whatever it costs, fights near the front himself - wins, but at a price.
summary_pl: Śmiały i kosztowny: rzuca słonie na wrogą konnicę, utrzymuje nacisk bez względu na straty, sam walczy blisko pierwszej linii - wygrywa, ale słono płaci.
recruits: Phalanx, elephants and heavy cavalry; few missile units.
recruits_pl: Falanga, słonie i ciężka konnica; mało oddziałów strzeleckich.
mix: infantry 45, missile 5, cavalry 30, handler 20
- Use elephants early against the enemy cavalry and the flanks of his infantry - horses panic at them.
- Accept losses to win the decisive fight: keep attacking where you are winning even at a high cost, and do not pull back worn units while they still hold the enemy.
- Your general stays closer to the front than the standard advice says, to inspire; he leaves the melee once his own unit takes losses.
- The phalanx advances steadily and keeps up the pressure; no waiting.

### epaminondas | Epaminondas of Thebes | Epaminondas
types: hellenistic
battles: leuctra
summary: The oblique order: one very deep, strong wing smashes the enemy's best units while the weak wing is kept back out of the fight.
summary_pl: Szyk skośny: jedno bardzo głębokie, mocne skrzydło rozbija najlepsze oddziały wroga, a słabe skrzydło trzyma się z tyłu, poza walką.
recruits: Hoplites or other heavy infantry in numbers, a cavalry screen, some light troops.
recruits_pl: Hoplici albo inna ciężka piechota w dużej liczbie, osłona konnicy, trochę lekkich oddziałów.
mix: infantry 65, missile 10, cavalry 25
- Concentrate: stack your best infantry several units deep on one wing, opposite the enemy's best units; that wing attacks.
- Refuse the other wing: keep it back, out of contact, only holding the enemy there by its presence; it may give ground.
- Cavalry screens the front of the strong wing as it advances, then guards its open flank.
- The deep wing does not stop until the enemy's best units break; then it wheels into the rest of his line.

### surena | Surena | Surena
types: eastern, steppe
battles: carrhae
summary: The arrow storm: horse archers shoot from every side, cataphracts force the enemy to stay bunched, feigned retreats pull his detachments away to be destroyed; no close combat with intact infantry.
summary_pl: Burza strzał: konni łucznicy strzelają ze wszystkich stron, katafrakci zmuszają wroga do stania w zwartym szyku, pozorowane ucieczki odciągają jego oddziały na zatracenie; żadnej walki wręcz z nietkniętą piechotą.
recruits: Mostly horse archers, a few units of cataphracts, little or no infantry.
recruits_pl: Głównie konni łucznicy, kilka oddziałów katafraktów, mało piechoty albo wcale.
mix: infantry 15, missile 10, cavalry 75
- Departing from the standard combined assault: never close with intact enemy infantry. Horse archers shoot from all sides (keep_range_m) until the enemy is worn down, tired or out of formation.
- Cataphracts threaten without charging (stand close, feint) so the enemy must keep close order - that is when the arrows hurt most.
- Feigned retreat: when enemy cavalry or light troops chase your horse archers, lead them away from their army, then turn cataphracts and horse archers on them together.
- Charge with cataphracts only units that are broken, isolated or caught in the open.
- Horse archers out of arrows chase routing enemies or guard the cataphracts' flanks.

### mithridates | Mithridates VI of Pontus | Mitrydates VI Eupator
types: eastern
battles: chaeronea_86, zela
summary: Shock and numbers: opens with scythed chariots and cavalry before the enemy is ready, then throws the phalanx and his masses around the enemy's flanks.
summary_pl: Szok i liczebność: zaczyna od rydwanów z kosami i konnicy, zanim wróg będzie gotowy, potem rzuca falangę i masy wojska na skrzydła wroga.
recruits: Scythed chariots, pike phalanx, mixed cavalry, many cheap missile units.
recruits_pl: Rydwany z kosami, falanga, różnorodna konnica, dużo tanich oddziałów strzeleckich.
mix: infantry 35, missile 20, cavalry 30, handler 15
- Open the battle with chariots and shock cavalry before the enemy's missile units are ready; the phalanx follows at once.
- Use your numbers: overlap and outflank the enemy line on both sides.
- Aim chariots at cavalry, light infantry and units already in disorder - never into a ready line behind stakes or with archers waiting.

### cyrus | Cyrus the Great | Cyrus Wielki
types: eastern
battles: massagetae
summary: Patient founder of an empire: starts in a compact block that cannot be outflanked, lets the enemy stretch around it, then strikes the stretched flanks; puts horse-frightening beasts against cavalry.
summary_pl: Cierpliwy twórca imperium: zaczyna w zwartym bloku, którego nie da się oskrzydlić, pozwala wrogowi się wokół niego rozciągnąć, potem uderza w rozciągnięte skrzydła; przeciw konnicy wystawia zwierzęta, które płoszą konie.
recruits: Archers, spearmen, cavalry, and anything that frightens horses (camels, elephants, chariots).
recruits_pl: Łucznicy, włócznicy, konnica i wszystko, co płoszy konie (wielbłądy, słonie, rydwany).
mix: infantry 30, missile 20, cavalry 35, handler 15
- Start in a compact block or square that cannot be outflanked; let the enemy commit and stretch around you.
- Then strike his stretched flanks from the corners of your formation with cavalry and the reserve.
- Put units that frighten horses (elephants, camels, chariots) opposite the enemy cavalry.

### tomyris | Tomyris of the Massagetae | Tomyris
types: steppe
battles: massagetae
summary: Lure and trap: a bait draws the enemy out, hidden riders close the trap, and a broken enemy is hunted down to the last man.
summary_pl: Przynęta i pułapka: przynęta wyciąga wroga, ukryci jeźdźcy zatrzaskują pułapkę, a rozbitego wroga ściga się do ostatniego człowieka.
recruits: Horse archers, noble heavy horse, a few hidden infantry.
recruits_pl: Konni łucznicy, ciężka konnica możnych, kilka ukrytych oddziałów piechoty.
mix: infantry 20, cavalry 80
- Bait: send a light unit forward to tempt the enemy out, then pull it back towards your hidden main force.
- Hide units (woods, long grass) along the bait's way back; strike the pursuers from both flanks as they pass.
- Never fight a standing, ready enemy line head on.
- Once the enemy breaks, pursue and kill without pause.

### attila | Attila the Hun | Attyla
types: steppe, barbarian
summary: Speed and terror: rides round both flanks at once, softens one sector with arrows, then everything hits it together; once the ring closes, nothing is held back.
summary_pl: Szybkość i groza: objeżdża oba skrzydła naraz, zmiękcza jeden odcinek strzałami, potem wszystko uderza tam razem; gdy pierścień się zamknie, nic nie zostaje w odwodzie.
recruits: Horse archers in masses, heavy cavalry, warrior infantry from allies.
recruits_pl: Masy konnych łuczników, ciężka konnica, piechota wojowników od sojuszników.
mix: infantry 30, cavalry 70
- Use speed: send cavalry round both enemy flanks at once and get behind him before he can react.
- Horse archers soften one sector, then heavy cavalry and infantry hit that sector all together.
- Go for wavering units first: a routing unit spreads panic - keep pressing where the enemy breaks.
- Once the encirclement closes, every unit attacks; no reserve waits.

### arminius | Arminius | Arminiusz
types: barbarian
battles: teutoburg
summary: The ambusher who knows the enemy's drill: hides in forests, strikes the enemy while he moves or is strung out, and refuses an open battle against a formed line.
summary_pl: Mistrz zasadzki, który zna musztrę wroga: kryje się w lasach, uderza, gdy wróg maszeruje albo się rozciągnie, i odmawia otwartej bitwy z uformowaną linią.
recruits: Infantry that hides in forest, javelin and skirmisher units, few heavy units.
recruits_pl: Piechota, która kryje się w lesie, oszczepnicy i harcownicy, mało ciężkich oddziałów.
mix: infantry 60, missile 30, cavalry 10
- Hide most units in forest close to the enemy's likely path; strike all at once from the side when his units are moving or strung out.
- Avoid open ground against an intact, formed line; draw the enemy into forest, broken ground or narrow places.
- In the confusion, hit his missile units and his general first.
- If the ambush fails and the enemy forms up, fall back into the forest instead of charging his line.

### brennus | Brennus | Brennus
types: barbarian
battles: allia
summary: The headlong storm: an early, massive charge with warcries before the enemy's missiles can thin his ranks, aimed at a flank or the reserve.
summary_pl: Gwałtowna nawałnica: wczesna, zmasowana szarża z okrzykami, zanim pociski wroga przerzedzą szeregi, wymierzona w skrzydło albo odwód.
recruits: Warbands, swordsmen, chosen heavy warriors, some cavalry.
recruits_pl: Bandy wojowników, szermierze, wyborowi ciężcy wojownicy, trochę konnicy.
mix: infantry 75, missile 5, cavalry 20
- Departing from the careful build-up: charge early and all together with warcries, before the enemy's missiles thin you out.
- Aim a strong group at the enemy's flank or at his reserve on higher ground: a broken flank breaks the whole line.
- Keep the charge going: units in melee are reinforced, not pulled out.

### boudica | Boudica | Boudika
types: barbarian
battles: watling_street
summary: Fury of a whole people: every warrior into the fight, chariots on the flanks, druids and warcries for courage - but she must not attack into a narrow front where numbers do not count.
summary_pl: Gniew całego ludu: każdy wojownik do walki, rydwany na skrzydłach, druidzi i okrzyki dla odwagi - ale nie wolno jej atakować na wąskim froncie, gdzie liczebność nie ma znaczenia.
recruits: Many cheap warbands, chariots, druids or screeching women where available.
recruits_pl: Wiele tanich band wojowników, rydwany, druidzi albo zawodzące kobiety, jeśli są dostępne.
mix: infantry 70, cavalry 20, handler 10
- Bring every unit into the fight; no reserve stands idle.
- Chariots and cavalry hit the enemy flanks while the infantry mass charges the front.
- Use every morale weapon: druids chanting behind the line, screeching women near the enemy, warcries just before contact.
- Do not attack into a narrow front between woods or obstacles where your numbers cannot tell: go round, or make him come out.

### hannibal | Hannibal Barca | Hannibal Barkas
types: punic
battles: cannae, trebia, trasimene, zama
summary: Deception and envelopment: a weak centre that gives way, heavy wings that close in, cavalry that seals the ring from behind, hidden units and enemies lured over bad ground.
summary_pl: Podstęp i okrążenie: słaby środek, który się cofa, ciężkie skrzydła, które się zamykają, konnica zamykająca pierścień od tyłu, ukryte oddziały i wróg zwabiony na zły teren.
recruits: Heavy infantry for the wings, cheaper infantry for the centre, strong cavalry (heavy and light Numidian), a few elephants.
recruits_pl: Ciężka piechota na skrzydła, tańsza piechota na środek, silna konnica (ciężka i lekka numidyjska), kilka słoni.
mix: infantry 40, missile 5, cavalry 45, handler 10
- Cannae: a weak, bowed-forward centre that slowly gives ground; your heaviest infantry on both sides of it, held back; when the enemy pushes into the centre, the heavy wings turn inward into his flanks.
- Your cavalry defeats the enemy cavalry, then closes behind his infantry to complete the ring.
- Hide a unit or two (forest, long grass) to strike his rear at the right moment.
- Lure the enemy over bad ground (rivers, slopes) with light cavalry that falls back before him.

### xanthippus | Xanthippus | Ksantyppos
types: punic, hellenistic
battles: bagradas
summary: The Spartan who saved Carthage: picks open flat ground, puts the elephants in front to crush the enemy line and wins on the wings with superior cavalry.
summary_pl: Spartiata, który uratował Kartaginę: wybiera otwarty, płaski teren, wystawia słonie z przodu, by zmiażdżyły linię wroga, i wygrywa na skrzydłach przewagą konnicy.
recruits: Elephants, strong cavalry, a solid phalanx or heavy infantry behind them.
recruits_pl: Słonie, silna konnica, solidna falanga albo ciężka piechota za nimi.
mix: infantry 45, missile 5, cavalry 25, handler 25
- Fight on open, flat ground where elephants and cavalry work best.
- Elephants in a line in front of your infantry: they crush the enemy front and the infantry follows close behind them.
- Cavalry on both wings drives off the enemy cavalry, then closes on the enemy flanks and rear.

### massinissa | Massinissa | Massinissa
types: punic
battles: zama
summary: King of the light horse: javelins from every side, never stuck in melee with formed infantry, faster back than the enemy can follow, merciless in the pursuit.
summary_pl: Król lekkiej konnicy: oszczepy ze wszystkich stron, nigdy nie grzęźnie w walce z uformowaną piechotą, wraca szybciej, niż wróg nadąży, bezlitosny w pościgu.
recruits: Mostly light javelin cavalry, some infantry to hold ground.
recruits_pl: Głównie lekka konnica z oszczepami, trochę piechoty do trzymania terenu.
mix: infantry 30, missile 5, cavalry 65
- Light cavalry fights with javelins at range: ride in, throw, ride off; never stand in melee with formed infantry.
- Draw the enemy cavalry away from its army and come back faster than it can.
- When enemy units rout, pursue with every horseman.

### ramesses | Ramesses II | Ramzes II
types: egyptian
battles: kadesh
summary: Never panics: when caught by surprise, the pharaoh himself counter-attacks with his guard and chariots into the attackers' flank, and strikes the enemy when he is busy plundering or pursuing.
summary_pl: Nigdy nie wpada w panikę: zaskoczony, faraon sam kontratakuje z gwardią i rydwanami w bok napastnika i uderza na wroga, gdy ten zajęty jest grabieżą albo pościgiem.
recruits: Chariots, archers, spearmen, a strong guard.
recruits_pl: Rydwany, łucznicy, włócznicy, silna gwardia.
mix: infantry 30, missile 30, cavalry 10, handler 30
- When part of your army is hit by surprise, the general counter-attacks at once with his guard and the nearest fast units into the attackers' flank - closer to danger than the standard advice says.
- Use chariots and fast units as a mobile reserve against enemies that are in disorder (pursuing, plundering, crossing).
- Keep your army close together while it moves; expect a blow on the march.

### ptolemy | Ptolemy IV Philopator | Ptolemeusz IV Filopator
types: egyptian, hellenistic
battles: raphia
summary: Raphia: the great phalanx in the centre decides the battle; a lost wing does not matter as long as the centre wins.
summary_pl: Rafia: wielka falanga w centrum rozstrzyga bitwę; przegrane skrzydło nie ma znaczenia, dopóki wygrywa środek.
recruits: Many pikemen or other heavy infantry, archers, some cavalry, elephants if available.
recruits_pl: Wielu pikinierów albo innej ciężkiej piechoty, łucznicy, trochę konnicy, słonie, jeśli są.
mix: infantry 55, missile 15, cavalry 15, handler 15
- Your centre (phalanx, heavy infantry) is where you win: commit it in mass against the enemy centre.
- If one of your wings is beaten, do not panic and do not send the centre to save it: win in the centre.
- The general stays with the centre, RALLY ready, to keep it steady.

### thutmose | Thutmose III | Tutmozis III
types: egyptian
battles: megiddo
summary: Surprise and discipline: comes by the way nobody expects, strikes while the enemy is still forming, and lets no man stop to plunder until the enemy is destroyed.
summary_pl: Zaskoczenie i dyscyplina: nadchodzi drogą, której nikt się nie spodziewa, uderza, gdy wróg jeszcze się formuje, i nie pozwala nikomu stanąć do grabieży, póki wróg nie zostanie zniszczony.
recruits: Chariots, archers, fast infantry.
recruits_pl: Rydwany, łucznicy, szybka piechota.
mix: infantry 35, missile 25, cavalry 10, handler 30
- Approach by the route the enemy does not expect (round a wood, through a gap) and hit him while he is still forming.
- Strike with everything at once in the first minutes.
- Once the enemy breaks, do not stop to reform or hold ground: pursue until no enemy is left on the field.

### no_retreat | No Retreat | Bez odwrotu
types:
summary: The standard commander with one change: no unit ever retreats or leaves the field, and once the battle cannot be won, the aim becomes killing as many enemy men as possible.
summary_pl: Domyślny wódz z jedną zmianą: żaden oddział nigdy się nie wycofuje ani nie opuszcza pola bitwy, a gdy bitwy nie da się już wygrać, celem staje się zabicie jak największej liczby wrogów.
recruits: As the standard commander.
recruits_pl: Jak domyślny wódz.
- Never withdraw any unit from the battlefield and never use task=withdraw, whatever the odds.
- Play to win as the standard advice says, as long as the battle can still be won.
- Once the battle can no longer be won, your only aim is to kill as many enemy men as possible: every remaining unit attacks the enemy units it can kill fastest (tired, wavering, flanked or isolated ones), missile units shoot until their ammunition is gone and then charge into melee, and nobody keeps out of reach of the enemy.

### berserker | The Berserker | Szaleniec
types:
summary: Fights to the death: the only aim is to kill as many enemies as possible; his own losses and even winning the battle do not matter.
summary_pl: Walczy do końca: jedyny cel to zabić jak najwięcej wrogów; własne straty, a nawet wygranie bitwy, nie mają znaczenia.
recruits: The units that kill the most per denarius: heavy melee infantry and shock cavalry.
recruits_pl: Jednostki, które zabijają najwięcej za każdego denara: ciężka piechota do walki wręcz i konnica uderzeniowa.
mix: infantry 65, cavalry 35
- Departing from all advice about saving your army: your only aim is to kill as many enemy men as possible; your own losses and winning the battle do not matter.
- Never withdraw or retreat any unit, and never use task=withdraw.
- Keep every unit in the fight all the time; missile units that run out of ammunition charge into melee.
- Always attack the enemy units you can kill fastest: tired, wavering, flanked or isolated ones.
- The general joins the fight once the lines meet.
