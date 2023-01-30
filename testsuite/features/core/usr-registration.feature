# Copyright ByteOtter (c) 2022

Feature: Registration and Login

    Scenario: Register as new user with email "testsuite@otter_den.com" and name "testuite"
        Given I am on the "Home" page
        And I follow "Register"
        When I enter "testsuite@otter_den.com" as "email"
        And I enter "testsuite" as "password"
        And I click "Sign Up"
        Then I should see a "Your Account has been created! Welcome, testsuite!" text
