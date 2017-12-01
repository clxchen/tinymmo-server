from twisted.internet import reactor
from twisted.python import log
import ConfigParser
import random

def load_abilities(world):

  config = ConfigParser.RawConfigParser()
  config.read('server_data/abilities.ini')

  for ability in config.sections():
    title       = config.get(ability,'title')
    icon = config.get(ability, 'icon')
    description = config.get(ability,'description')
    duration = config.getint(ability,'duration')
    cooldown = config.getint(ability,'cooldown')
    cast_time = config.getint(ability,'cast_time')
    animation = config.get(ability,'animation')
    rng = config.getint(ability,'rng')
    damage = config.getint(ability,'damage')
    heal = config.getint(ability,'heal')
    level = config.getint(ability,'level')
    hit = config.getint(ability,'hit')
    dam = config.getint(ability,'dam')
    arm = config.getint(ability,'arm')
    spi = config.getint(ability,'spi')
    description = config.get(ability,'description')
    mana_cost = config.getint(ability,'mana_cost')
    summon = config.get(ability,'summon').split(',')

    
    world.abilities[ability] = Ability(ability, title, icon, duration, cooldown, cast_time, animation, rng, damage, heal, level, hit, dam, arm, spi, description, mana_cost, summon, world)  


class Ability:

  def __init__(self, name, title, icon, duration, cooldown, cast_time, animation, rng, damage, heal, level, hit, dam, arm, spi, description, mana_cost, summon, world):
    
    self.name = name
    self.title = title
    self.icon = icon
    self.duration = duration
    self.cooldown = cooldown
    self.cast_time = cast_time
    self.animation = animation
    self.mana_cost = mana_cost
    self.description = description
    self.rng = rng
    self.level = level
    self.damage = damage
    self.heal = heal
    self.hit = hit
    self.dam = dam
    self.arm = arm
    self.spi = spi
    self.summon = summon
    self.world = world

    log.msg( "Loaded ABILITY %s" % self.name )

  def activate(self, actor, target):
    
    # Stop if we don't have enough mp
    if not self.mana_cost < actor.mp[0]:
      return
    
    roll_for_hit = True
    roll = 0
    spi_defence = 0
    # Rules:
    # actor must roll 1d20 < 8 + actor.spi

    # can only buff or heal a player
    if actor.__class__.__name__ == 'Player' and target.__class__.__name__ == 'Player':
      if self.dam < 0 or self.damage > 0 or self.hit < 0 or self.arm < 0 or self.spi < 0:
        return {'type': 'message', 'message': "You cannot cast %s on %s!" % (self.title, target.title) }
      else:
        roll_to_hit = False

    # can only debuff or damage a monster
    elif actor.__class__.__name__ == 'Player' and target.__class__.__name__ == 'Monster':
      if self.dam > 0 or self.heal > 0 or self.hit > 0 or self.arm > 0 or self.spi > 0:
        return {'type': 'message', 'message': "You cannot cast %s on %s!" % (self.title, target.title) }
      else:
        roll_to_hit = True
        roll = random.randint(1,20) + self.world.get_player_spi(actor.name)
        spi_defence = 8 + self.world.get_monster_spi(target.name)

    # can only debuff or damage an npc if it's a villan
    elif actor.__class__.__name__ == 'Player' and target.__class__.__name__ == 'Npc':
      if not target.villan:
        return {'type': 'message', 'message': "You cannot cast %s on %s!" % (self.title, target.title) }
      elif self.dam > 0 or self.heal > 0 or self.hit > 0 or self.arm > 0 or self.spi > 0:
        return {'type': 'message', 'message': "You cannot cast %s on %s!" % (self.title, target.title) }
      else:
        roll_to_hit = True
        roll = random.randint(1,20) + self.world.get_player_spi(actor.name)
        spi_defence = 8 + self.world.get_npc_spi(target.name)

    # Do we have enough mana
    if actor.mp[0] < self.mana_cost:
      return {'type': 'message', 'message': "Not enough mana to cast %s" % self.title }
   
    if self.name in actor.abilities_in_cooldown.keys():
      return {'type': 'message', 'message': "You are not ready to cast %s" % self.title }

    # deduct MP
    actor.mp[0] -= self.mana_cost
    self.world.events.append({'type': 'playermpused', 'name': actor.name, 'used': self.mana_cost, 'mp': actor.mp, 'zone': actor.zone })
    
    if roll_to_hit:
      if roll > spi_defence:
        self.world.events.append({'type': 'playercast', 'name': actor.name, 'cast_time': self.cast_time, 'zone': actor.zone, 'hit': True })
        reactor.callLater(self.cast_time, self.apply_effects, actor, target)
      
      else:
        self.world.events.append({'type': 'playercast', 'name': actor.name, 'cast_time': self.cast_time, 'zone': actor.zone, 'hit': False })
        return { 'type': 'message', 'message': "Casting of %s failed. Rolled %s; needed > %s." % (self.title, roll, spi_defence) }

  def apply_effects(self, actor, target):

    # Stuff that happens when this ability is activated. Add 'effect'
    # event in event queue
    self.world.events.append({'type': 'addeffect', 'name': self.animation, 'target': target.name, 'duration': self.duration, 'animation': self.animation, 'zone': target.zone })

    # set target's target to actor if bad things done to target
    if self.hit < 0 or self.dam < 0 or self.arm < 0 or self.spi < 0:
      target.target = actor

    if self.damage > 0:
      target.take_damage(actor, random.randint(self.damage/2, self.damage))

    if self.heal > 0:
      target.heal(random.randint(self.heal/2, self.heal))

    # Add effects on target to active effects table
    effects_on_target = { 'hit': self.hit,
                          'dam': self.dam,
                          'spi': self.spi,
                          'arm': self.arm, }
   
    name = "%s-%s" % (actor.name, self.name)
    target.active_effects[name] = effects_on_target
    
    reactor.callLater(self.duration, self.cleanup, target, name)
   
    # Mark this ability as in cooldown 
    actor.abilities_in_cooldown[self.name] = True
    reactor.callLater(self.cooldown, self.cooldown_expire, actor)

  def cleanup(self, target, name):
    try:
      del target.active_effects[name]
    except:
      log.msg("Could not remove effect %s from %s" % (name, target.name))
    
  def cooldown_expire(self, actor):
    try:
      del actor.abilities_in_cooldown[self.name]
    except:
      log.msg("No cooldown for %s %s" % (self.name, actor.name))
      
  def stats(self):
    
    return { 'name': self.name, 'title': self.title, 'icon': self.icon, 'description': self.description }
