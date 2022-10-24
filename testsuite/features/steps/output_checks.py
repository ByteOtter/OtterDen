# Copyright 2021-2022 ByteOtter

from behave import *

### Step defintions to check LogBlogs output ###

@given(u'I am on the "(.?*)" page')
def step_impl(context):
    pass

@then(u'I should see a "(.?*)" text')
def step_impl(context):
    pass

@then(u'I should see a "(.?*)" link')
def step_impl(context):
    pass

@then(u'I should see a "LogBlog" heading')
def step_impl(context):
    pass
