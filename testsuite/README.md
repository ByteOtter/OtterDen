# Testing OtterDen with Behave

## About

OtterDen now uses the [Behave](https://behave.readthedocs.io/en/stable/) testing framework to automate tests for all its features.

This is still under heavy development and this section will be expanded upon when more information is available.

## Structure

The testsuite is mainly focused on testing WebUI output and functionality using [Selenium](https://www.selenium.dev/).<br>
The Browser these tests are being run on is Firefox using [Geckodriver](https://github.com/mozilla/geckodriver/releases) as the WebDriver.

Make sure pip installs all requirements.

## Running tests

To run the example tests already implemented:

- make sure that pip installed all of OtterDens requirements `pip install -R requirements.txt`

- go inside the `testsuite` folder and run `behave path/of/test.feature`