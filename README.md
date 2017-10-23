
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

Inspired by tri-stat rules

ATTRIBUTES:

Body: a measure of the character's physical prowess and health.
Mind: a measure of the character's mental capacity and intelligence.
Soul: a measure of the character's spirit and willpower.


DERIVED ATTRIBUTES:

Attack Combat Value: (ACV) [(Body + Mind + Soul) / 3] which is the focus of all the character's Stats to determine their bonus to Hit an opponent during combat scenes.
Defense Combat Value: (DCV) [(Body + Mind + Soul) / 3 - 2] which is the character's ability to react against incoming attacks.
Health Points: [(Body + Soul) × 5] which is the amount of damage a character can withstand before they are knocked unconscious or killed. These are similar to hit points in other games.
Energy Points: [(Mind + Soul) × 5] an optional Stat used for fueling certain superpower Attributes. When a character runs out of Energy Points, they can no longer use that power.

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
