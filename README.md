
Tinymmo-python is a very small, 'Minorly mulitplayer online role playing game'. Developed so that I may better understan python network game programming.

This game uses works from https://opengameart.org/.

Requires python 2.7

Tested on Mac OSX 10+


## Setup using virtual environment:

```
git clone https://github.com/dslice25/tinymmo-server.git
cd tinymmo-server
virtualenv pyenv
source pyenv/bin/activate
pip install twisted pytmx pyglet
```

### Quickstart:

After setting up in a virtual environment you should be able to run the server and client. By default server listens on localhost:10000.

```
source pyenv/bin/activate
python game_server.py
```

### The World

 TODO

### Mechanics

#### Stats:

* HIT - Chance to hit
* DAM - Damage done on hit
* ARM - Defensive statistic
* SPI - Mental Prowess
* HP - Health Points
* MP - Magic Points

#### Classes:

Fighter:
- Straight up Melee Fighter
- Wear any armor
- Wield any weapon except wands
- +1 HIT
- +1 HIT with swords and spears
- +3 HP/level, +0 MP/level
- No Spells

Mage:
- Powerfull spell caster
- Wear no armor
- Wield staff or wand
- +1 SPI
- +1 HIT with wands and staves
- +1 HP/level, +2 MP/level
- Spells
* 1 Fire Lion ([level * 1d4] damage to target at range)
* 2 Ice Shield ([level * 2] ARM bonus to target for next minute)
* 4 Snake Bite ([level * 1d4] damage plus [level/2] SPI penalty to target at range for next minute)
* 6 Tornado ([level * 1d4] damage plus [level/2] DAM penalty to target for next minute)
* 8 Earth Spikes ([level * 1d6] damage plus [level/2] ARM penalty to target at range for next minute)
* 10 Ice Spikes ([level * 1d8] damage plus [level/2] HIT penalty to target at range for next minute)
* 12 Water Tentacle ([level * 1d4] damage multiple targets)
* 14 Ice Tentacle ([level * 1d6] damage multiple targets)
* 16 Lightning Claw ([level * 1d8] damage multiple targets)

Cleric:
- Healer, fighter
- Wear cloth, leather or chain armor
- Wield any weapon except wand
- +1 ARM
- +1 HIT with swords and spears
- +2 HP/level, +1 MP/level
- Spells
* 2 Heal Wounds (restore [level * 1d4] HP to target)
* 4 Turn Undead ([level * 1d4] damage to undead creatures)
* 8 Heal Allies (restore [level * 1d4] HP to nearby allies)

Ranger:
- Ranged figher
- Wear clother or leather armor
- Wield any weapon except wand
- +1 DAM
- +2 HIT with bows
- +2 HP/level, +1 MP/level
- Spells:
* 4 Summon Bee (Summon bee to fight along side you [1d4 damage, 1 ARM/DAM/HIT/SPI])
* 8 Summon Bat (Summon a bat to fight along side you [1d6 damage, 2 ARM/DAM/HIT/SPI])
* 16 Summon Snake (Summon a snake to fight along side you [1d8 damage, 3 ARM/DAM/HIT/SPI])


