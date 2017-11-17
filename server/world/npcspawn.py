import random
import uuid
import time
import copy
from npc import Npc
from twisted.internet import task
from twisted.python import log
import ConfigParser

class NpcSpawn:


  def __init__(self, name, x, y, w, h, zone, spawn_max, spawn_delay, world):
    
    self.name        = name
    self.x           = x
    self.y           = y
    self.w           = w
    self.h           = h
    self.zone        = zone
    self.spawn_max   = spawn_max
    self.spawn_delay = spawn_delay
    self.world       = world
    self.spawn_count = 0

    # Schedule update task
    self.spawn_task = task.LoopingCall(self.spawn)
    self.spawn_task.start(self.spawn_delay, now=False)
 
    log.msg( "Loaded NPC SPAWN %s" % self.name )

  def spawn(self):

    if self.spawn_count < self.spawn_max:
      x = random.randint(self.x, self.x + self.w)
      y = random.randint(self.y, self.y + self.h)
      
      # Create npc
      Npc(self.name, x, y, self.zone, self.world, self)
      
      self.spawn_count += 1
  
