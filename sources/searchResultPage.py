from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchResult():

    def __init__(self, driver):
        self.driver = driver
        self.firstProduct_Locator = (By.XPATH, "(//div[@class = 'a-section aok-relative s-image-square-aspect'])[1]")

    def press_to_first_product(self):
        # firstProductElement = self.driver.find_element(*self.firstProduct_Locator)
        firstProductElement = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.firstProduct_Locator))
        firstProductElement.click()
