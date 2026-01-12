from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()


    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)


    def select_custom_dropdown(self, dropdown_locator, option_text):
        wait = WebDriverWait(self.driver, 10)

        # click pe dropdown
        dropdown = wait.until(EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()

        # click pe opțiune
        option_locator = (By.XPATH, f"//div[@role='option' and normalize-space()='{option_text}']")
        option = wait.until(EC.element_to_be_clickable(option_locator))
        option.click()

