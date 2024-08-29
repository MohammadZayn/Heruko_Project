from logging import exception

import allure

from pages.booking_page import booking
from pages.login_page import Login
from utils.helper import capture_screenshot


class Test_Automation:
    @allure.title("#Test_Case -1")
    @allure.description("Booking the HongKong country appointment with direct date option")
    @allure.tag("Integration", "#1", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_1")
    def test_Appointment(self, setup):
        try:
            self.lp = Login(setup)
            self.bp = booking(setup)
            self.lp.login_cred()
            self.bp.facility_hongkong()
            self.bp.readmission()
            self.bp.healthcare_medicare()
            self.bp.direct_date()
            self.bp.health_issue()
            self.bp.confirmation()
        except Exception as e:
            # Capture screenshot if there's an exception
            screenshot_path = capture_screenshot(setup, "home_page_error", "screenshots")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(setup, "home_page_success", "screenshots")
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
