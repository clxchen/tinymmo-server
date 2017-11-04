from twisted.internet import reactor, protocol, endpoints, task
from twisted.protocols import basic
from twisted.python import log

import json

PLAYER_ACTION_TIME = 1.0 # seconds it takes to perform an action
MONSTER_ACTION_TIME = 2.0 # seconds it takes to perform an action
TICK_RATE = 60 # seconds between keepalive ticks

class GameProtocol(basic.LineReceiver):
    def __init__(self, factory):
      self.factory = factory
      self.player_name = None
      self.authenticated = False
      self.last_event = len(self.factory.world.events)
      self.events_task = task.LoopingCall(self.sendevents)

    def connectionMade(self):
      log.msg( "Connection made" )
      self.factory.clients.add(self)
      self.transport.write(self.prepare({"type": "playeroptions"}))

    def connectionLost(self, reason):
      log.msg( "Connection lost" )
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
      if self.authenticated:
        self.playing(line)

      else:
        self.login(line)

    def login(self, line):
      # Create a new player
      data = self.unpack(line)

      if data:

        if data['action'] == 'createplayer':
          gender = data['gender'].lower()
          hairstyle = data['hairstyle'].lower()
          haircolor = data['haircolor'].lower()
          playerclass = data['playerclass'].lower()
          self.player_name = self.factory.world.create_player(data['name'], gender, hairstyle, haircolor, playerclass)
          self.transport.write(self.prepare({"type": "loginsucceeded"}))
          self.authenticated = True
          
          # Start sending events
          self.events_task.start(0.1)

    def playing(self, line): 
      data = self.unpack(line)

      # Process data
      if data:
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


