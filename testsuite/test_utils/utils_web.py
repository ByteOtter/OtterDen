# Copyright ByteOtter (c) 2022

"""
This file contains functions for anything related to the browser itself.
"""

from selenium import webdriver
from test_utils.utils_base import UtilFunc

def get_browser(browser):
    if browser == "firefox":
        return UtilFunc(webdriver.Firefox())
