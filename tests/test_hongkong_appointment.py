from PageObjects.Appointment import appointment

class Test_Automation:
    site_url = "https://katalon-demo-cura.herokuapp.com/"

    def test_Appointment(self, setup):
        self.driver = setup
        self.driver.get(self.site_url)

        self.ap = appointment(self.driver)
        self.ap.login_cred()
        self.ap.facility1()
        self.ap.readmission()
        self.ap.health_prog1()
        self.ap.direct_date()
        self.ap.health_issue()
        self.ap.confirmation()
        self.ap.quit()
