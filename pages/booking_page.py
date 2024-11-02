import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class booking:

    def __init__(self, setup):
        self.comment = None
        self.PDay = None
        self.wel_msg = None
        self.driver = setup

    def facility_hongkong(self):
        dropdown = Select(self.driver.find_element(By.TAG_NAME, "select"))
        time.sleep(5)
        dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    def facility_tokyo(self):
        dropdown = Select(self.driver.find_element(By.ID, "combo_facility"))
        time.sleep(3)
        dropdown.select_by_visible_text("Tokyo CURA Healthcare Center")

    def facility_seoul(self):
        dropdown = Select(self.driver.find_element(By.TAG_NAME, "select"))
        time.sleep(3)
        dropdown.select_by_visible_text("Seoul CURA Healthcare Center")

    def readmission(self):
        self.driver.find_element(By.CLASS_NAME, "checkbox-inline").click()

    def healthcare_medicare(self):
        self.driver.find_element(By.XPATH, "//input[@id='radio_program_medicaid']").click()
        if self.driver.find_element(By.XPATH, "//input[@id='radio_program_medicaid']").is_selected:
            print("Yes radio button is selected.")
        else:
            print("Yes radio button is not selected.")

    def healthcare_medicaid(self):
        self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").click()
        if self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").is_selected:
            print("Yes radio button is selected.")
        else:
            print("Yes radio button is not selected.")

    def healthcare_none(self):
        self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(3)").click()
        if self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(3)").is_selected:
            print("Yes radio button is selected.")
        else:
            print("Yes radio button is not selected.")

    def direct_date(self):
        self.driver.find_element(By.NAME, "visit_date").send_keys("10/12/2024")

    def yearmonth_picker(self):
        self.driver.find_element(By.XPATH, "//span[@class='glyphicon glyphicon-calendar']").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[class='datepicker-days'] th[class='datepicker-switch']").click()

        year = '2025'
        Month = "Dec"
        while True:
            Year = self.driver.find_element(By.CSS_SELECTOR,
                                            "div[class='datepicker-months'] th[class='datepicker-switch']").text
            Months = self.driver.find_elements(By.XPATH, "//span[@class='month']")
            if Year == year:
                for x in Months:
                    if x.text == Month:
                        x.click()
                        break
                break
            else:
                if Year > Year:
                    prev = self.driver.find_element(By.XPATH,
                                                    "//div[@class='datepicker-months']//th[@class='prev']").click()

                else:
                    ele = "//div[@class='datepicker-months']//th[@class='next'][normalize-space()='»']"
                    after = self.driver.find_element(By.XPATH, ele).click()

    def day_picker(self):
        self.PDay = "15"
        Days = self.driver.find_elements(By.XPATH, "//tbody//tr//td[@class='day']")
        for Day in Days:
            if Day.text == self.PDay:
                Day.click()
                break

    def health_issue(self):
        self.comment = "I'm attracting to the exquisite things in the world clearly."
        self.driver.find_element(By.ID, "txt_comment").send_keys(self.comment)
        time.sleep(5)
        self. driver.find_element(By.ID, "btn-book-appointment").click()

    def confirmation(self):
        time.sleep(5)
        confirmation = self.driver.find_element(By.XPATH, "//p[@class='lead']").text
        assert confirmation == "Please be informed that your appointment has been booked as following:", \
            "Please check your data"
