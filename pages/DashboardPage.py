from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    BTN_SELECT_MOVIE = (By.XPATH, "//*[@id='page']/div/app-page/div/section/app-home-master/app-home/main/app-home-carousel/swiper/div[2]/div[2]/div/div[2]/div[1]/div/app-play-button/button")
    BTN_SELECT_DROPDOWN_MENU = (By.XPATH, "//*[@id='page']/div/app-page/div/app-header/nav/div[2]/img")
    BTN_LOGOUT = (By.XPATH, "//a[contains(text(), 'Sair')]")
    TXT_DASHBOARD = (By.XPATH, "//*[@id='page']/div/app-page/div/app-header/nav/div[2]/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def select_movie(self):
        self.click_element(self.BTN_SELECT_MOVIE)
    
    def logout(self):
        self.click_element(self.BTN_SELECT_DROPDOWN_MENU)
        self.click_element(self.BTN_LOGOUT)
    
    def validate_page_loaded(self):
        assert self.get_element_text(self.TXT_DASHBOARD) == "Olá Teste, qual vai ser o play de hoje?"