from lettuce import *

@before.all
def clear_world_state():
  world.params = {}
  world.auth = None
  world.values = {}
