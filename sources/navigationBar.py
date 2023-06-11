from selenium.webdriver.common.by import By

class NavigationBar():
    def __init__(self, driver):
        self.driver = driver
        self.searchField_Locator = (By.ID, "twotabsearchtextbox")
        self.searchButton_Locator = (By.ID, "nav-search-submit-button")

    def fill_search_field(self, searchItem):
        searchFieldElement = self.driver.find_element(*self.searchField_Locator)
        searchFieldElement.clear()
        searchFieldElement.send_keys(searchItem)

    def press_to_search_button(self):
        searchButtonElement = self.driver.find_element(*self.searchButton_Locator)
        searchButtonElement.click()
