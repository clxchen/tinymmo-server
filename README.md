
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
* HP - Health Points
* MP - Magic Points

#### Abilities:

- Spells
* Incinerate (damage to target at range)
* Heal Wounds (restore HP to target)
* Ice Shield (armor bonus to target for next minute)
* Snake Bite (damage plus hit penalty to target at range for next minute)
* Earth Spikes (damage plus armor penalty to target at range for next minute)
* Ice Spikes (damage plus armor penalty to target at range for next minute)
* Tornado (damage plus dam penalty to target for next minute)
* Tentacles (damage multiple targets plus hit pentalty at range for next minute)
* Water Tentacle (damage multiple targets plus dam penalty at range for next minute)
* Ice Tentacle (damage multiple targets plus armor penalty at range for next minute)

