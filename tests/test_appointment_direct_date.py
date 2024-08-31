import os
import allure
from pages.booking_page import booking
from pages.login_page import Login
from utils.helper import capture_screenshot, snaps_path


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
            screenshot_path = capture_screenshot(setup, name="home_page_error")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e
        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(setup, name="home_page_success")
        print(f"Screenshot Path: {screenshot_path}")
        if os.path.exists(screenshot_path):
            print("Screenshot captured successfully.")
        else:
            print("Screenshot file not found.")
        allure.attach.file(screenshot_path, name="Direct_Date_Sucess", attachment_type=allure.attachment_type.PNG)

