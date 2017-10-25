from twisted.internet import reactor
import ConfigParser

def load_abilities(world):

  config = ConfigParser.RawConfigParser()
  config.read('server_data/abilities.ini')

  abilities = []
  
  for ability in config.sections():
    title       = config.get(ability,'title')
    description = config.get(ability,'description')
    duration = config.get(ability,'duration')
    cast_time = config.get(ability,'cast_time')
    animation = config.get(ability,'animation')
    rng = config.get(ability,'rng')
    level = config.get(ability,'level')
    target_hp = config.get(ability,'target_hp')
    target_mp = config.get(ability,'target_mp')
    target_hit = config.get(ability,'target_hit')
    target_dam = config.get(ability,'target_dam')
    target_arm = config.get(ability,'target_arm')
    actor_hp = config.get(ability,'actor_hp')
    actor_mp = config.get(ability,'actor_mp')
    actor_hit = config.get(ability,'actor_hit')
    actor_dam = config.get(ability,'actor_dam')
    actor_arm = config.get(ability,'actor_arm')
    description = config.get(ability,'description')
    mana_cost = config.get(ability,'mana_cost')

    
    world.abilities[ability] = Ability(ability, title, duration, cast_time, animation, rng, level, target_hp, target_mp, target_hit, target_dam, target_arm, actor_hp, actor_mp, actor_hit, actor_dam, actor_arm, description, mana_cost, world)  


class Ability:

  def __init__(self, name, title, duration, cast_time, animation, rng, level, target_hp, target_mp, target_hit, target_dam, target_arm, actor_hp, actor_mp, actor_hit, actor_dam, actor_arm, description, mana_cost, world):
    
    self.name = name
    self.title = title
    self.duration = duration
    self.cast_time = cast_time
    self.animation = animation
    self.mana_cost = mana_cost
    self.description = description
    self.rng = rng
    self.level = level
    self.target_hp = target_hp
    self.target_mp = target_mp
    self.target_hit = target_hit
    self.target_dam = target_dam
    self.target_arm = target_arm
    self.actor_hp = actor_hp
    self.actor_mp = actor_mp
    self.actor_hit = actor_hit
    self.actor_dam = actor_dam
    self.actor_arm = actor_arm
    self.world = world

    self.active_index = 0

  def activate(self, actor, target):
    
    # Stuff that happens before the ability is applied. Add 'playercast'
    # or 'npccast' event to event queue
    self.world.events.append({'type': 'playercast', 'name': actor.name, 'cast_time': self.cast_time })
    
    reactor.callLater(cast_time, self.apply_effects, actor, target)
  
  def apply_effects(self, actor, target):

    # Stuff that happens when this ability is activated. Add 'effect'
    # event in event queue

    # Apply damage
    # Apply buffs/debuffs
    # Apply MP cost to actor
    
    self.world.events.append({'type': 'effect', 'name': self.animation, 'target': target.name, 'duration': self.duration })

    # set target's target to actor if bad things done to target
    if self.target_hp < 0 or self.target_mp < 0 or self.target_hit < 0 or self.target_dam < 0 or self.target_arm < 0:
      target.target = actor

    # Update target hp/mp
    target.hp[0] += self.target_hp
    if actor.hp[0] > actor.hp[1]:
      actor.hp[0] = actor.hp[1]

    target.mp[0] += self.target_mp

    # Add effects on target to active effects table
    effects_on_target = { 'target': target.name,
                          'target_hit': self.target_hit,
                          'target_dam': self.target_dam,
                          'target_arm': self.target_arm, }
   
    name = "%s-%s" % (self.name, self.active_index)
    self.active_index += 1
    self.server.world.active_effects[name] = effects_on_target
    
    reactor.callLater(duration, self.cleanup, name)

    
    # update actor hp/mp
    actor.hp[0] += self.actor_hp
    if actor.hp[0] > actor.hp[1]:
      actor.hp[0] = actor.hp[1]

    actor.mp[0] += self.actor_mp

    # Add effets on actor to active effects table
    effects_on_actor  = { 'target': target.name,
                          'target_hit': self.target_hit,
                          'target_dam': self.target_dam,
                          'target_arm': self.target_arm, }
   
    name = "%s-%s" % (self.name, self.active_index)
    self.active_index += 1
    self.server.world.active_effects[name] = effects_on_actor

    reactor.callLater(duration, self.cleanup, name)

  def cleanup(self, name):
    
    del self.world.active_effects[name]

