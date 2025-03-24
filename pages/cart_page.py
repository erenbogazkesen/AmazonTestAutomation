from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
     CART_BUTTON=(By.XPATH,"//a[@href='/cart?ref_=sw_gtc']")
     PRODUCT_NAME=(By.CLASS_NAME,"a-truncate-cut")
     DELETE_BUTTON=(By.XPATH,"//span[@class='a-icon a-icon-small-trash']")
     EMPTY_CART_MESSAGE=(By.ID,"sc-subtotal-label-activecart")
     HOME_PAGE_ICON=(By.ID,"nav-logo-sprites")
     def __init__(self, driver):
        super().__init__(driver)


     def go_to_cart_page(self):
         self.click(*self.CART_BUTTON)

     def get_product_title(self):
         return self.get_text(*self.PRODUCT_NAME)

     def delete_product(self):
         self.click(*self.DELETE_BUTTON)

     def empty_cart_message_is_displayed(self):
         return self.get_text(*self.EMPTY_CART_MESSAGE)

     def go_to_home_page(self):
         self.click(*self.HOME_PAGE_ICON)
