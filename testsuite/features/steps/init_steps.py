# Copyright ByteOtter (c) 2022

from behave import *
from test_utils import *

### Step definitions for initialization ###

@when(u'I start Firefox')
def step_impl(context):
    context.browser.open("localhost:5000/home")
    context.browser.maximize()

@when(u'I navigate to "localhost:5000/home"')
def step_impl(context, url):
   context.UtilFunc.open(url)
