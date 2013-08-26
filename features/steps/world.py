from lettuce import world
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("features/config.ini")
world.config = Config
assert world.config.get('bitly', 'host') is not None
assert world.config.get('geonames', 'host') is not None
world.provider = None

@world.absorb
def cfg(name, provider=None):
  if provider is None:
    provider = world.provider
  return world.config.get(provider, name) 
