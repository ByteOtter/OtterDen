# Copyright ByteOtter (c) 2022

from behave import *
from test_utils import *

### Step definitions for initialization ###

@when(u'I start Firefox')
def step_impl(context):
    context.browser.open()
    context.browser.maximize()
