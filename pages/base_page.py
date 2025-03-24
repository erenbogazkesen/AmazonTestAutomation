

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.action = ActionChains(driver)

    def get_current_url(self):
        return self.driver.current_url

    def go_to_url(self, url):
        self.driver.get(url)

    def get_text(self, by, locator):
        element = self.wait_for_visibility(by, locator)
        return element.text

    def wait_for_clickable(self, by, locator, timeout=15):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_visibility(self, by, locator, timeout=15):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def is_element_displayed(self, by, locator):
        try:
            element = self.wait_for_visibility(by, locator)
            return element.is_displayed()
        except:
            return False

    def click(self, by, locator):
        element = self.wait_for_clickable(by, locator)
        element.click()

    def send_keys(self, by, locator, text):
        element = self.wait_for_visibility(by, locator)
        element.send_keys(text)

    def scroll_to_element(self, by, locator):
        element = self.wait_for_clickable(by, locator)
        ActionChains(self.driver).scroll_to_element(element).perform()

