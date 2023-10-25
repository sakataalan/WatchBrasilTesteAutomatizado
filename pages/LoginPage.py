from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    TXT_EMAIL = (By.XPATH, "//input[@type='email']")
    TXT_PASSWORD = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.XPATH, "//button[@type='submit']")
    TXT_LOGIN_TEXT = (By.XPATH, "//*[@id='page']/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[1]/h3")
    TXT_FAILED_LOGIN_TEXT = (By.XPATH, "//*[@id='page']/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[3]/p")                 

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.input_element(self.TXT_EMAIL, user)
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_username(self,user):
        self.input_element(self.TXT_EMAIL, user)

    def enter_password(self, pwd):
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_login(self):
        self.click_element(self.BTN_LOGIN)

    def validate_login_page(self):
        assert self.get_element_text(self.TXT_LOGIN_TEXT) == "Entrar"

    def validate_invalid_login(self):
        assert self.get_element_text(self.TXT_FAILED_LOGIN_TEXT) == "E-mail ou senha incorreta." or \
               self.get_element_text(self.TXT_FAILED_LOGIN_TEXT) == "E-mail inválido."

    def validade_disabled_login_button(self):
        assert self.verify_button_is_disabled(self.BTN_LOGIN)

