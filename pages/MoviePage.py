from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MoviePage(BasePage):
    BTN_PLAY_MOVIE = (By.XPATH, "//*[@id='page']/div/app-page/div/section/app-movies-and-series/div[1]/app-series-banner/div/div[3]/div[4]/app-play-button/button/span")

    def __init__(self, driver):
        super().__init__(driver)

    def play_movie(self):
        self.click_element(self.BTN_PLAY_MOVIE)
        self.wait(10)