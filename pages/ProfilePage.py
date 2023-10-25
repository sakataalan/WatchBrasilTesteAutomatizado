from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ProfilePage(BasePage):
    BTN_SELECT_TEST_PROFILE = (By.XPATH, "//p[contains(text(), 'Teste')]")

    def __init__(self, driver):
        super().__init__(driver)

    def select_test_profile(self):
        self.click_element(self.BTN_SELECT_TEST_PROFILE)
     

   