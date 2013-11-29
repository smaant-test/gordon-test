from nose.tools import *
import gevent_psycopg2
from gevent.hub import get_hub, reinit

def test_nothing():
  assert_true(True)
