from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO = (By.ID, "nav-logo-sprites")
    SEARCH_BOX=(By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON=(By.ID, "nav-search-submit-button")
    def __init__(self, driver):
        super().__init__(driver)

    def is_on_home_page(self):
        return self.is_element_displayed(*self.LOGO)

    def search_product(self,product):
        self.click(*self.SEARCH_BOX)
        self.send_keys(*self.SEARCH_BOX,product)
        self.click(*self.SEARCH_BUTTON)
