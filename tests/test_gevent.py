from nose.tools import *

def test_nothing():
  from gevent.hub import get_hub, reinit
  assert_true(True)
