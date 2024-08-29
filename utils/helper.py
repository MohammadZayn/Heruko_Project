from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class base_helpers:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.base_url = "https://flipcart.com"

    @staticmethod
    def base_url(self):
        self.driver.get(self.base_url)

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