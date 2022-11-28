# Copyright ByteOtter (c) 2022

from selenium import webdriver
from utils_base import UtilFunc

def get_browser(browser):
    if browser == "firefox":
        return UtilFunc(webdriver.Firefox())
