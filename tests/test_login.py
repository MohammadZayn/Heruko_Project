import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Ensure screenshots directory exists
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def capture_screenshot(driver, name):
    screenshot_path = f"screenshots/{name}.png"
    driver.save_screenshot(screenshot_path)
    return screenshot_path

class TestHome:
    @allure.title("#Test_Case -4")
    @allure.description("Checking the home page and capturing the screenshot.")
    @allure.tag("Integration", "#4", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_4")
    def test_home(self, setup):
        driver = setup

        # Perform some actions
        try:
            driver.find_element(By.CSS_SELECTOR, ".fa.fa-bars").click()
            driver.find_element(By.LINK_TEXT, "Home").click()
            address = driver.find_element(By.XPATH, "//body//footer//p[1]").text
            print(address)
        except Exception as e:
            # Capture screenshot if there's an exception
            screenshot_path = capture_screenshot(driver, "home_page_error")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(driver, "home_page_success")
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

        # Continue with test assertions and steps
        wel_msg = driver.find_element(By.CSS_SELECTOR, "div[class='text-vertical-center'] h1").text
        print('Welcome to the', wel_msg)
