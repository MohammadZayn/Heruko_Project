```
1. Project Structure with Expanded Utilities

markdown
Copy code
pytest-hybrid-framework/
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_search.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
├── utils/
│   ├── __init__.py
│   ├── helper.py
│   ├── logger.py
│   ├── custom_exceptions.py
│   ├── constants.py
├── config/
│   ├── __init__.py
│   ├── config.json
│   ├── environment.yaml
├── test_data/
│   ├── login_data.json
│   ├── search_data.json
├── reports/
│   ├── report.html
├── logs/
│   ├── test_log.log
├── pytest.ini
├── requirements.txt
└── conftest.py
2. BasePage Class
This class will provide common methods that all pages can inherit:

python
Copy code
# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_title(self):
        return self.driver.title
3. LoginPage Example
Example of a login page using the BasePage class:

python
Copy code
# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'passwd')
        self.login_button = (By.ID, 'SubmitLogin')

    def login(self, email, password):
        self.send_keys(self.email_input, email)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)
4. Environment Handling
Handle multiple environments using a YAML configuration:

yaml
Copy code
# config/environment.yaml
default: qa

environments:
  qa:
    base_url: "http://automationpractice.com/index.php"
    browser: "chrome"
  prod:
    base_url: "http://automationpractice.com/index.php"
    browser: "firefox"
Modify conftest.py to read the environment:

python
Copy code
# conftest.py
import pytest
import yaml
from selenium import webdriver
from utils.logger import Logger

@pytest.fixture(scope='session', autouse=True)
def config():
    with open('config/environment.yaml', 'r') as file:
        env = yaml.safe_load(file)
        environment = env['default']
        return env['environments'][environment]

@pytest.fixture(scope='function')
def setup(config):
    Logger.info("Initializing WebDriver")
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")

    driver.get(config['base_url'])
    yield driver
    Logger.info("Closing WebDriver")
    driver.quit()
5. Custom Logger
Use a logger to capture logs:

python
Copy code
# utils/logger.py
import logging

class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('logs/test_log.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(file_handler)

        return logger

    @staticmethod
    def info(message):
        logger = Logger.get_logger()
        logger.info(message)
6. Custom Exceptions
Handle custom exceptions to improve debugging:

python
Copy code
# utils/custom_exceptions.py
class ElementNotFoundException(Exception):
    def __init__(self, message="Element not found"):
        self.message = message
        super().__init__(self.message)
7. Constants
Store constants used across the project:

python
Copy code
# utils/constants.py
class Constants:
    LOGIN_SUCCESS_MESSAGE = "Welcome to your account."
    INVALID_LOGIN_MESSAGE = "Authentication failed."
8. Test Case Examples
Example test cases using the framework:

python
Copy code
# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from utils.constants import Constants

@pytest.mark.parametrize("email, password", [
    ("test@example.com", "invalid_password"),
    ("invalid@example.com", "test123")
])
def test_invalid_login(setup, email, password):
    login_page = LoginPage(setup)
    login_page.login(email, password)
    assert Constants.INVALID_LOGIN_MESSAGE in setup.page_source
python
Copy code
# tests/test_search.py
from pages.home_page import HomePage

def test_search(setup):
    home_page = HomePage(setup)
    home_page.search('Dress')
    assert 'Dress' in home_page.get_title()
9. Running Tests with HTML Reporting
The pytest.ini file should be configured to generate detailed HTML reports:

ini
Copy code
# pytest.ini
[pytest]
addopts = --html=reports/report.html --self-contained-html --tb=short
10. Best Practices
DRY Principle: Reuse methods from BasePage across different pages.
Data-Driven Testing: Use JSON/YAML/CSV files for data-driven tests.
Custom Markers: Use pytest markers to group tests, e.g., @pytest.mark.smoke.
Parallel Execution: Run tests in parallel using pytest-xdist.
This extended framework will make it easier to maintain and scale your automation efforts. Let me know if you need further details on any specific part!




```
1. Project Structure with Expanded Utilities
We'll add some more useful components like custom exceptions, constants, environment handling, and reporting:

markdown
Copy code
pytest-hybrid-framework/
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_search.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
├── utils/
│   ├── __init__.py
│   ├── helper.py
│   ├── logger.py
│   ├── custom_exceptions.py
│   ├── constants.py
├── config/
│   ├── __init__.py
│   ├── config.json
│   ├── environment.yaml
├── test_data/
│   ├── login_data.json
│   ├── search_data.json
├── reports/
│   ├── report.html
├── logs/
│   ├── test_log.log
├── pytest.ini
├── requirements.txt
└── conftest.py
2. BasePage Class
This class will provide common methods that all pages can inherit:

python
Copy code
# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_title(self):
        return self.driver.title
3. LoginPage Example
Example of a login page using the BasePage class:

python
Copy code
# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'passwd')
        self.login_button = (By.ID, 'SubmitLogin')

    def login(self, email, password):
        self.send_keys(self.email_input, email)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)
4. Environment Handling
Handle multiple environments using a YAML configuration:

yaml
Copy code
# config/environment.yaml
default: qa

environments:
  qa:
    base_url: "http://automationpractice.com/index.php"
    browser: "chrome"
  prod:
    base_url: "http://automationpractice.com/index.php"
    browser: "firefox"
Modify conftest.py to read the environment:

python
Copy code
# conftest.py
import pytest
import yaml
from selenium import webdriver
from utils.logger import Logger

@pytest.fixture(scope='session', autouse=True)
def config():
    with open('config/environment.yaml', 'r') as file:
        env = yaml.safe_load(file)
        environment = env['default']
        return env['environments'][environment]

@pytest.fixture(scope='function')
def setup(config):
    Logger.info("Initializing WebDriver")
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")

    driver.get(config['base_url'])
    yield driver
    Logger.info("Closing WebDriver")
    driver.quit()
5. Custom Logger
Use a logger to capture logs:

python
Copy code
# utils/logger.py
import logging

class Logger:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('logs/test_log.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(file_handler)

        return logger

    @staticmethod
    def info(message):
        logger = Logger.get_logger()
        logger.info(message)
6. Custom Exceptions
Handle custom exceptions to improve debugging:

python
Copy code
# utils/custom_exceptions.py
class ElementNotFoundException(Exception):
    def __init__(self, message="Element not found"):
        self.message = message
        super().__init__(self.message)
7. Constants
Store constants used across the project:

python
Copy code
# utils/constants.py
class Constants:
    LOGIN_SUCCESS_MESSAGE = "Welcome to your account."
    INVALID_LOGIN_MESSAGE = "Authentication failed."
8. Test Case Examples
Example test cases using the framework:

python
Copy code
# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from utils.constants import Constants

@pytest.mark.parametrize("email, password", [
    ("test@example.com", "invalid_password"),
    ("invalid@example.com", "test123")
])
def test_invalid_login(setup, email, password):
    login_page = LoginPage(setup)
    login_page.login(email, password)
    assert Constants.INVALID_LOGIN_MESSAGE in setup.page_source
python
Copy code
# tests/test_search.py
from pages.home_page import HomePage

def test_search(setup):
    home_page = HomePage(setup)
    home_page.search('Dress')
    assert 'Dress' in home_page.get_title()
9. Running Tests with HTML Reporting
The pytest.ini file should be configured to generate detailed HTML reports:

ini
Copy code
# pytest.ini
[pytest]
addopts = --html=reports/report.html --self-contained-html --tb=short
10. Best Practices
DRY Principle: Reuse methods from BasePage across different pages.
Data-Driven Testing: Use JSON/YAML/CSV files for data-driven tests.
Custom Markers: Use pytest markers to group tests, e.g., @pytest.mark.smoke.
Parallel Execution: Run tests in parallel using pytest-xdist.
This extended framework will make it easier to maintain and scale your automation efforts. Let me know if you need further details on any specific part!




To generate Allure reports automatically while running pytest, you can configure the pytest.ini file. Here’s how you can set it up:

Install Allure dependencies: Ensure you have the required packages installed:

bash
Copy code
pip install allure-pytest
Configure pytest.ini: Add or update your pytest.ini file with the following content:

ini
Copy code
[pytest]
addopts = --alluredir=./allure-results
This configuration automatically generates Allure results in the ./allure-results directory every time you run pytest.

Run Tests: Run your tests as usual:

bash
Copy code
pytest
After running the tests, the results will be stored in the allure-results folder.

Generate Allure Report: Once the tests are completed, you can generate the Allure report using the command:

bash
Copy code
allure serve ./allure-results
This command will start a local server and open the report in your default web browser.

Advanced Options
You can also pass additional options via the pytest.ini file if needed. For example:

ini
Copy code
[pytest]
addopts = --alluredir=./allure-results --clean-alluredir
This ensures the Allure results directory is cleaned before each test run.

Now, your tests will automatically generate an Allure report after each pytest run without needing to pass additional options from the command line.








Certainly! Here's a README.md template that follows market standards, explaining the pytest hybrid automation framework in detail:

markdown
Copy code
# Pytest Hybrid Automation Framework

## Overview

This is a Pytest-based hybrid automation framework designed for web UI testing. The framework is structured to be scalable, maintainable, and reusable, integrating Page Object Model (POM), Data-Driven Testing (DDT), and custom utilities for efficient test automation.

## Features

- **Page Object Model (POM):** Encapsulates web elements and actions in separate classes.
- **Data-Driven Testing:** Test data is externalized using JSON and YAML files.
- **Configurable Environment:** Supports multiple environments (e.g., QA, Prod) through YAML configuration.
- **Logging:** Captures test execution logs.
- **HTML Reporting:** Generates detailed HTML reports for test execution.
- **Custom Exceptions:** Provides meaningful error messages for easier debugging.
- **Scalable Structure:** Easy to extend and maintain.

## Project Structure

```plaintext
pytest-hybrid-framework/
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_search.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
├── utils/
│   ├── __init__.py
│   ├── helper.py
│   ├── logger.py
│   ├── custom_exceptions.py
│   ├── constants.py
├── config/
│   ├── __init__.py
│   ├── config.json
│   ├── environment.yaml
├── test_data/
│   ├── login_data.json
│   ├── search_data.json
├── reports/
│   ├── report.html
├── logs/
│   ├── test_log.log
├── pytest.ini
├── requirements.txt
└── conftest.py
Getting Started
Prerequisites
Python 3.7+
Google Chrome or Mozilla Firefox (for WebDriver)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/pytest-hybrid-framework.git
cd pytest-hybrid-framework
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configuration
Set up your environment configuration: Edit the config/environment.yaml file to configure your environments:

yaml
Copy code
default: qa

environments:
  qa:
    base_url: "http://automationpractice.com/index.php"
    browser: "chrome"
  prod:
    base_url: "http://automationpractice.com/index.php"
    browser: "firefox"
Update test data: Modify JSON files in the test_data/ directory to suit your testing needs.

Running Tests
Run all tests:

bash
Copy code
pytest
Run tests with HTML reporting:

bash
Copy code
pytest --html=reports/report.html --self-contained-html
Run tests in parallel:

bash
Copy code
pytest -n 4  # Adjust the number based on your CPU cores
Reporting and Logs
HTML Reports: Detailed reports are generated in the reports/ directory.
Logs: Execution logs are stored in the logs/ directory.
Adding New Tests
Create a new test script under the tests/ directory.
Use the Page Object Model by importing the necessary page classes.
Utilize fixtures, data-driven parameters, and custom utilities as needed.
Best Practices
Follow the DRY principle when writing test cases.
Use parameterized tests for data-driven testing.
Implement custom markers to categorize tests (e.g., smoke, regression).
Integrate the framework with CI/CD pipelines for continuous testing.
Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.

Contact
For questions or suggestions, contact your.email@example.com.

less
Copy code

### How to Customize:
- Replace `"https://github.com/your-repo/pytest-hybrid-framework.git"` with your actual GitHub repository URL.
- Update the email address in the **Contact** section.
- Add specific details relevant to your project in the **Getting Started** section.

This README provides a clear overview, setup instructions, and best practices, making it easy for others to understand and contribute to your project.


## To run the pytest case specifically from which broswer use this command 'pytest --browser=chrome"


```

# Heruko Healthcare Test Automation

This project automates test cases for the [Heruko Healthcare](https://heruko.healthcare) website using Selenium and the Page Object Model (POM) design pattern. The aim is to create a robust, maintainable, and scalable test automation suite.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Test Execution](#test-execution)
- [Project Structure](#project-structure)
- [Best Practices](#best-practices)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview

This project focuses on automating the end-to-end testing of the Heruko Healthcare website. Using Selenium WebDriver and the Page Object Model (POM) design pattern, the tests are designed for easy maintenance and high reusability. The framework also supports cross-browser testing and includes detailed reporting.

## Features

- **Page Object Model (POM):** Ensures modularity and reduces code duplication.
- **Cross-Browser Testing:** Tests can be executed on multiple browsers to ensure compatibility.
- **TestNG Integration:** Provides detailed reporting and parallel execution capabilities.
- **Logging and Reporting:** Logs and screenshots are captured for failed test cases.

## Technologies Used

- **Programming Language:** Python
- **Build Tool:** Jenkins
- **Testing Framework:** PyTest
- **Automation Tool:** Selenium WebDriver
- **Reporting:** Allure/TestNG Reports

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Heruko_Tc.git
2. Navigate to the project directory:
   ```bash
   cd Heruko_Tc

#### Test results will be available in the target/surefire-reports directory.
## Project Structure
```plaintext
Heruko_Overview/
├── Page_Object_Model/
│   ├── All_actions/
│   │   ├── test_create.py
│   │   ├── test_read.py
│   │   ├── test_update.py
│   │   ├── test_delete.py
├── Test_Cases/
│   ├── Create_Appointment.py
│   ├── Create_Appointment_With_Details.py
│   ├── Create_Appointment_With_Full_Update.py
├── utils/
│   ├── request_util.py
│   ├── data_util.py
│   ├── data1_util.py
├── conftest.py
├── requirements.txt
└── README.md
```
# Best Practices for Automated Testing

## 1. Follow the Page Object Model (POM)

The Page Object Model (POM) is a design pattern that helps in creating an object repository for web UI elements. It separates the test logic from the UI logic, making the code more maintainable and reusable.

### Benefits:
- **Separation of Concerns:** Keeps test code clean and easy to understand by separating UI interactions from the test logic.
- **Reusability:** Common operations on UI elements are encapsulated in methods within the page objects, allowing you to reuse them across different tests.
- **Maintainability:** Changes to UI elements need only be updated in one place, the page object, which simplifies maintenance when the UI changes.

### Implementation Tips:
- Create a separate class for each page of the application.
- Define locators for UI elements and wrap them in methods that perform actions on those elements.
- Avoid putting test assertions within the page objects; these should remain in the test scripts.

```python
# Page Object in Python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element_by_id('username')
        self.password_input = driver.find_element_by_id('password')
        self.login_button = driver.find_element_by_id('login')

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
```
## 2. Use Data-Driven Testing
Data-driven testing involves running a test script with multiple sets of data inputs to ensure comprehensive test coverage. This approach allows you to validate how the application behaves with different inputs, edge cases, and data scenarios.

### Benefits:
- **Increased Test Coverage:** Allows testing of multiple scenarios and edge cases without duplicating test code.
- **Efficiency:** Reduces the number of test scripts needed, as the same script can run with different data sets.
- **Ease of Maintenance:** Test data can be managed separately from test scripts, making it easier to update or expand test scenarios.

### Implementation Tips:
- Store test data in external files such as CSV, JSON, or Excel.
- Use a framework that supports parameterized testing to feed the test data into your scripts.
- Ensure that your tests validate expected results for each data set.
```python
# Data-Driven Test in Python using pytest
import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "password1"),
    ("user2", "password2"),
    ("user3", "password3"),
])
def test_login(username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert "Welcome" in driver.page_source
```
## 3. Implement Cross-Browser Testing
Cross-browser testing ensures that your application works correctly across different web browsers and versions. It's crucial for providing a consistent user experience and catching browser-specific issues.

### Benefits:
**Compatibility:** Ensures that your application is functional across multiple browsers, reducing the risk of browser-specific bugs.
**User Experience:** Helps maintain a consistent experience for users, regardless of their preferred browser.
**Quality Assurance:** Early detection of browser-specific issues helps in delivering a more robust application.

#### Implementation Tips:
- Use cloud-based testing platforms like Selenium Grid, BrowserStack, or Sauce Labs to run tests across multiple browsers.
- Automate tests for popular browsers like Chrome, Firefox, Safari, and Edge.
- Prioritize testing on browsers and versions most commonly used by your audience.
```python
# Cross-Browser Testing in Python with Selenium
from selenium import webdriver

browsers = ['chrome', 'firefox', 'safari']

for browser in browsers:
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()

    driver.get("http://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
```
  ## Future Enhancements

### Integrate with CI/CD Tools like Jenkins

**Installation in Jenkins:**
1. Install Jenkins: Follow the [official guide](https://www.jenkins.io/doc/book/installing/) to set up Jenkins.
2. Install Python: Ensure that Python and required dependencies (e.g., Selenium) are installed on the Jenkins server.
3. Create a new Jenkins job: 
   - Choose "Freestyle project" or "Pipeline."
   - Configure the job to pull the code from the repository.
   - Add a build step to execute the test script using the command:
     ```bash
     python -m filename.py -s tests
     ```
   - Configure email notifications for test results.
4. Set up triggers: Schedule jobs or trigger them via webhooks on code commits.

**Benefits:**
- Automates test execution on every code change.
- Generates detailed reports that can be viewed directly within Jenkins.
- Supports continuous integration for a smooth development workflow.

### Add Mobile Testing Support Using Appium

**Installation and Setup:**
1. Install Appium: Follow the [Appium documentation](http://appium.io/docs/en/about-appium/intro/) to set up Appium.
2. Configure Python with Appium: 
   - Install Appium-Python-Client:
     ```bash
     pip install Appium-Python-Client
     ```
   - Set up desired capabilities for Android/iOS in your test script:
     ```python
     desired_caps = {
         'platformName': 'Android',
         'deviceName': 'emulator-5554',
         'app': '/path/to/app.apk'
     }
     ```
3. Write and run test cases for mobile applications.

**Benefits:**
- Ensures cross-platform compatibility for the Heruko Healthcare application.
- Provides end-to-end testing on real devices and emulators.

### Implement Visual Regression Testing

**Installation and Setup:**
1. Choose a tool: For Python, consider tools like `SeleniumBase` or `Pikachu`.
2. Install the required package:
   ```bash
   pip install seleniumbase

## Contributing
Contributions are welcome! Please create a pull request with a detailed description of the changes.

### Contact
For any inquiries or opportunities, feel free to reach out via www.linkedin.com/in/mohammadzayn or email at mohammadshaik776@gmail.com.




# Heruko Healthcare Test Automation

This project automates test cases for the [Heruko Healthcare](https://heruko.healthcare) website using Selenium and the Page Object Model (POM) design pattern. The aim is to create a robust, maintainable, and scalable test automation suite.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Test Execution](#test-execution)
- [Project Structure](#project-structure)
- [Best Practices](#best-practices)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview

This project focuses on automating the end-to-end testing of the Heruko Healthcare website. Using Selenium WebDriver and the Page Object Model (POM) design pattern, the tests are designed for easy maintenance and high reusability. The framework also supports cross-browser testing and includes detailed reporting.

## Features

- **Page Object Model (POM):** Ensures modularity and reduces code duplication.
- **Cross-Browser Testing:** Tests can be executed on multiple browsers to ensure compatibility.
- **TestNG Integration:** Provides detailed reporting and parallel execution capabilities.
- **Logging and Reporting:** Logs and screenshots are captured for failed test cases.

## Technologies Used

- **Programming Language:** Python
- **Build Tool:** Jenkins
- **Testing Framework:** PyTest
- **Automation Tool:** Selenium WebDriver
- **Reporting:** Allure/TestNG Reports

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Heruko_Tc.git
2. Navigate to the project directory:
   ```bash
   cd Heruko_Tc

#### Test results will be available in the target/surefire-reports directory.
## Project Structure
```plaintext
Heruko_Overview/
├── Page_Object_Model/
│   ├── All_actions/
│   │   ├── test_create.py
│   │   ├── test_read.py
│   │   ├── test_update.py
│   │   ├── test_delete.py
├── Test_Cases/
│   ├── Create_Appointment.py
│   ├── Create_Appointment_With_Details.py
│   ├── Create_Appointment_With_Full_Update.py
├── utils/
│   ├── request_util.py
│   ├── data_util.py
│   ├── data1_util.py
├── conftest.py
├── requirements.txt
└── README.md
```
# Best Practices for Automated Testing

## 1. Follow the Page Object Model (POM)

The Page Object Model (POM) is a design pattern that helps in creating an object repository for web UI elements. It separates the test logic from the UI logic, making the code more maintainable and reusable.

### Benefits:
- **Separation of Concerns:** Keeps test code clean and easy to understand by separating UI interactions from the test logic.
- **Reusability:** Common operations on UI elements are encapsulated in methods within the page objects, allowing you to reuse them across different tests.
- **Maintainability:** Changes to UI elements need only be updated in one place, the page object, which simplifies maintenance when the UI changes.

### Implementation Tips:
- Create a separate class for each page of the application.
- Define locators for UI elements and wrap them in methods that perform actions on those elements.
- Avoid putting test assertions within the page objects; these should remain in the test scripts.

```python
# Page Object in Python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element_by_id('username')
        self.password_input = driver.find_element_by_id('password')
        self.login_button = driver.find_element_by_id('login')

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
```
## 2. Use Data-Driven Testing
Data-driven testing involves running a test script with multiple sets of data inputs to ensure comprehensive test coverage. This approach allows you to validate how the application behaves with different inputs, edge cases, and data scenarios.

### Benefits:
- **Increased Test Coverage:** Allows testing of multiple scenarios and edge cases without duplicating test code.
- **Efficiency:** Reduces the number of test scripts needed, as the same script can run with different data sets.
- **Ease of Maintenance:** Test data can be managed separately from test scripts, making it easier to update or expand test scenarios.

### Implementation Tips:
- Store test data in external files such as CSV, JSON, or Excel.
- Use a framework that supports parameterized testing to feed the test data into your scripts.
- Ensure that your tests validate expected results for each data set.
```python
# Data-Driven Test in Python using pytest
import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "password1"),
    ("user2", "password2"),
    ("user3", "password3"),
])
def test_login(username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert "Welcome" in driver.page_source
```
## 3. Implement Cross-Browser Testing
Cross-browser testing ensures that your application works correctly across different web browsers and versions. It's crucial for providing a consistent user experience and catching browser-specific issues.

### Benefits:
**Compatibility:** Ensures that your application is functional across multiple browsers, reducing the risk of browser-specific bugs.
**User Experience:** Helps maintain a consistent experience for users, regardless of their preferred browser.
**Quality Assurance:** Early detection of browser-specific issues helps in delivering a more robust application.

#### Implementation Tips:
- Use cloud-based testing platforms like Selenium Grid, BrowserStack, or Sauce Labs to run tests across multiple browsers.
- Automate tests for popular browsers like Chrome, Firefox, Safari, and Edge.
- Prioritize testing on browsers and versions most commonly used by your audience.
```python
# Cross-Browser Testing in Python with Selenium
from selenium import webdriver

browsers = ['chrome', 'firefox', 'safari']

for browser in browsers:
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()

    driver.get("http://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
```
  ## Future Enhancements

### Integrate with CI/CD Tools like Jenkins

**Installation in Jenkins:**
1. Install Jenkins: Follow the [official guide](https://www.jenkins.io/doc/book/installing/) to set up Jenkins.
2. Install Python: Ensure that Python and required dependencies (e.g., Selenium) are installed on the Jenkins server.
3. Create a new Jenkins job: 
   - Choose "Freestyle project" or "Pipeline."
   - Configure the job to pull the code from the repository.
   - Add a build step to execute the test script using the command:
     ```bash
     python -m filename.py -s tests
     ```
   - Configure email notifications for test results.
4. Set up triggers: Schedule jobs or trigger them via webhooks on code commits.

**Benefits:**
- Automates test execution on every code change.
- Generates detailed reports that can be viewed directly within Jenkins.
- Supports continuous integration for a smooth development workflow.

### Add Mobile Testing Support Using Appium

**Installation and Setup:**
1. Install Appium: Follow the [Appium documentation](http://appium.io/docs/en/about-appium/intro/) to set up Appium.
2. Configure Python with Appium: 
   - Install Appium-Python-Client:
     ```bash
     pip install Appium-Python-Client
     ```
   - Set up desired capabilities for Android/iOS in your test script:
     ```python
     desired_caps = {
         'platformName': 'Android',
         'deviceName': 'emulator-5554',
         'app': '/path/to/app.apk'
     }
     ```
3. Write and run test cases for mobile applications.

**Benefits:**
- Ensures cross-platform compatibility for the Heruko Healthcare application.
- Provides end-to-end testing on real devices and emulators.

### Implement Visual Regression Testing

**Installation and Setup:**
1. Choose a tool: For Python, consider tools like `SeleniumBase` or `Pikachu`.
2. Install the required package:
   ```bash
   pip install seleniumbase

## Contributing
Contributions are welcome! Please create a pull request with a detailed description of the changes.

### Contact
For any inquiries or opportunities, feel free to reach out via www.linkedin.com/in/mohammadzayn or email at mohammadshaik776@gmail.com.





# Run all tests in a directory
pytest tests/

# Run specific test files
pytest tests/test_file1.py tests/test_file2.py

# Run tests with specific marker
pytest -m smoke

# Run tests with names matching keyword
pytest -k "test_login or test_logout"

# Run tests in parallel with 4 processes
pytest -n 4
