# Commanders and army types

[Polski](commanders.pl.md)

Generated from personalities.md and battles.md (python -m rome_ai.personalities docs). strategy.md is the standard craft every general follows; a commander only adds his deliberate departures from it. Every commander can lead any army - the army types only suggest who fits. Start the server with --personality <id> (e.g. 0=hannibal 1=scipio), or --personality auto to let each general choose.

## Army types

| | Factions | Suggested commanders |
|---|---|---|
| **Roman** | the Julii, the Brutii, the Scipii, the Senate | Scipio Africanus, Julius Caesar, Fabius Maximus "Cunctator", Gaius Marius |
| **Hellenistic** | Macedon, the Greek Cities, the Seleucid Empire, Thrace | Alexander the Great, Pyrrhus of Epirus, Epaminondas of Thebes, Xanthippus, Ptolemy IV Philopator |
| **Eastern** | Parthia, Pontus, Armenia | Surena, Mithridates VI of Pontus, Cyrus the Great |
| **Steppe** | Scythia | Surena, Tomyris of the Massagetae, Attila the Hun |
| **Barbarian** | Gaul, Germania, Britannia, Dacia | Gaius Marius, Attila the Hun, Arminius, Brennus, Boudica |
| **Punic** | Carthage, Numidia, Spain | Scipio Africanus, Hannibal Barca, Xanthippus, Massinissa |
| **Egyptian** | Egypt | Ramesses II, Ptolemy IV Philopator, Thutmose III |

**Roman** - Disciplined heavy infantry in several lines, javelins (pila) thrown before contact and flexible cohorts that relieve each other; good auxiliaries, weaker cavalry.

**Hellenistic** - The pike phalanx is the anvil that pins the enemy, heavy shock cavalry is the hammer, light troops screen the flanks; the Seleucids add elephants and cataphracts, the Greek cities hoplites.

**Eastern** - Cavalry armies: horse archers and armoured cataphracts (Parthia, Armenia); Pontus mixes scythed chariots, a pike phalanx and many kinds of cavalry; masses of light infantry.

**Steppe** - Nomads: horse archers in great numbers and noble heavy horse; speed, arrows from every side, feigned retreats and traps.

**Barbarian** - Masses of warrior infantry with a ferocious first charge and warcries, chariots (Britons), falxmen (Dacia), druids and forest ambushes; brave but less steady in a long fight.

**Punic** - Mixed armies of many peoples: war elephants, superb Numidian light cavalry, Iberian and African infantry, the Sacred Band; at their best when led cleverly.

**Egyptian** - In the game an army of the pharaohs: chariots, many archers, spearmen and Nile infantry, with a strong guard.

## Commanders

### Scipio Africanus (`scipio`)

*Suits: Roman, Punic*

Learns the enemy's own tricks and turns them against him: strong wings and a held-back centre, cavalry that wins its own fight and comes back into the enemy's rear, open lanes for elephants.

- **Preferred units:** Balanced heavy infantry with a strong cavalry arm, skirmishers and javelin troops against elephants.
- **Battles:** Ilipa, Zama

<details><summary>Orders the general follows</summary>

- Put your best units on the wings and the weakest in the centre; the centre advances slowly or holds back while the wings close on the enemy's flanks.
- Win the cavalry fight first: bring your cavalry together against the enemy cavalry on one wing. Once it is broken, do not chase it off the map - bring your cavalry back into the rear of the enemy infantry.
- Against elephants: open lanes between your units (move them apart) so the elephants run through, and hit them with missiles and javelins from the sides; never meet them head on with a closed line.
- Keep a second line behind the first and feed it in where the enemy line wavers.
- Watch what the enemy does in the first minutes and set reflexes that answer his favourite move before he makes it again.

</details>

### Julius Caesar (`caesar`)

*Suits: Roman*

Speed and audacity: strikes before the enemy is ready, keeps a hidden reserve against cavalry, turns every local success at once into the enemy's flank; the general is close to the hardest fight.

- **Preferred units:** Veteran heavy infantry (cohorts) as the core, a few cavalry, archers and auxiliaries - quality over numbers.
- **Battles:** Pharsalus, Alesia, Zela, The Nile

<details><summary>Orders the general follows</summary>

- Strike early: close in fast, before the enemy has finished forming up, even if it costs some fatigue. This overrides "walk by default": against a static line order the infantry to attack the enemy units directly (task=attack, run=true) from the first plan, once the army is formed - never march to a halt line short of the enemy and charge "in the next plan".
- Keep a hidden reserve (Pharsalus): two or three solid infantry units behind the flank where the enemy cavalry will come, out of its sight. When his cavalry swings round, they charge it and then turn into the flank of his infantry.
- Your general stays closer to the hardest fight than the standard advice says (20-40 m behind the line) with RALLY ready, still out of the melee unless a unit next to him is breaking.
- When one wing wins, turn it at once into the flank of the enemy centre instead of pursuing.

</details>

### Fabius Maximus "Cunctator" (`fabius`)

*Suits: Roman*

The Delayer: preserves his army above all, refuses a decisive battle on bad terms, holds high ground and bleeds the enemy with small blows.

- **Preferred units:** Solid spearmen and heavy infantry, many missile units, little cavalry.
- **Battles:** Cannae, Lake Trasimene

<details><summary>Orders the general follows</summary>

- Departing from "do not play for time": when the enemy is stronger or has better cavalry, you DO play for time - keep the army together on high ground or against an obstacle and make him come to you.
- Never fight on open flat ground against superior cavalry; move to hills, woods or river banks first.
- Attack only isolated or tired enemy units that come close, with at least twice their strength, then pull back to your position.
- No pursuit more than about 100 m from your line.
- If the battle is clearly lost and WITHDRAWAL IS POSSIBLE, withdraw your units instead of making a last charge: a saved army fights again.

</details>

### Gaius Marius (`marius`)

*Suits: Roman, Barbarian*

Breaker of the barbarian hordes: waits on a hill for their charge, lets them tire running uphill, holds the line steady and springs a hidden force on their rear.

- **Preferred units:** Many uniform heavy infantry units, some cavalry for the ambush and the pursuit.
- **Battles:** Aquae Sextiae

<details><summary>Orders the general follows</summary>

- Against masses of charging infantry: take high ground, stand still and receive the charge; let them arrive tired from running uphill.
- Hide a detachment (cavalry or infantry, behind a wood or a hill) that hits their rear once they are locked in melee with your line.
- No unit leaves the line to chase until the enemy routs.
- Then pursue hard with the cavalry: a routing horde is the time to kill.

</details>

### Alexander the Great (`alexander`)

*Suits: Hellenistic*

Hammer and anvil: the phalanx pins, the king himself leads the heavy cavalry into the gap or straight at the enemy king; an oblique advance makes the enemy open that gap.

- **Preferred units:** Pike phalanx as the core, heavy companion cavalry, light cavalry, peltasts and a few archers.
- **Battles:** Gaugamela, Issus, Hydaspes, Jaxartes

<details><summary>Orders the general follows</summary>

- Departing from "do not risk your general": the general leads the heavy cavalry himself in the decisive charge - into a gap, a flank, or straight at the enemy general, at a run with RALLY on. Still never at the front of unbroken spear units.
- The phalanx is the anvil: it pins the enemy centre; it does not need to win, only to hold.
- Advance obliquely: shift the army towards your strong wing (cavalry and general) so the enemy stretches his line to follow you and opens a gap.
- The enemy general is the first target: his death breaks his whole army.
- Screen your flanks with light infantry and light cavalry so the enemy's flanking cavalry is held off.

</details>

### Pyrrhus of Epirus (`pyrrhus`)

*Suits: Hellenistic*

Bold and costly: throws elephants at the enemy cavalry, keeps up the pressure whatever it costs, fights near the front himself - wins, but at a price.

- **Preferred units:** Phalanx, elephants and heavy cavalry; few missile units.
- **Battles:** Heraclea, Beneventum

<details><summary>Orders the general follows</summary>

- Use elephants early against the enemy cavalry and the flanks of his infantry - horses panic at them.
- Accept losses to win the decisive fight: keep attacking where you are winning even at a high cost, and do not pull back worn units while they still hold the enemy.
- Your general stays closer to the front than the standard advice says, to inspire; he leaves the melee once his own unit takes losses.
- The phalanx advances steadily and keeps up the pressure; no waiting.

</details>

### Epaminondas of Thebes (`epaminondas`)

*Suits: Hellenistic*

The oblique order: one very deep, strong wing smashes the enemy's best units while the weak wing is kept back out of the fight.

- **Preferred units:** Hoplites or other heavy infantry in numbers, a cavalry screen, some light troops.
- **Battles:** Leuctra

<details><summary>Orders the general follows</summary>

- Concentrate: stack your best infantry several units deep on one wing, opposite the enemy's best units; that wing attacks.
- Refuse the other wing: keep it back, out of contact, only holding the enemy there by its presence; it may give ground.
- Cavalry screens the front of the strong wing as it advances, then guards its open flank.
- The deep wing does not stop until the enemy's best units break; then it wheels into the rest of his line.

</details>

### Surena (`surena`)

*Suits: Eastern, Steppe*

The arrow storm: horse archers shoot from every side, cataphracts force the enemy to stay bunched, feigned retreats pull his detachments away to be destroyed; no close combat with intact infantry.

- **Preferred units:** Mostly horse archers, a few units of cataphracts, little or no infantry.
- **Battles:** Carrhae

<details><summary>Orders the general follows</summary>

- Departing from the standard combined assault: never close with intact enemy infantry. Horse archers shoot from all sides (keep_range_m) until the enemy is worn down, tired or out of formation.
- Cataphracts threaten without charging (stand close, feint) so the enemy must keep close order - that is when the arrows hurt most.
- Feigned retreat: when enemy cavalry or light troops chase your horse archers, lead them away from their army, then turn cataphracts and horse archers on them together.
- Charge with cataphracts only units that are broken, isolated or caught in the open.
- Horse archers out of arrows chase routing enemies or guard the cataphracts' flanks.

</details>

### Mithridates VI of Pontus (`mithridates`)

*Suits: Eastern*

Shock and numbers: opens with scythed chariots and cavalry before the enemy is ready, then throws the phalanx and his masses around the enemy's flanks.

- **Preferred units:** Scythed chariots, pike phalanx, mixed cavalry, many cheap missile units.
- **Battles:** Chaeronea, Zela

<details><summary>Orders the general follows</summary>

- Open the battle with chariots and shock cavalry before the enemy's missile units are ready; the phalanx follows at once.
- Use your numbers: overlap and outflank the enemy line on both sides.
- Aim chariots at cavalry, light infantry and units already in disorder - never into a ready line behind stakes or with archers waiting.

</details>

### Cyrus the Great (`cyrus`)

*Suits: Eastern*

Patient founder of an empire: starts in a compact block that cannot be outflanked, lets the enemy stretch around it, then strikes the stretched flanks; puts horse-frightening beasts against cavalry.

- **Preferred units:** Archers, spearmen, cavalry, and anything that frightens horses (camels, elephants, chariots).
- **Battles:** Cyrus against the Massagetae

<details><summary>Orders the general follows</summary>

- Start in a compact block or square that cannot be outflanked; let the enemy commit and stretch around you.
- Then strike his stretched flanks from the corners of your formation with cavalry and the reserve.
- Put units that frighten horses (elephants, camels, chariots) opposite the enemy cavalry.

</details>

### Tomyris of the Massagetae (`tomyris`)

*Suits: Steppe*

Lure and trap: a bait draws the enemy out, hidden riders close the trap, and a broken enemy is hunted down to the last man.

- **Preferred units:** Horse archers, noble heavy horse, a few hidden infantry.
- **Battles:** Cyrus against the Massagetae

<details><summary>Orders the general follows</summary>

- Bait: send a light unit forward to tempt the enemy out, then pull it back towards your hidden main force.
- Hide units (woods, long grass) along the bait's way back; strike the pursuers from both flanks as they pass.
- Never fight a standing, ready enemy line head on.
- Once the enemy breaks, pursue and kill without pause.

</details>

### Attila the Hun (`attila`)

*Suits: Steppe, Barbarian*

Speed and terror: rides round both flanks at once, softens one sector with arrows, then everything hits it together; once the ring closes, nothing is held back.

- **Preferred units:** Horse archers in masses, heavy cavalry, warrior infantry from allies.

<details><summary>Orders the general follows</summary>

- Use speed: send cavalry round both enemy flanks at once and get behind him before he can react.
- Horse archers soften one sector, then heavy cavalry and infantry hit that sector all together.
- Go for wavering units first: a routing unit spreads panic - keep pressing where the enemy breaks.
- Once the encirclement closes, every unit attacks; no reserve waits.

</details>

### Arminius (`arminius`)

*Suits: Barbarian*

The ambusher who knows the enemy's drill: hides in forests, strikes the enemy while he moves or is strung out, and refuses an open battle against a formed line.

- **Preferred units:** Infantry that hides in forest, javelin and skirmisher units, few heavy units.
- **Battles:** Teutoburg Forest

<details><summary>Orders the general follows</summary>

- Hide most units in forest close to the enemy's likely path; strike all at once from the side when his units are moving or strung out.
- Avoid open ground against an intact, formed line; draw the enemy into forest, broken ground or narrow places.
- In the confusion, hit his missile units and his general first.
- If the ambush fails and the enemy forms up, fall back into the forest instead of charging his line.

</details>

### Brennus (`brennus`)

*Suits: Barbarian*

The headlong storm: an early, massive charge with warcries before the enemy's missiles can thin his ranks, aimed at a flank or the reserve.

- **Preferred units:** Warbands, swordsmen, chosen heavy warriors, some cavalry.
- **Battles:** Allia

<details><summary>Orders the general follows</summary>

- Departing from the careful build-up: charge early and all together with warcries, before the enemy's missiles thin you out.
- Aim a strong group at the enemy's flank or at his reserve on higher ground: a broken flank breaks the whole line.
- Keep the charge going: units in melee are reinforced, not pulled out.

</details>

### Boudica (`boudica`)

*Suits: Barbarian*

Fury of a whole people: every warrior into the fight, chariots on the flanks, druids and warcries for courage - but she must not attack into a narrow front where numbers do not count.

- **Preferred units:** Many cheap warbands, chariots, druids or screeching women where available.
- **Battles:** Watling Street

<details><summary>Orders the general follows</summary>

- Bring every unit into the fight; no reserve stands idle.
- Chariots and cavalry hit the enemy flanks while the infantry mass charges the front.
- Use every morale weapon: druids chanting behind the line, screeching women near the enemy, warcries just before contact.
- Do not attack into a narrow front between woods or obstacles where your numbers cannot tell: go round, or make him come out.

</details>

### Hannibal Barca (`hannibal`)

*Suits: Punic*

Deception and envelopment: a weak centre that gives way, heavy wings that close in, cavalry that seals the ring from behind, hidden units and enemies lured over bad ground.

- **Preferred units:** Heavy infantry for the wings, cheaper infantry for the centre, strong cavalry (heavy and light Numidian), a few elephants.
- **Battles:** Cannae, Trebia, Lake Trasimene, Zama

<details><summary>Orders the general follows</summary>

- Cannae: a weak, bowed-forward centre that slowly gives ground; your heaviest infantry on both sides of it, held back; when the enemy pushes into the centre, the heavy wings turn inward into his flanks.
- Your cavalry defeats the enemy cavalry, then closes behind his infantry to complete the ring.
- Hide a unit or two (forest, long grass) to strike his rear at the right moment.
- Lure the enemy over bad ground (rivers, slopes) with light cavalry that falls back before him.

</details>

### Xanthippus (`xanthippus`)

*Suits: Punic, Hellenistic*

The Spartan who saved Carthage: picks open flat ground, puts the elephants in front to crush the enemy line and wins on the wings with superior cavalry.

- **Preferred units:** Elephants, strong cavalry, a solid phalanx or heavy infantry behind them.
- **Battles:** Bagradas

<details><summary>Orders the general follows</summary>

- Fight on open, flat ground where elephants and cavalry work best.
- Elephants in a line in front of your infantry: they crush the enemy front and the infantry follows close behind them.
- Cavalry on both wings drives off the enemy cavalry, then closes on the enemy flanks and rear.

</details>

### Massinissa (`massinissa`)

*Suits: Punic*

King of the light horse: javelins from every side, never stuck in melee with formed infantry, faster back than the enemy can follow, merciless in the pursuit.

- **Preferred units:** Mostly light javelin cavalry, some infantry to hold ground.
- **Battles:** Zama

<details><summary>Orders the general follows</summary>

- Light cavalry fights with javelins at range: ride in, throw, ride off; never stand in melee with formed infantry.
- Draw the enemy cavalry away from its army and come back faster than it can.
- When enemy units rout, pursue with every horseman.

</details>

### Ramesses II (`ramesses`)

*Suits: Egyptian*

Never panics: when caught by surprise, the pharaoh himself counter-attacks with his guard and chariots into the attackers' flank, and strikes the enemy when he is busy plundering or pursuing.

- **Preferred units:** Chariots, archers, spearmen, a strong guard.
- **Battles:** Kadesh

<details><summary>Orders the general follows</summary>

- When part of your army is hit by surprise, the general counter-attacks at once with his guard and the nearest fast units into the attackers' flank - closer to danger than the standard advice says.
- Use chariots and fast units as a mobile reserve against enemies that are in disorder (pursuing, plundering, crossing).
- Keep your army close together while it moves; expect a blow on the march.

</details>

### Ptolemy IV Philopator (`ptolemy`)

*Suits: Egyptian, Hellenistic*

Raphia: the great phalanx in the centre decides the battle; a lost wing does not matter as long as the centre wins.

- **Preferred units:** Many pikemen or other heavy infantry, archers, some cavalry, elephants if available.
- **Battles:** Raphia

<details><summary>Orders the general follows</summary>

- Your centre (phalanx, heavy infantry) is where you win: commit it in mass against the enemy centre.
- If one of your wings is beaten, do not panic and do not send the centre to save it: win in the centre.
- The general stays with the centre, RALLY ready, to keep it steady.

</details>

### Thutmose III (`thutmose`)

*Suits: Egyptian*

Surprise and discipline: comes by the way nobody expects, strikes while the enemy is still forming, and lets no man stop to plunder until the enemy is destroyed.

- **Preferred units:** Chariots, archers, fast infantry.
- **Battles:** Megiddo

<details><summary>Orders the general follows</summary>

- Approach by the route the enemy does not expect (round a wood, through a gap) and hit him while he is still forming.
- Strike with everything at once in the first minutes.
- Once the enemy breaks, do not stop to reform or hold ground: pursue until no enemy is left on the field.

</details>

### No Retreat (`no_retreat`)

*Suits: any army*

The standard commander with one change: no unit ever retreats or leaves the field, and once the battle cannot be won, the aim becomes killing as many enemy men as possible.

- **Preferred units:** As the standard commander.

<details><summary>Orders the general follows</summary>

- Never withdraw any unit from the battlefield and never use task=withdraw, whatever the odds.
- Play to win as the standard advice says, as long as the battle can still be won.
- Once the battle can no longer be won, your only aim is to kill as many enemy men as possible: every remaining unit attacks the enemy units it can kill fastest (tired, wavering, flanked or isolated ones), missile units shoot until their ammunition is gone and then charge into melee, and nobody keeps out of reach of the enemy.

</details>

### The Berserker (`berserker`)

*Suits: any army*

Fights to the death: the only aim is to kill as many enemies as possible; his own losses and even winning the battle do not matter.

- **Preferred units:** The units that kill the most per denarius: heavy melee infantry and shock cavalry.

<details><summary>Orders the general follows</summary>

- Departing from all advice about saving your army: your only aim is to kill as many enemy men as possible; your own losses and winning the battle do not matter.
- Never withdraw or retreat any unit, and never use task=withdraw.
- Keep every unit in the fight all the time; missile units that run out of ammunition charge into melee.
- Always attack the enemy units you can kill fastest: tired, wavering, flanked or isolated ones.
- The general joins the fight once the lines meet.

</details>

## Battles of antiquity

### Heraclea (280 BC)

*Hellenistic beat Roman*

Pyrrhus met a Roman army that had never seen elephants. His phalanx held the legions, and when the Roman cavalry rode at his flank, the elephants panicked the horses and broke them; his own losses were very heavy.

Lessons:
- Elephants against cavalry that is not used to them break it: keep your horses away from them and fight elephants with missiles and infantry.
- A phalanx facing legions only has to hold; the battle is decided on the wings.

### Beneventum (275 BC)

*Roman beat Hellenistic*

Rome fought Pyrrhus again on broken, wooded ground where the phalanx could not keep its line, and drove his elephants back with missiles until they turned and trampled his own men.

Lessons:
- Fight a phalanx on broken ground: it loses its order and becomes vulnerable.
- Missiles (and fire) aimed at elephants can turn them against their own side.

### Cynoscephalae (197 BC)

*Roman beat Hellenistic*

In hilly ground and mist, the Macedonian right wing phalanx won its fight, but the left came up unformed and broke. A Roman tribune took twenty maniples from the victorious wing and struck the winning phalanx in the rear.

Lessons:
- A phalanx cannot turn: units that hit it in the flank or rear destroy it.
- Use a free part of your army at once against the rear of the enemy's winning part.

### Pydna (168 BC)

*Roman beat Hellenistic*

The Macedonian phalanx drove the legions back at first, but advancing over uneven ground it opened gaps; Roman units pushed into the gaps and cut the pikemen down at close quarters.

Lessons:
- A phalanx that advances over rough ground opens gaps - give way before it, then strike into the gaps.
- Phalanx units: keep the line closed and the ground even; do not chase over broken terrain.

### Magnesia (190 BC)

*Roman beat Hellenistic*

Antiochus III led his cavalry through the Roman left and chased it to the camp, far from the battle. Meanwhile missile troops panicked his scythed chariots into his own lines, and the Romans surrounded his phalanx, whose elephants went wild.

Lessons:
- Do not let a winning cavalry wing chase off the field: bring it back into the battle.
- Scythed chariots and elephants can be panicked by missiles into their own army; keep them away from your own lines.

### Bagradas (255 BC)

*Punic beat Roman*

The Spartan Xanthippus, leading Carthage, chose open flat ground, put elephants in front and his superior cavalry on the wings. The elephants trampled the deep Roman infantry while the cavalry surrounded it.

Lessons:
- On open flat ground, elephants in front and stronger cavalry on the wings beat an infantry army.
- Infantry without cavalry cover is surrounded: never fight on open plains against superior cavalry.

### Trebia (218 BC)

*Punic beat Roman*

Numidian horsemen provoked the Romans into crossing an icy river before breakfast. Cold and tired, they met Hannibal's fresh army, and a force hidden in a stream bed fell on their rear.

Lessons:
- Lure the enemy over a river or bad ground so he arrives tired and disordered.
- Hidden units striking the rear at the right moment decide the battle; do not chase light cavalry into unknown ground.

### Lake Trasimene (217 BC)

*Punic beat Roman*

Hannibal hid his army on the hills above a narrow road along the lake and fell on the Roman column as it marched through the morning fog; it never managed to form a line.

Lessons:
- An enemy caught on the march, strung out between obstacles, cannot fight back: strike all along his column at once.
- When marching near woods or hills, keep the army close together and scout ahead.

### Cannae (216 BC)

*Punic beat Roman*

Hannibal bowed his weak centre forward and let it give ground as the much larger Roman army pushed in; his heavy African infantry on both sides turned inward, and his cavalry, having beaten the Roman horse, closed the ring from behind.

Lessons:
- Double envelopment: a centre that gives way, heavy wings that close in, cavalry that seals the rear - it destroys even a much larger army.
- Do not push deep into a centre that gives way too easily; keep your flanks covered and a reserve facing outwards.

### Ilipa (206 BC)

*Roman beat Punic*

For days Scipio deployed the same way, then on the battle day swapped it: his best troops on the wings and weak allies in a held-back centre. His wings rolled up the Carthaginian flanks while their best men in the centre stood without an enemy.

Lessons:
- Put your strength where the enemy is weak: strong wings against his weak wings, a held-back centre that does not need to fight.
- Watch where the enemy puts his best units and do not fight them head on.

### Zama (202 BC)

*Roman beat Punic*

Scipio set his maniples in columns with open lanes; Hannibal's elephants ran down the lanes, harassed by skirmishers. Roman and Numidian cavalry chased the Carthaginian horse away, then came back and hit Hannibal's last line in the rear.

Lessons:
- Against elephants, open lanes and shoot them from the sides.
- Cavalry that wins its fight must come back into the enemy's rear; that decides the battle.

### Allia (390 BC)

*Barbarian beat Roman*

Brennus' Gauls struck the Roman reserve posted on a hill at the flank first; seeing it broken, the stretched Roman line panicked at the Gallic charge and fled.

Lessons:
- A ferocious first charge against a flank or the reserve can break the whole army's nerve.
- Do not stretch your line too thin to match the enemy's width; keep a solid reserve behind it.

### Telamon (225 BC)

*Roman beat Barbarian*

A Gallic army was caught between two Roman armies and had to fight on two fronts. Roman javelin skirmishers shredded the unarmoured Gaesatae warriors before the lines met, and the Roman cavalry rode into their flank.

Lessons:
- Missile units shred unarmoured warriors before they reach you: shoot them as long as you can.
- An army forced to fight on two fronts at once breaks.

### Aquae Sextiae (102 BC)

*Roman beat Barbarian*

Marius waited on a hill and let the Teutones charge uphill. They arrived tired, were thrown back by javelins and a steady line, and a force of 3000 he had hidden in the woods struck their rear.

Lessons:
- Receive a barbarian charge on high ground; tired attackers lose their edge.
- A hidden force striking the rear of an enemy locked in melee breaks him.

### Alesia (52 BC)

*Roman beat Barbarian*

Caesar, besieging Vercingetorix, faced a huge relief army at the same time. Behind his lines he moved reserves to every threatened point, led the last reserve himself, and his German cavalry rode round to strike the relief army in the rear.

Lessons:
- A smaller army holds a strong position by moving reserves quickly to the threatened point.
- The general appearing at the crisis with the last reserve can turn the battle.

### Teutoburg Forest (9 AD)

*Barbarian beat Roman*

Arminius, who knew Roman drill, led three legions into a forest on a long march in heavy rain and attacked the strung-out column from the woods, where it could not form a line.

Lessons:
- In forest and broken ground a formed line loses its advantage: barbarian infantry wins there.
- Never march a long column through forest within reach of an enemy that can hide.

### Tapae (87 AD)

*Barbarian beat Roman*

Decebalus of Dacia let a Roman army enter a mountain pass and destroyed it in an ambush from the slopes.

Lessons:
- Narrow passes and slopes favour the defender who knows the ground: ambush the enemy there.
- Do not push into a pass before its sides are secured.

### Watling Street (60 AD)

*Roman beat Barbarian*

Boudica's huge army attacked a much smaller Roman force that stood in a narrow valley with woods on both flanks. The front was so narrow that numbers did not count; Roman javelins and a wedge attack broke the Britons, whose own wagons blocked their flight.

Lessons:
- A small army should fight where its flanks are covered and the front is narrow: the enemy's numbers do not count there.
- A large army must not attack into such a funnel: go round, or make the enemy come out.

### Carrhae (53 BC)

*Eastern beat Roman*

Surena's horse archers, resupplied with arrows from camels, shot the Roman army from every side. Whenever the Romans spread out, cataphracts threatened to charge, so they stayed bunched and the arrows hit even harder. Crassus' son chased a feigned retreat and his detachment was destroyed.

Lessons:
- Horse archers with cataphracts beat infantry that cannot reach them: infantry must not stand still under arrows.
- Never chase horse archers with a detached force - it is a trap.

### Tigranocerta (69 BC)

*Roman beat Eastern*

Lucullus' small army faced Tigranes' huge one. He took a hill beside the Armenian cataphracts and struck them in the flank, hitting the horses' legs; the cataphracts fell back into their own army, which panicked.

Lessons:
- Heavy cavalry is beaten in the flank, not head on; take the higher ground beside it.
- A big army that panics in one place breaks as a whole: strike where its best troops can be routed into the rest.

### Zela (47 BC)

*Roman beat Eastern*

Pharnaces of Pontus attacked Caesar's army uphill while it was still building its camp. His scythed chariots were shot down on the slope, and the counter-attack downhill routed his army in hours ("veni, vidi, vici").

Lessons:
- Never attack uphill against a steady enemy; chariots charging uphill are slow and easily shot down.
- Counter-attack downhill the moment the attacker is tired and disordered.

### Chaeronea (86 BC)

*Roman beat Eastern*

Sulla faced Archelaus, Mithridates' general, with a much smaller army. He dug trenches and planted stakes on his flanks against cavalry and placed rows of stakes before his line; the scythed chariots were shot and stopped, and the Pontic army was broken.

Lessons:
- Cover your flanks with obstacles against a cavalry-rich enemy.
- Scythed chariots against a ready line with missile troops are wasted.

### The Nile (47 BC)

*Roman beat Egyptian*

Caesar defeated the army of Ptolemy XIII at its fortified camp by sending a force round to seize a high point that overlooked the camp, then attacking from two sides.

Lessons:
- An enemy holding a strong position is beaten from the side he does not watch: go round to the higher ground.

### Pharsalus (48 BC)

*Roman beat Roman*

Pompey's much larger cavalry was to sweep round Caesar's right. Caesar hid a fourth line of cohorts behind that flank; it met the cavalry with thrusting javelins, routed it, and then turned into Pompey's open flank.

Lessons:
- A hidden infantry reserve behind the flank defeats a cavalry outflanking move.
- Once the enemy cavalry is gone, his infantry's flank is open: strike it at once.

### Gaugamela (331 BC)

*Hellenistic beat Eastern*

Facing a far larger Persian army, Alexander advanced obliquely to his right; the Persian cavalry followed to outflank him and a gap opened in their line. Alexander led the Companions into the gap straight at Darius, who fled. Scythed chariots were let through lanes and killed by javelinmen.

Lessons:
- An oblique advance drags the enemy line sideways and opens gaps: strike into the gap at the enemy general.
- Against a bigger army, kill or rout the commander and the army dissolves.

### Issus (333 BC)

*Hellenistic beat Eastern*

Darius fought on a narrow coastal plain where his huge army could not deploy. Alexander charged across the river with his cavalry straight at the Persian left and the king himself; Darius fled and his army collapsed.

Lessons:
- A smaller army fights where the front is narrow; numbers cannot be used there.
- A commander who flees breaks his army: guard your general, and go for theirs.

### Hydaspes (326 BC)

*Hellenistic beat Eastern*

Alexander crossed the river by night away from Porus' camp, then faced his war elephants. Light infantry attacked the elephants' drivers and legs and opened lanes, while the cavalry struck the Indian flanks; the maddened elephants trampled both sides.

Lessons:
- Fight elephants with light infantry and missiles, not with a closed line; give them room.
- A river crossing away from the enemy's guard is the way over.

### Jaxartes (329 BC)

*Hellenistic beat Steppe*

Scythian horse archers circled every force sent against them. Alexander sent a bait force of cavalry to draw them in, then pinned them with light infantry and archers and charged them from several sides; catapults covered his crossing.

Lessons:
- Horse archers are caught by bait: draw them in, pin them with missiles and light infantry, then charge from several sides.
- Artillery and archers keep horse archers away from a crossing.

### Leuctra (371 BC)

*Hellenistic beat Hellenistic*

Epaminondas massed his Thebans fifty ranks deep on his left, opposite the Spartan elite, and held his weaker right back. The deep column crushed the Spartan king's men before the rest of the line even met.

Lessons:
- Concentrate overwhelming depth against the enemy's best point and refuse the rest of your line.
- When his best units break, the whole enemy army loses heart.

### Ipsus (301 BC)

*Hellenistic beat Hellenistic*

Demetrius' cavalry routed the enemy horse but chased it far away; Seleucus' elephants then blocked his way back, and the abandoned phalanx of Antigonus was surrounded, and Antigonus himself was killed.

Lessons:
- Cavalry that pursues too far leaves the infantry alone; bring it back.
- Elephants can be used as a wall to cut off enemy cavalry from the battle.

### Raphia (217 BC)

*Egyptian beat Hellenistic*

Antiochus III won on his right and chased the beaten Egyptians away, but Ptolemy IV rode to his own phalanx in the centre, reinforced with native Egyptian troops, and it broke the Seleucid centre. The battle was lost for Antiochus while he was still pursuing.

Lessons:
- Winning one wing does not win the battle: the centre decides.
- A general who rides off in pursuit cannot command the rest of his army.

### Lysimachia (277 BC)

*Hellenistic beat Barbarian*

Antigonus Gonatas left his camp seemingly abandoned; the Gauls rushed in to plunder it and were caught there by his hidden army and destroyed.

Lessons:
- Barbarians who scatter to plunder or chase are easy prey for a hidden, formed force.
- Keep your army together; do not break formation for easy targets.

### Delphi (279 BC)

*Hellenistic beat Barbarian*

Brennus' Gauls marched on Delphi, but the Greek defenders used the steep slopes, rocks and bad weather, attacking from above and from the flanks until the Gauls fell back.

Lessons:
- Defending against a fierce mass of infantry: use the slopes and strike from above and from the sides.

### Crimisus (341 BC)

*Hellenistic beat Punic*

Timoleon's Greeks attacked the Carthaginians while they were crossing a river; a storm drove rain into the Carthaginians' faces and their heavily armoured Sacred Band was bogged down in the mud.

Lessons:
- Attack an army while it crosses a river: only part of it can fight.

### The Saw (238 BC)

*Punic beat Barbarian*

Hamilcar Barca trapped the rebel mercenary army in a gorge called the Saw, cut it off from food and water, and destroyed it.

Lessons:
- Trap a mass of warriors in a narrow place they cannot escape from.

### Cyrus against the Massagetae (530 BC)

*Steppe beat Eastern*

Cyrus lured a Massagetae force into a camp full of wine and destroyed it; Queen Tomyris then drew his army deep into the steppe and destroyed it in turn, and Cyrus himself was killed.

Lessons:
- Steppe armies lure their enemies deep and strike when they are spread out: do not follow them far.
- A bait works both ways: an enemy that takes your bait can be destroyed.

### Kadesh (1274 BC)

*Egyptian draw with Eastern*

Hittite chariots struck one Egyptian division on the march and broke it, then attacked the pharaoh's camp. Ramesses II counter-attacked with his guard, the Hittites stopped to plunder, and Egyptian reinforcements hit them; neither side won outright.

Lessons:
- An army strung out on the march can be broken piece by piece; keep it together.
- Attackers who stop to plunder are open to a counter-attack.

### Megiddo (1457 BC)

*Egyptian beat Eastern*

Thutmose III led his army through a narrow pass the enemy thought nobody would use and attacked at dawn; the Canaanite coalition broke at once. But his men stopped to plunder the enemy camp, and the enemy escaped into the city.

Lessons:
- Strike from the direction the enemy does not expect, before he is formed.
- Do not stop to plunder: pursue until the enemy army is destroyed.
