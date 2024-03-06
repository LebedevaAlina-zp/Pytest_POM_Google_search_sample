
## How to run in PyCharm

1) To install all needed packages run in terminal: pip install -r requirements.txt

2) Download corresponding Selenium WebDrivers and past the paths to driver files to selenium_chromedriver 
and selenium_firefoxdriver fixtures in conftest.py.

3) Run tests


Based on the framework (files base.py, elements.py, conftest.py) from https://github.com/TimurNurlygayanov/ui-tests-example by TimurNurlygayanov

Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

