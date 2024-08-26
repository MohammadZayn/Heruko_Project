import os

import pytest
import yaml
from selenium import webdriver
from utils.logger import Logger

@pytest.fixture(scope='session', autouse=True)
def config():
    # Use an absolute path for debugging
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'environment.yaml')
    with open(config_path, 'r') as file:
        env = yaml.safe_load(file)
        environment = env['default']
        return env['environments'][environment]

@pytest.fixture(scope='function')
def setup(config):
    Logger.info("Initializing WebDriver")
    if config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Browser not supported")

    driver.get(config['base_url'])
    yield driver
    Logger.info("Closing WebDriver")
    driver.quit()