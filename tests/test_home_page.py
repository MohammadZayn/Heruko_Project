import allure
from pages.home_page import Home
from utils.helper import base_helpers, capture_screenshot


class Test_Home:
    @allure.title("#Test_Case -2")
    @allure.description("Checking the home page and capturing the screenshot.")
    @allure.tag("Integration", "#2", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_2")
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
