# Copyright 2021-2022 ByteOtter

from behave import *
from test_utils import *

### Step definitions for navigating throught OtterDen ###

@given(u'I am logged in')
def step_impl(context):
    context.browser.open("localhost:5000/home")
    context.browser.find_by_xpath("/html/body/header/nav/div/div/div[2]/a[1]")
    context.browser.find_by_id("email").send_key("testsuite@otter_den.com")
    context.browser.find_by_id("password").send_keys("testsuite")

@when(u'I click on "{btn_identifier}"')
def step_impl(context, btn_identifier):
    context.UtilFunc.find_by_id(btn_identifier).click()

@when(u'I enter "{value}" as "{identifier}"')
def step_impl(context, value, identifier):
    context.UtilFunc.find_by_id(identifier).send_keys(value)

@when(u'I navigate to "{url}"')
def step_impl(context, url):
   context.UtilFunc.open(url)
