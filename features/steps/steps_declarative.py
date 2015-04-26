from lettuce import step, world

@step(u'I use the "([^"]*)" endpoint')
def when_i_use_the_endpoint(step, name):
    world.base_url = world.route(name)

@step(u'I identify my "([^"]*)" user credentials')
def and_i_identify_my_user_credentials(step, provider):
    username = world.cfg("username", provider)
    step.when('I provide parameter "%s" as "%s"' % ("username", username))

@step(u'I provide coordinates (.*), (.*)')
def and_i_provide_coordinates(step, lat, long):
    step.when('I provide parameter "%s" as "%s"' % ("lat", lat))
    step.when('I provide parameter "%s" as "%s"' % ("lng", long))

@step(u'it should have at least (\d*) valid "([^"]*)" items?')
def then_it_should_have_at_least_valid_result(step, num, name):
    step.then('it should have a list "%s"' % (name))
    step.then('the list should have at least %d items' % (int(num)))
