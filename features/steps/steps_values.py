from lettuce import *
import requests 
from requests.auth import HTTPBasicAuth
from nose.tools import *

@step(u'it should have the error "(.*)" containing the value "(.*)"')
def it_should_have_the_error(step, error, value):
  eq_(world.results_json.has_key('status'), True)
  eq_(world.results_json['status']['message'], value)

@step(u'it should have the field "([^"]*)" containing the value "([^"]*)"')
def it_should_have_the_field_containing_the_string(step, field, value):
  eq_(world.results_json[field], value)

@step(u'it should have the field "([^"]*)" containing the value (\d*)')
def it_should_have_the_field_containing_the_int(step, field, value):
  eq_(world.results_json[field], int(value))

@step(u'the results should be saved as "(.*)" for later')
def the_results_should_be_saved(step, name):
  world.values[name] = world.results.text

@step(u'the value "(.*)" should be "(.*)"')
def value_should_be(step, name, value):
  eq_(world.values[name], value)

@step(u'the value "(.*)" should not be empty')
def value_should_not_be_empty(step, name):
  assert world.values[name] is not None
