# Copyright 2021-2022 ByteOtter

# TODO: implement tests for register login and logout
Feature: Registration and Login

    Scenario: Register as new user with email "testsuite@logblog.com" and name "testuite"
        Given I am on the "Home" page
        And I follow "Register"
        And I enter "testsuite@logblog.com" as "email"
        And I enter "testsuite" as "username"
