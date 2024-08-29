import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def capture_screenshot(driver, name, folder_name):
    # Ensure screenshots directory exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    screenshot_path = f"folder_name/{name}.png"
    driver.save_screenshot(screenshot_path)
    return screenshot_path

class base_helpers:
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
