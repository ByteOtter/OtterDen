# Copyright ByteOtter (c) 2022

### Initialization of Test ###

Feature: Setting up the Browser and page

    Scenario: OtterDen
        When I start Firefox
        And I navigate to "localhost:5000/home/"
        Then I should see a "OtterDen" text
