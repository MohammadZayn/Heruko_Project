import os

import allure
from pages.home_page import Home

# Ensure screenshots directory exists
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def capture_screenshot(driver, name):
    screenshot_path = f"screenshots/{name}.png"
    driver.save_screenshot(screenshot_path)
    return screenshot_path

class Test_Home:
    @allure.title("#Test_Case -4")
    @allure.description("Checking the home page and capturing the screenshot.")
    @allure.tag("Integration", "#4", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_4")
    def test_home(self, setup):
        self.ap = Home(setup)
        try:
            self.ap.home()
            self.ap.logo()
        except Exception as e:
            # Capture screenshot if there's an exception
            screenshot_path = capture_screenshot(setup, "home_page_error")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(setup, "home_page_success")
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
