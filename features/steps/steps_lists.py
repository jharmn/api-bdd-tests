from lettuce import *
import requests
from nose.tools import *

@step(u'it should have a list "([^"]*)"')
def should_have_a_list_of_results(step, name):
  assert world.results_json.has_key(name)
  world.list = world.results_json[name]

@step(u'the list should have at least (\d+) items')
def the_list_should_have_at_least_x_item_in_list(step, num):
  assert world.list is not None
  assert len(world.list) >= int(num)

@step(u'the list should have the field "([^"]*)" containing the value "([^"]*)"')
def the_list_should_have_the_field_containing_the_value(step, field, value):
  eq_(world.list[0][field], value)
