
from lettuce import *
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
world.config = Config
assert world.config.get('bitly', 'host') is not None
assert world.config.get('geonames', 'host') is not None
world.provider = None

@world.absorb
def cfg(name, provider=None):
  if provider is None:
    provider = world.provider
  assert provider is not None
  return world.config.get(provider, name) 

@before.all
def clear_world_state():
  world.params = {}
  world.auth = None
  world.values = {}
