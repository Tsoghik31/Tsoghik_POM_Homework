# Without logging in to the amazon account search a product and click to the first result
import time
import unittest
from selenium import webdriver
from sources.navigationBar import NavigationBar
from sources.searchResultPage import SearchResult



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

    def test_search(self):
        self.navigationBar = NavigationBar(self.driver)
        self.navigationBar.fill_search_field("python books")
        self.navigationBar.press_to_search_button()


        self.searchResult = SearchResult(self.driver)
        self.searchResult.press_to_first_product()

    def tearDown(self) -> None:
        self.driver.close()
