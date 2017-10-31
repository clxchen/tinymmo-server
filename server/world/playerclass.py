from twisted.python import log
import ConfigParser

def load_playerclasses(world):

  config = ConfigParser.RawConfigParser()
  config.read('server_data/classes.ini')

  for playerclass in config.sections():
    title  = config.get(playerclass,'title')
    hp_rate  = config.getfloat(playerclass,'hp_rate')
    mp_rate  = config.getfloat(playerclass,'mp_rate')
    hit_bonus  = config.getint(playerclass,'hit_bonus')
    arm_bonus  = config.getint(playerclass,'arm_bonus')
    dam_bonus  = config.getint(playerclass,'dam_bonus')
    spi_bonus  = config.getint(playerclass,'spi_bonus')
    armor_allowed = config.get(playerclass, 'armor_allowed').split(',')
    weapons_allowed = config.get(playerclass, 'weapons_allowed').split(',')
    abilities  = config.get(playerclass,'abilities').split(',')
    sword_bonus = config.getfloat(playerclass, 'sword_bonus')
    spear_bonus = config.getfloat(playerclass, 'spear_bonus')
    wand_bonus = config.getfloat(playerclass, 'wand_bonus')
    staff_bonus = config.getfloat(playerclass, 'staff_bonus')
    bow_bonus = config.getfloat(playerclass, 'bow_bonus')
    
    world.playerclasses[playerclass] = PlayerClass(playerclass,title,hp_rate,mp_rate,abilities,hit_bonus,arm_bonus,dam_bonus,spi_bonus,weapons_allowed, armor_allowed, sword_bonus, spear_bonus, wand_bonus,staff_bonus,bow_bonus)  

class PlayerClass:

  def __init__(self, name, title, hp_rate, mp_rate, abilities, hit_bonus, arm_bonus, dam_bonus, spi_bonus, weapons_allowed, armor_allowed, sword_bonus, spear_bonus, wand_bonus, staff_bonus, bow_bonus):
    '''
    Store information on player classes
    '''

    self.name = name
    self.title = title
    self.mp_rate = mp_rate
    self.hp_rate = hp_rate
    self.abilities = abilities
    self.hit_bonus = hit_bonus
    self.arm_bonus = arm_bonus
    self.dam_bonus = dam_bonus
    self.spi_bonus = spi_bonus
    self.weapons_allowed = weapons_allowed
    self.armor_allowed = armor_allowed
    self.sword_bonus = sword_bonus
    self.spear_bonus = spear_bonus
    self.wand_bonus = wand_bonus
    self.staff_bonus = staff_bonus
    self.bow_bonus = bow_bonus

  
