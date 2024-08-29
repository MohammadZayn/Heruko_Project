from pages.login_page import Login
import os
import allure
from pages.home_page import Home
from utils.helper import capture_screenshot


class Test_Appointment_Tokyo:
    @allure.title("#Test_Case -6")
    @allure.description("Booking the Tokyo country appointment")
    @allure.tag("Integration", "#6", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_6")
    def test_tokyo(self, setup):
        self.hp = Home(setup)
        self.lp = Login(setup)

        try:
            self.hp.home()
            self.hp.logo()
            self.lp.login_cred()

        except Exception as e:
            # Capture screenshot if there's an exception
            screenshot_path = capture_screenshot(setup, "home_page_error", "screenshots")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(setup, "home_page_success", "screenshots")
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
