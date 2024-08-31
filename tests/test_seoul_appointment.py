import allure

from pages.booking_page import booking
from pages.login_page import Login
from utils.helper import capture_screenshot


class Test_Appointment_Seoul:
    @allure.title("#Test_Case -5")
    @allure.description("Booking the Seoul country appointment")
    @allure.tag("Integration", "#5", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_5")
    def test_seoul(self, setup):
        try:
            self.lp = Login(setup)
            self.bp = booking(setup)
            self.lp.login_cred()
            self.bp.facility_seoul()
            self.bp.readmission()
            self.bp.healthcare_none()
            self.bp.yearmonth_picker()
            self.bp.day_picker()
            self.bp.health_issue()
            self.bp.confirmation()
        except Exception as e:
            # Capture screenshot if there's an exception
            screenshot_path = capture_screenshot(setup, "home_page_error")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(setup, "Tokyo_Appointment")
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)


