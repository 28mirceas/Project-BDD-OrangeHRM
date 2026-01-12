from selenium.webdriver.common.by import By
from pages.base_page import BasePage

LOGIN_PAGE_URL = "https://opensource-demo.orangehrmlive.com"

class LoginPage(BasePage):

    #Login Page Locators
    INPUT_USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    INPUT_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    LOGIN_ERROR_TEXT = (By.XPATH, "//p[contains(@class,'alert-content-text')]")
    

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)

    def set_username(self, text):
        self.type(self.INPUT_USERNAME, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_button(self):
        self.click(self.BUTTON_LOGIN)

    def verify_new_url(self, expected_url):
        return self.driver.current_url == expected_url

    def verify_header_text(self):
        return self.find(self.DASHBOARD_HEADER).is_displayed()

    def verify_login_error_message_displayed(self, expected_text):
        return self.find(self.LOGIN_ERROR_TEXT).text == expected_text

    def get_current_url(self):
        return self.driver.current_url

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_button()




