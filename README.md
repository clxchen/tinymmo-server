
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

### Class/Attribute system:

Strength - Governs hit with melee weapons, damage with range and melee weapons
Speed - Governs hit with range weapons, small influence on armor class
Intellect - Governs Magic use and hit with wands


Ability trees:

Fighter:
 - Battlefield Abilities:  utility abilities
 - * "Battle Hardened" - Percent bonus to HP
 - Arms Abilities: Skills with melee weapons
 - * "Swords" - Bonus to slash damage
 - * "Spears" - Bonus to thrust damage
 - * "Tactician" - Bonus to hit chance
 - * "Repost" - Next hit will do +50% damage. Use once a minute.
 - * "Rampage" - Damage all targets in area.
 - Armor Abilities: Skills with armors
 - * "Battle Tested" - Percent bonus to armor


Ranger:
 - Fieldsman Abilities: Some healing, bonuses to self and party
 - Marksman Abilities: Skills with range weapons
 - Wildlife Abilities: Skills with monsters (summon a monster to fight along side?)

Mage:
 - Life Magic: Strong healing magic, bonuses to self and party
 - * "Heal Wounds" - Heal single target
 - * "Health Fountain" - Heal all players in area
 - Death Magic: Combat magic, summon skeleton to help fight?
 - * "Curse" - HP and MP draining spell
 - Elemental Magic: Fireballs, ice bolts and other fun stuff (summon elemental to fight alon side?)
