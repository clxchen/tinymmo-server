from twisted.internet import reactor, protocol, endpoints, task
from world.game import Game
from net import GameFactory

from twisted.python.filepath import FilePath
from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess, FilePasswordDB
from twisted.internet import reactor
from twisted.python import log

import os,sys


def start():

  log.startLogging(sys.stdout)

  game = Game()
  
  # Game event server
  endpoints.serverFromString(reactor, "tcp:10000").listen(GameFactory(game))
  loop = task.LoopingCall(game.loop)
  loop.start(0.05)

  # Game data server
  client_resources = '/tmp/pub/'
  p = Portal( FTPRealm(client_resources), [AllowAnonymousAccess()])
  f = FTPFactory(p)
  reactor.listenTCP(10001, f)

  reactor.run()
