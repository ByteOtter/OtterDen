# Copyright 2021-2022 ByteOtter

### Sanity-Checks to test GUI Output ###

Feature: Sanity checkt to test GUI outputs

    Scenario: The home page
        Given I am on the "Home" page
        Then I should see a "LogBlog" heading
        And I should see a "Home" link in the navigation bar
        And I should see a "About" link in the navigation bar
        And I should see a "Register" link in the navigation bar
        And i should see a "Login" link in the navigaton bar
