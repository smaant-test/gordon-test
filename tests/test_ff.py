from selenium import webdriver
import time

from nose.tools import *

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

@timed(150)
def test_ff_works_with_selenium():
    driver = webdriver.Firefox()

    for i in range(100):
        element = driver.find_element_by_id("myButtonId")
        element.click()
        print "fetched {}".format(element)
        time.sleep(1)
