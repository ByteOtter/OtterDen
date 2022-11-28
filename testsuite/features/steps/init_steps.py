# Copyright ByteOtter (c) 2022

from behave import *

### Step definitions for initialization ###

@given(u'I open Firefox')
def step_impl(context):
    context.browser.open()
    context.browser.maximize()

@when(u'I navigate to "(.?*)"')
def step_impl(context, url):
    pass