import allure
from pages.home_page import Home


class Test_Home:
    @allure.title("#Test_Case -4")
    @allure.description("Checking the home page and capturing the screenshot.")
    @allure.tag("Integration", "#4", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_4")
    def test_home(self, setup):
        self.ap = Home(setup)

        self.ap.home()
        self.ap.logo()