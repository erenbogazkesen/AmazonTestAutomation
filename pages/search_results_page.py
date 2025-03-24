from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    NUMBER_BAR=(By.XPATH,"//div[@class='a-section a-text-center s-pagination-container']")
    NUMBER_CONTAINER=(By.XPATH,"//a[@aria-label='2 sayfasına git']")
    PRODUCT=(By.XPATH, "(//a//img)[{}]")


    def __init__(self, driver):
        super().__init__(driver)

    def check_samsung_products(self):
        try:
            # Hata alma ihtimalimizi azaltmak için wait kullandık
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@aria-label, 'Samsung')]"))
            )

            # "Samsung" içeren ürün başlıklarını bul ve döndür
            return self.driver.find_elements(By.XPATH, "//h2[contains(@aria-label, 'Samsung')]")
        except:
            # Hata durumunda boş liste döndürmesini sağladık
            return []

    def check_number_bar_visible(self):
        return self.is_element_displayed(*self.NUMBER_BAR)

    def scroll_page(self):
        self.scroll_to_element(*self.NUMBER_BAR)

    def click_page_number(self):
      self.click(*self.NUMBER_CONTAINER)

    def click_product(self,number):
        product=(self.PRODUCT[0],self.PRODUCT[1].format(number))
        self.click(*product)

