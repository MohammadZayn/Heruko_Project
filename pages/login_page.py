import time

from selenium.webdriver.common.by import By

class Login:

    def __init__(self, setup):
        self.driver = setup

    def login_cred(self):
        self.driver.find_element(By.CSS_SELECTOR, ".fa.fa-bars").click()
        self.driver.find_element(By.LINK_TEXT, "Login")
        self.driver.find_element(By.LINK_TEXT, "Make Appointment").click()
        self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        self.driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, "button").click()
