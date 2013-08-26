from lettuce import *

@after.all
def say_goodbye(total):
    print "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_ran,
        total.scenarios_passed
    )
    print "Goodbye!"

