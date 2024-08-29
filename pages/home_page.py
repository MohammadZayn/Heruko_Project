from selenium.webdriver.common.by import By

class Home:

    def __init__(self, driver):
        self.wel_msg = None
        self.driver = driver

    def home(self):
        self.driver.find_element(By.CSS_SELECTOR, ".fa.fa-bars").click()
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        address = self.driver.find_element(By.XPATH, "//body//footer//p[1]").text
        print(address)

    def logo(self):
        self.wel_msg = self.driver.find_element(By.CSS_SELECTOR, "div[class='text-vertical-center'] h1").text
        print('Welcome to the', self.wel_msg)

