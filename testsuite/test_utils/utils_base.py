# Copyright ByteOtter (c) 2022

"""
This file contains wrapper functions for Selenium API calls.
This is to avoid redundant expressions in code.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UtilFunc(object):
    __TIMEOUT = 10

    def __init__(self, driver):
        super(UtilFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, UtilFunc.__TIMEOUT)
        self._driver = driver
    
    def open(self, url):
        self._driver.get(url)
    
    def maximize(self):
        self._driver.maximize_window()
    
    def close(self):
        self._driver.quit()
    
    # Helper functions used to identify web locators in Selenium

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
    
    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))
    