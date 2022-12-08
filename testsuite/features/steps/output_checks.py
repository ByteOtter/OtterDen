# Copyright 2021-2022 ByteOtter

from behave import *
from test_utils import *

### Step defintions to check OtterDens output ###

@given(u'I am on the "{text}" page')
def step_impl(context, text):
    pass

@then(u'I should see a "{text}" text')
def step_impl(context, text):
    context.UtilFunc.find_by_name(text)

@then(u'I should see a "{text}" link')
def step_impl(context, text):
    pass

@then(u'I should see a "{text}" heading')
def step_impl(context):
    pass
