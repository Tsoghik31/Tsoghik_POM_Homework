# Log in to the amazon account and make sure the right user is logged in using assertions

import time
import unittest
from selenium import webdriver
from sources.logInPage import LogInPage
from selenium.webdriver.support.wait import WebDriverWait

class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    def test_login_test(self):
        self.logInPage = LogInPage(self.driver)
        self.logInPage.fill_username_field("acompap@yahoo.com")
        self.logInPage.press_to_continue_button()
        self.logInPage.fill_password_field("Selenium!")
        time.sleep(2)
        self.logInPage.press_to_sign_in_button()
        time.sleep(20)

        assert self.logInPage.get_greeting_text() == "Hello, Selenium"


    def tearDown(self) -> None:
        self.driver.close()
