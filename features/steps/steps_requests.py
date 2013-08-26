from lettuce import *
import requests
from requests.auth import HTTPBasicAuth
from nose.tools import *

@step(u'I use the (.*) host')
def use_the_host(step, provider):
  world.provider = provider
  world.host = world.config.get(provider, 'host')

@step(u'I access the resource url "(.*)"')
def access_the_resource_url(step, base_url):
  world.base_url = base_url

@step(u'I provide authentication credentials')
def provide_authorization_credentials(step):
  username = world.config.get(world.provider, "username")
  assert username is not None
  password = world.config.get(world.provider, "password")
  assert password is not None
  world.auth = HTTPBasicAuth(username, password)

@step(u'I provide parameter "(.*)" as "(.*)"')
def query_param_string(step, param, value):
  world.params[param] = value

@step(u'I provide parameter "(.*)" as the value "(.*)"')
def query_param_string(step, param, value):
  world.params[param] = world.values[value]

@step(u'I retrieve the JSON results')
def retrieve_json_results(step):
  retrieve_results(step)
  world.results_json = world.results.json()

@step(u'I retrieve the results')
def retrieve_results(step):
  world.results = requests.get(world.host + world.base_url, params=world.params, auth=world.auth)

@step(u'I post to the url')
def post_to_url(step):
  world.results = requests.post(world.host + world.base_url, params=world.params, auth=world.auth)

@step(u'the status code should be (\d+)')
def status_code_should_be(step, status_code):
  status = int(status_code)
  assert world.results.status_code == status, "Status invalid: %s, Results: %s" % (world.results.status_code, world.results)
