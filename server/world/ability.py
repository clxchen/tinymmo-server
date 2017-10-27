from twisted.internet import reactor
from twisted.python import log
import ConfigParser

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
    target_hit = config.getint(ability,'target_hit')
    target_dam = config.getint(ability,'target_dam')
    target_arm = config.getint(ability,'target_arm')
    target_spi = config.getint(ability,'target_spi')
    actor_hit = config.getint(ability,'actor_hit')
    actor_dam = config.getint(ability,'actor_dam')
    actor_arm = config.getint(ability,'actor_arm')
    actor_spi = config.getint(ability,'actor_spi')
    description = config.get(ability,'description')
    mana_cost = config.getint(ability,'mana_cost')
    summon = config.get(ability,'summon').split(',')

    
    world.abilities[ability] = Ability(ability, title, icon, duration, cooldown, cast_time, animation, rng, damage, heal, level, target_hit, target_dam, target_arm, target_spi, actor_hit, actor_dam, actor_arm, actor_spi, description, mana_cost, summon, world)  


class Ability:

  def __init__(self, name, title, icon, duration, cooldown, cast_time, animation, rng, damage, heal, level, target_hit, target_dam, target_arm, target_spi, actor_hit, actor_dam, actor_arm, actor_spi, description, mana_cost, summon, world):
    
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
    self.target_hit = target_hit
    self.target_dam = target_dam
    self.target_arm = target_arm
    self.target_spi = target_spi
    self.actor_hit = actor_hit
    self.actor_dam = actor_dam
    self.actor_arm = actor_arm
    self.actor_spi = actor_spi
    self.summon = summon
    self.world = world

    log.msg( "Loaded ABILITY %s" % self.name )

  def activate(self, actor, target):
    
    # Start cast animation
    self.world.events.append({'type': 'playercast', 'name': actor.name, 'cast_time': self.cast_time, 'zone': actor.zone })
    
    # Stop if we don't have enough mp
    if not self.mana_cost < actor.mp[0]:
      return
    
    # can only buff or heal a player
    if target.__class__.__name__ == 'Player':
      if self.target_dam < 0 or self.damage > 0 or self.target_hit < 0 or self.target_arm < 0 or self.target_spi < 0:
        print "Cant do that to a player"
        return

    # can only debuff or damage a monster
    if target.__class__.__name__ == 'Monster':
      if self.target_dam > 0 or self.heal > 0 or self.target_hit > 0 or self.target_arm > 0 or self.target_spi > 0:
        print "Cant do that to a monster"
        return
    
    # can only debuff or damage an npc if it's a villan
    if target.__class__.__name__ == 'Npc':
      if not target.villan:
        print "Cant do that to a friendly npc"
        return
      if self.target_dam > 0 or self.heal > 0 or self.target_hit > 0 or self.target_arm > 0 or self.target_spi > 0:
        print "Cant do that to a villan npc"
        return
    
    # Do we have enough mana
    if actor.mp[0] < self.mana_cost:
      return
   
    if self.name in actor.abilities_in_cooldown.keys():
      log.msg("in cooldown")
      return

    reactor.callLater(self.cast_time, self.apply_effects, actor, target)
  
  def apply_effects(self, actor, target):

    # Stuff that happens when this ability is activated. Add 'effect'
    # event in event queue
    actor.mp[0] -= self.mana_cost
    self.world.events.append({'type': 'playermpused', 'name': actor.name, 'used': self.mana_cost, 'mp': actor.mp, 'zone': actor.zone })
    
    self.world.events.append({'type': 'addeffect', 'name': self.animation, 'target': target.name, 'duration': self.duration, 'animation': self.animation, 'zone': target.zone })

    # Add effets on actor to active effects table
    effects_on_actor  = { 'hit': self.actor_hit,
                          'dam': self.actor_dam,
                          'spi': self.actor_spi,
                          'arm': self.actor_arm, }
   
    name = "%s-%s" % (actor.name,self.name)
    actor.active_effects[name] = effects_on_actor

    reactor.callLater(self.duration, self.cleanup, actor, name)

    # set target's target to actor if bad things done to target
    if self.target_hit < 0 or self.target_dam < 0 or self.target_arm < 0 or self.target_spi < 0:
      target.target = actor

    if self.damage > 0:
      target.take_damage(actor, self.damage)

    if self.heal > 0:
      target.heal(self.heal)

    # Add effects on target to active effects table
    effects_on_target = { 'hit': self.target_hit,
                          'dam': self.target_dam,
                          'spi': self.target_spi,
                          'arm': self.target_arm, }
   
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
