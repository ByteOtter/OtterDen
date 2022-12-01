# Copyright 2021-2022 ByteOtter

from behave import *
from test_utils import *

### Step definitions for navigating throught LogBlog ###

@given(u'I am logged in')
def step_impl(context):
    context.browser.open("localhost:5000/home")
    context.browser.find_by_xpath("/html/body/header/nav/div/div/div[2]/a[1]")
    context.browser.find_by_id("email").send_key("testsuite@logblog.com")
    context.browser.find_by_id("password").send_keys("testsuite")

@given(u'I am on the "(.*?)" page')
def step_impl(context):
    pass

@when(u'I click on "(.*?)"')
def step_impl(context, btn_identifier):
    context.UtilFunc.find_by_id(btn_identifier).click()

@when(u'I enter "(.*?)" as "(.?*)"')
def step_impl(context, value, identifier):
    context.UtilFunc.find_by_id(identifier).send_keys(value)
