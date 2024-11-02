from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def capture_screenshot(driver, name):
    # Define the path for the screenshots directory
    screenshot_dir = 'C:\\Users\\moham\\PycharmProjects\\Heruko_Project\\Snaps'
    
    # Create the directory if it does not exist
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    # Define the full path to save the screenshot
    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
    
    # Capture and save the screenshot
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
