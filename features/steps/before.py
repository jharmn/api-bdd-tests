from lettuce import *
import ConfigParser

@before.all
def load_config():
  Config = ConfigParser.ConfigParser()
  Config.read("features/config.ini")
  world.config = Config
  assert world.config.get('geonames', 'host') is not None
