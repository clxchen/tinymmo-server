from twisted.internet import reactor, protocol, endpoints, task
from twisted.protocols import basic
from twisted.python import log

import json
import uuid

class GameProtocol(basic.LineReceiver):
    def __init__(self, factory):
      self.factory = factory
      self.player_name = None
      self.authenticated = False
      self.is_playing = False
      self.username = None
      self.last_event = len(self.factory.world.events)
      self.events_task = task.LoopingCall(self.sendevents)

    def connectionMade(self):
      log.msg( "Connection made" )
      self.factory.clients.add(self)

    def connectionLost(self, reason):
      log.msg( "Connection lost" )
      self.authenticated = False
      
      if self.username:
        self.factory.world.accounts[self.username].online = False
      
      if self.player_name: 
        self.factory.world.player_leave(self.player_name)
        self.events_task.stop()

      self.factory.clients.remove(self)

    def prepare(self, data):
      '''
      Take raw data and prep for sending by converting it to json.
      '''
      final = ""

      try:
        final = json.dumps(data)
      except:
        final = ""
      return final + "\r\n"

    def unpack(self, data):
      '''
      Take recieved data unpack it for usage.
      '''
      final = None

      try:
        final = json.loads(data)
      except Exception as err:
        print err
        final = None

      return final

    def lineReceived(self, line):
      if self.is_playing:
        self.playing(line)
      
      elif self.authenticated:
        self.lobby(line)

      else:
        self.login(line)
    
    def login(self, line):
      data = self.unpack(line)
      
      self.username = data['username']

      if not self.factory.world.accounts.has_key(self.username):
        print "no such username %s" % self.username
        return

      if self.factory.world.accounts[self.username].online:
        print "%s is already online" % self.username
        return

      if self.factory.world.accounts[self.username].password != data['password']:
        print "password mismatch"
        return

      self.authenticated = True
      self.factory.world.accounts[self.username].online = True
      characters = {}
      for name,char in self.factory.world.players.items():
        if char.account == self.username:
          characters[name] = { 'title': char.title, 'name': char.name }

      classes = {}
      for name,pc in self.factory.world.playerclasses.items():
        classes[name] = { 'title': pc.title, 'name': pc.name }

      self.transport.write(self.prepare({"type": "playeroptions", "characters": characters, "classes": classes }))

    def lobby(self, line):
      # Create a new player
      data = self.unpack(line)

      if data:
        
        if data['action'] == 'chooseplayer':
          
          name = data['name']
          
          if not self.factory.world.players.has_key(name):
            return

          if self.factory.world.players[name].online:
            return
          
          if not self.factory.world.players[name].account == self.username:
            return

          # Ok, all checks out:
          self.factory.world.players[name].online = True
          self.player_name = name
          self.transport.write(self.prepare({"type": "entergame"}))
          self.is_playing = True
          self.events_task.start(0.1)

        elif data['action'] == 'createplayer':
          
          gender = data['gender'].lower()
          hairstyle = data['hairstyle'].lower()
          haircolor = data['haircolor'].lower()
          playerclass = data['playerclass'].lower()
          self.player_name = self.factory.world.create_player(data['name'], gender, hairstyle, haircolor, playerclass, self.username)
          self.transport.write(self.prepare({"type": "entergame"}))
          self.is_playing = True
             
          # Start sending events
          self.events_task.start(0.1)

    def playing(self, line): 
      data = self.unpack(line)

      # Process data
      if data:
        
        if data['action'] == 'leave':
          self.is_playing = False
        
        else:

          send_now = self.factory.world.process_data(self.player_name, data)

          # Send any additional data to client
          if send_now:
            self.transport.write(self.prepare(send_now))

    # Send all game events since last event 
    def sendevents(self):
      if self.authenticated and self.player_name:
        events = self.factory.world.get_events(self.player_name, self.last_event)
        if not events['events']:
          return
        events_data = self.prepare(events)
        if events_data:
          self.transport.write(events_data)
          self.last_event = len(self.factory.world.events)
      


class GameFactory(protocol.Factory):
  
  def __init__(self, world):
    self.world = world
    self.clients = set()


  def buildProtocol(self, addr):
    return GameProtocol(self)


