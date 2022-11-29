# Copyright ByteOtter (c) 2022

### Initialization of Test ###

Feature: Setting up the Browser and page

    Scenario: LogBlog
        When I start Firefox
        And I navigate to "localhost:5000/home/"
        Then I should see a "LogBlog" text

Feature: Registration and Login

    Scenario: Register as new user with email "testsuite@logblog.com" and name "testuite"
        Given I am on the "Home" page
        And I follow "Register"
        And I enter "testsuite@logblog.com" as "email"
        And I enter "testsuite" as "password"
