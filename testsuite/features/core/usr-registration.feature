# Copyright ByteOtter (c) 2022

Feature: Registration and Login

    Scenario: Register as new user with email "testsuite@otter_den.com" and name "testuite"
        Given I am on the "Home" page
        And I follow "Register"
        And I enter "testsuite@otter_den.com" as "email"
        And I enter "testsuite" as "password"
