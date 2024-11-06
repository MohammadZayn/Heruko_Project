import os
import pytest
import yaml
from selenium import webdriver
from utils.logger import Logger


@pytest.fixture(scope='session', autouse=True)
def config():
    # Adjust the path to look one level up if needed
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'environment.yaml')
    config_path = os.path.abspath(config_path)
    print(f"Looking for configuration file at: {config_path}")  # Debugging line

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    with open(config_path, 'r') as file:
        env = yaml.safe_load(file)
        environment = env.get('default')
        if not environment:
            raise ValueError("Environment 'default' not specified in YAML config.")

        return env['environments'].get(environment)


@pytest.fixture(scope='function')
def setup(config):
    Logger.info("Initializing WebDriver")

    driver = None
    if config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif config['browser'] == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Browser not supported")

    driver.get(config['base_url'])
    yield driver
    Logger.info("Closing WebDriver")
    driver.quit()
