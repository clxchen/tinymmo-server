
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

Required level, ability title, description, effects

1 Incinerate (damage to target at range)
2 Heal Wounds (restore HP to target)
4 Ice Shield (armor bonus to target for next minute)
6 Snake Bite (damage plus hit penalty to target at range for next minute)
8 Spikes (damage plus armor penalty to target at range for next minute)
10 Tornado (damage plus dam penalty to target for next minute)
12 Tentacles (damage multiple targets plus hit pentalty at range for next minute)
14 Water Tentacle (damage multiple targets plus dam penalty at range for next minute)
16 Ice Tentacle (damage multiple targets plus armor penalty at range for next minute)


