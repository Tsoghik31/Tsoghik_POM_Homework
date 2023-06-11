from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogInPage():
    def __init__(self, driver):
        self.driver = driver
        self.userNameFieldLocator = (By.ID, "ap_email")
        self.continueButtonLocator = (By.ID, "continue")
        self.passwordFieldLocator = (By.ID, "ap_password")
        self.singInButtonLocator = (By.ID, "signInSubmit")
        self.greetingTextLocator = (By.ID, "nav-link-accountList-nav-line-1")


    def fill_username_field(self, username):
        # userNameFieldElement = self.driver.find_element(*self.userNameFieldLocator)
        userNameFieldElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.userNameFieldLocator))
        userNameFieldElement.clear()
        userNameFieldElement.send_keys(username)

    def press_to_continue_button(self):
        continueButtonElement = self.driver.find_element(*self.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password):
       # passwordFieldElement = self.driver.find_element(*self.passwordFieldLocator)
        passwordFieldElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.passwordFieldLocator))
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)

    def press_to_sign_in_button(self):
        singInButtonElement = self.driver.find_element(*self.singInButtonLocator)
        singInButtonElement.click()


    def get_greeting_text(self):
        greetingTextElement = self.driver.find_element(*self.greetingTextLocator)
        message = greetingTextElement.text
        return message
