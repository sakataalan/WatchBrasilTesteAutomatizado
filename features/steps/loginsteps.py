from behave import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from configuration.config import TestData
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.ProfilePage import ProfilePage
from pages.MoviePage import MoviePage
from webdriver_manager.chrome import ChromeDriverManager
from basestep import BaseStep

class LoginSteps(BaseStep):

    @given(u'Launch the browser')
    def launch_browser(context):
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
        context.driver.maximize_window()

    @when(u'Open the https://play.watch.tv.br/login/ website')
    def open_login_page(context):
        try:
            context.driver.get(TestData.URL)
            context.loginPage = LoginPage(context.driver)
            context.profilePage = ProfilePage(context.driver)
            context.dashboardPage = DashboardPage(context.driver)
            context.moviePage = MoviePage(context.driver)
            
        except:
            context.driver.close()
            assert False,"Test is failed in open login page section"

    @then(u'The login portal has been opened')
    def validate_login_page(context):
        try:
            context.loginPage.validate_login_page()
        except:
            context.driver.close()
            assert False, "Test is failed in validate login page title"

    @then(u'Provide the username "{user}" and password "{pwd}"')
    def enter_login_creds(context, user, pwd):
        try:
            context.loginPage.enter_login_credentials(user,pwd)
        except:
            context.driver.close()
            assert False, "Test is failed in enter login credentials"

    @then(u'Click on the Login button')
    def enter_login(context):
        try:
            context.loginPage.enter_login()
        except:
            context.driver.close()
            assert False, "Test is failed in enter login"

    @then(u'Login is failed and invalid credential error is displayed')
    def validate_invalid_login(context):
        try:
            context.loginPage.validate_invalid_login()
        except:
            context.driver.close()
            assert False, "Test is failed in validating valid login"

    @then(u'Provide the username "{user}"')
    def enter_login_creds(context, user):
        try:
            context.loginPage.enter_username(user)
        except:
            context.driver.close()
            assert False, "Test is failed in enter username"

    @then(u'Provide the password "{pwd}"')
    def enter_login_creds(context, pwd):
        try:
            context.loginPage.enter_password(pwd)
        except:
            context.driver.close()
            assert False, "Test is failed in enter password"

    @then(u'Login is failed and disable button is displayed')
    def validate_empty_username(context):
        try:
            context.loginPage.validade_disabled_login_button()
        except:
            context.driver.close()
            assert False, "Test is failed in validate empty username"

    @then(u'Select test profile')
    def select_test_profile(context):
        try:
            context.profilePage.select_test_profile()
        except:
            context.driver.close()
            assert False, "Test is failed in selecting test profile"

    @then(u'Select movie')
    def select_movie(context):
        try:
            context.dashboardPage.select_movie()
        except:
            context.driver.close()
            assert False, "Test has failed in selecting movie in dashboard"

    @then(u'Play Movie')
    def play_movie(context):
        try:
            context.moviePage.play_movie()
        except:
            context.driver.close()
            assert False, "Test has failed in playing movie in movie page"

    @then(u'Go to previous page')
    def previous_page(context):
        try:
            context.driver.execute_script("window.history.go(-1)")
        except:
            context.driver.close()
            assert False, "Test has failed in going to previous page"

    @then(u'Logout')
    def logout(context):
        try:
            context.dashboardPage.logout()
        except:
            context.driver.close()
            assert False, "Test has failed in logout"

    @then(u'Close the browser')
    def step_impl(context):
        context.driver.close()