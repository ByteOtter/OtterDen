# Copyright ByteOtter (c) 2022

import os
import time

from behave.fixture import use_fixture_by_tag
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_utils.utils_web import get_browser

def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the config file
    browser = get_browser(config.get('Environment', 'Browser'))
    context.browser = browser

    if context.browser == "firefox":
        context.driver = webdriver.Firefox()


def after_all(context):
    context.browser.close()
