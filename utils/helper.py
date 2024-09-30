from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def capture_screenshot(driver, name):
    # Ensure Snaps directory exists
    screenshot_path = r"C:\ProgramData\Jenkins\.jenkins\workspace\Health_Care Project\Snaps"
    # Define the full path for the screenshot
    screenshot_path = os.path.join(screenshot_path, f"{name}.png")
    # Capture the screenshot
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
