import ConfigParser
from twisted.python import log

def load_accounts(world):

  pconfig = ConfigParser.RawConfigParser()
  pconfig.read('server_data/accounts.ini')
  
  for name in pconfig.sections():
    password = pconfig.get(name, 'password')

    world.accounts[name] = Account(name,password)

class Account:

  def __init__(self, username, password):

    self.username = username
    self.password = password
    self.online = False

    log.msg( "Loaded ACCOUNT %s" % self.username )
