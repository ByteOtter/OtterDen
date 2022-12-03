# Copyright 2021-2022 ByteOtter

Feature: Create, view edit and delte posts

    Scenario: Login with test credentials
        Given I am logged in as "testsuite" with password "testsuite"

    Scenario: Create a new post
        Given I am on the "Home" page
        And I am logged in
        When I follow "Create new post!"
        Then I should see a "Create new post" text
        And I should see a "Title" field
        And I should see a "Content" field
        And I should see a "Add media" text
        And I should see a "Browse..." button
        When I enter "Testsuite" as "Title"
        And I enter "Testsuite" as "content"
        And I click on "Post"
        Then I should see a "Testuite" link in the content section
