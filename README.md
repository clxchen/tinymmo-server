
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

### Stats system:


#### Stats:

* HIT - Chance to hit target with a weapon. Derived from equipment.
* DAM - Damage done by a weapon. Derived from equipment.
* ARM - Armor granted by equipment. Derived from equipment.
* HP - Health Points. 10 + Level * 1.5
* EP - Energy Points 10 + Level * 1.5


#### Abilities:

All abilities avaliable to all classes. Purchased at a appropriate trainer using Character points. Effectiveness of abilitiy increased by spending more points on it. Points earned at 1 per level. Abilities include spells and other special attacks. Some abilities require the player to be at a certain level.

* Magic Tree:
- Fireball (damage to target at range)
- Ice Shield (armor bonus to target for next minute)
- Snake Bite (damage at range plus hit pentalty to target at range for next minute)
- Spikes (damage plus armor penalty to target at range for next minute)
- Tornado (damage plus dam penalty to target for next minute)
- Tentacles (damage multiple targets plus hit pentalty at range for next minute)
- Water Tentacle (damage multiple targets plus dam penalty at range for next minute)
- Ice Tentacle (damage multiple targets plus armor penalty at range for next minute)
* Combat Tree:
- Concussing Shot (hit penalty to target for next minute)
- Disarm (damage penalty to target for next minute)
- Find Weakness (armor penalty to target for next minute)
- Multi-Shot (damage to multiple targets with bow)
- Aggresive Stance (extra damage at cost of armor for next minute)
- Defensive Stance (extra armor at cost of damage for next minute)
- Patience Stance (extra hit at cost of damage for next minute)
* Wilderness Tree:
- Heal Wounds (restore target health at range)
- Summon Bee (summon a bee to fight along sight the player for one minute)
- Summon Bat (summon a bat to fight along side the player for one minute) 
- Summon Snake (summon a snake to fight along side the player for one minute) 
- Heal Allies (restore health to multiple targets in range)


