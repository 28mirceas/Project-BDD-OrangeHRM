from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DashboardPage(BasePage):

    BUTTON_PIM = (By.XPATH, "//span[text()='PIM']")
    BUTTON_ADD = (By.XPATH, "//button[normalize-space()='Add']")
    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    BUTTON_SAVE = (By.XPATH, "//button[@type='submit']")
    PERSONAL_PAGE_NAME = (By.XPATH, "//h6")
    INPUT_EMPLOYEE_NAME = (By.XPATH, "//label[text()='Employee Name']/following::input[1]")
    BUTTON_SEARCH = (By.XPATH, "//button[normalize-space()='Search']")
    FIRST_ROW_RECORDS_TABLE = (By.XPATH,  "//div[contains(@class,'oxd-table-body')]//div[contains(@class,'oxd-table-row')][1]")
    RECORD_FIRST_NAME = (By.XPATH, ".//div[@role='cell'][3]//div")
    RECORD_LAST_NAME = (By.XPATH, ".//div[@role='cell'][4]//div")
    BUTTON_EDIT_PROFILE = (By.XPATH, "//div[contains(@class,'oxd-table-row')][1]//button[i[contains(@class,'bi-pencil-fill')]]")
    SELECT_NATIONALITY = (By.XPATH, "//label[text()='Nationality']/following::div[contains(@class,'oxd-select-text-input')][1]")
    SELECT_MARITAL_STATUS = (By.XPATH, "//label[text()='Marital Status']/following::div[contains(@class,'oxd-select-text-input')][1]")
    BUTTON_SAVE_PROFILE = (By.XPATH, "//div[contains(@class,'oxd-form-actions')]/button[@type='submit' and normalize-space()='Save']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_pim(self):
        self.click(self.BUTTON_PIM)

    def click_add(self):
        self.click(self.BUTTON_ADD)

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def click_save(self):
        self.click(self.BUTTON_SAVE)

    def verify_personal_page_name(self, expected_personal_page_name):
        return self.find(self.PERSONAL_PAGE_NAME).text == expected_personal_page_name

    #searchEmployee Scenario
    def set_employee_name(self, text):
        self.type(self.INPUT_EMPLOYEE_NAME, text)

    def click_search(self):
        self.click(self.BUTTON_SEARCH)
        self.wait.until(EC.visibility_of_element_located(self.FIRST_ROW_RECORDS_TABLE))

    def find_first_row(self):
        return self.find(self.FIRST_ROW_RECORDS_TABLE)

    def verify_record_first_name(self, expected_record_first_name):
        row = self.find_first_row()
        return row.find_element(*self.RECORD_FIRST_NAME).text == expected_record_first_name

    def verify_record_last_name(self, expected_record_last_name):
        row = self.find_first_row()
        return row.find_element(*self.RECORD_LAST_NAME).text == expected_record_last_name

    #editEmployeeProfile Scenario

    def click_edit_profile(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_ROW_RECORDS_TABLE))
        self.click(self.BUTTON_EDIT_PROFILE)

    def select_nationality(self, text):
        self.select_custom_dropdown(self.SELECT_NATIONALITY, text)

    def select_marital_status(self, text):
        self.select_custom_dropdown(self.SELECT_MARITAL_STATUS, text)

    def click_save_profile(self):
        self.click(self.BUTTON_SAVE_PROFILE)

    def get_selected_nationality(self):
        return self.find(self.SELECT_NATIONALITY).text.strip()

    def get_selected_marital_status(self):
        return self.find(self.SELECT_MARITAL_STATUS).text.strip()

    def verify_selected_nationality(self, expected_nationality):
        return self.get_selected_nationality() == expected_nationality

    def verify_selected_marital_status(self, expected_marital_status):
        return self.get_selected_marital_status() == expected_marital_status
