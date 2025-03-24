from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    CART_BUTTON=(By.ID,"add-to-cart-button")
    ADDED_TO_CART_MESSAGE=(By.XPATH,"//h1[normalize-space()='Sepete eklendi']")
    PRODUCT_NAME=(By.ID,"productTitle")
    def __init__(self, driver):
        super().__init__(driver)


    def is_on_product_page(self):
        return self.is_element_displayed(*self.CART_BUTTON)

    def add_to_cart(self):
        self.click(*self.CART_BUTTON)

    def is_product_added_to_cart(self):
        return self.is_element_displayed(*self.ADDED_TO_CART_MESSAGE)

    def get_product_title(self):
        return self.get_text(*self.PRODUCT_NAME)