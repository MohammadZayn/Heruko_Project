from pages.login_page import Login
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

class Test_Appointment_Tokyo:
    @allure.title("#Test_Case -1")
    @allure.description("Booking the Tokyo country appointment")
    @allure.tag("Integration", "#1", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_1")
    def test_tokyo(self, setup):
        self.hp = Home(setup)
        self.lp = Login(setup)

        try:
            self.hp.home()
            self.hp.logo()
            self.lp.login_cred()

        except Exception as e:
            # Capture screenshot if there's an exception
            screenshot_path = capture_screenshot(setup, "home_page_error")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

        # Capture and attach screenshot after certain actions
        screenshot_path = capture_screenshot(setup, "home_page_success")
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
