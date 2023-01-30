# Copyright 2021-2022 ByteOtter

# TODO: implement tests for login and logout
Feature: Login and Logout

    Scenario: Make sure not to be logged in
        Given I am not logged in

    Scenario: Logged in
        When I follow "Login"
        And I enter "testsuite@otter_den.com" as "email"
        And I enter "testsuite" as "password"
        And I click "Sign In"
        Then I should see a "Welcome, testsuite!" text
