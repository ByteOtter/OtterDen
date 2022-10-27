# Copyright 2021-2022 ByteOtter

### Sanity-Checks to test GUI Output ###

Feature: Sanity checkt to test default GUI outputs

    Scenario: The home page
        Given I am on the "Home" page
        Then I should see a "LogBlog" heading
        And I should see a "Home" link in the navigation bar
        And I should see a "About" link in the navigation bar
        And I should see a "Register" link in the navigation bar
        And i should see a "Login" link in the navigaton bar
        And I should see a "Welcome to LogBlog" text
        And I should see a "A basic but solid online blog." text
    
    Scenario: The about page
        Given I am on the "Home" page
        When I follow "About"
        Then I should see a "About" heading
    
    Scenario: The registration form
        Given I am on the "Home" page
        And I follow "Register"
        Then I should see a "Create your LogBlog Account!" text
        And I should see a "Username" field
        And I should see a "Email" field
        And I should see a "Password" field
        And I should see a "Confirm Password" field
        And I should see a "Sign Up" button
        And I should see a "Already have an account" text
        And I should see a "Sign In!" link
    
    Scenario: The login form
        Given I am on the "Home" page
        And I follow "Login"
        Then I should see a "Welcome back! Please login." text
        And I should see a "Email" field
        And I should see a "Password" field
        And I should see a "Remember me?" checkbox
        And I should see a "Sign In" button
        And I should see a "Forgot your password?" link
        And I should see a "New to LogBlog?" text
        And I should see a "Join for free!" link
