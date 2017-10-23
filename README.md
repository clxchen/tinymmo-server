
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

The game ships with a very simple world, consisting of the town of Stuck and surrounding territory. 

## Worldbuilding

 TODO

## Notes:

### Attribute system:

* HIT - Chance to hit target with a weapon. Derived from equipment.
* DAM - Damage done by a weapon. Derived from equipment.
* ARM - Armor granted by equipment. Derived from equipment.
* HP - Health Points. 10 + Level * 1.5
* EP - Energy Points 10 + Level * 1.5

### Class Abilities:

Each ability costs more points to buy than the last. Get one point per level.

* Fighter:
- Class bonus: +25% damage with swords and spears, +20% HP
- Aggresive Stance (bonus to damage next minute)
- Defensive Stance (bonus to armor next minute)
- Patient Stance (bonus to hit for next minute)
- 
-
- 
- 
-

* Mage:
- Class bonus: +25% damage with wands, +20% EP
- Fireball (damage to target at range)
- Ice Shield (armor bonus to target for next minute)
- Snake Bite (damage at range plus hit pentalty to target at range for next minute)
- Spikes (damage plus armor penalty to target at range for next minute)
- Tornado (damage plus dam penalty to target for next minute)
- Tentacles (damage multiple targets plus hit pentalty at range for next minute)
- Water Tentacle (damage multiple targets plus dam penalty at range for next minute)
- Ice Tentacle (damage multiple targets plus armor penalty at range for next minute)

* Ranger:
- Class bonus: +25% damage with bows, +10% HP, +10% EP
- Aim Well (extra hit for next minute)
- Concussing Shot (hit penalty to target for next minute)
- Disarm (damage penalty to target for next minute)
- Find Weakness (armor penalty to target)  
- Summon Bat (summon a bat to fight along side the player for one minute) 
- Summon Snake (summon a snake to fight along sight the player for one minute)
- Summon ____
- Multi-Shot (damage to multiple targets at range)

* Cleric:
* Class Bonus: +25% damage with staffs, +10% HP, + 10% EP
- Heal Wounds (restore target health at range)
-
-
-
-
-
-
- Heal Allies (restore health to multiple targets in range)


