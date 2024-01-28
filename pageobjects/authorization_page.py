from pageobjects.basepage import BasePage
from selenium.webdriver.common.by import By
from data.consts import BASE_DIR


class AuthorizationPage(BasePage):
    input_first_name = (By.CSS_SELECTOR, "#firstName")
    input_last_name = (By.CSS_SELECTOR, "#lastName")
    input_user_email = (By.XPATH, "//*[@id='userEmail']")
    label_female = (By.XPATH, "//label[contains(., 'Female')]")
    input_user_number = (By.XPATH, "//*[@id='userNumber']")
    input_date_of_birth = (By.XPATH, "//*[@id='dateOfBirthInput']")
    div_subjects_container = (By.XPATH, "//div[@id='subjectsContainer']")
    input_subjects = (By.XPATH, "//div[@id='subjectsContainer']//input")
    input_upload_picture = (By.XPATH, "//*[@id='uploadPicture']")

    text_current_address = (By.XPATH, "//*[@id='currentAddress']")
    div_state = (By.XPATH, "//*[@id='state']")
    div_city = (By.XPATH, "//*[@id='city']")
    button_city = (By.XPATH, "//*[@id='submit']")

    select_div_option = (By.XPATH, "//*[contains(@id, 'select')][contains(@id, 'option')]")

    option_year = (By.XPATH, "//select[contains(@class, 'year')]")
    option_month = (By.XPATH, "//select[contains(@class, 'month')]")
    option_10_march = (By.XPATH, "//div[contains(text(), '{}')][contains(@aria-label, '{}')]")

    def navigate(self):
        self._driver.get('https://demoqa.com/automation-practice-form')

    def div_select_by_index(self, locator: tuple, index: int):
        select = self.find_element(locator)
        select.click()
        options = self.find_elements(self.select_div_option)
        options[index].click()

    def fill_in_subjects_field(self, value: str):
        self.click(self.div_subjects_container)
        self.send_keys(self.input_subjects, value)
        options = self.find_elements(self.select_div_option)
        options[0].click()

    def upload_picture(self, locator: tuple, file_path: str):
        upload = self._driver.find_element(locator)
        upload.send_keys(file_path)

    def set_option_datepicker_day(self, day: str, month: str):
        self.option_10_march = (self.option_10_march[0], self.option_10_march[1].format(day, month))

    def upload_test_picture(self):
        upload = self.find_element(self.input_upload_picture)
        upload.send_keys(str(BASE_DIR / 'data/1.png'))


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get("http://url-of-the-dropdown.com")

# # Найдите выпадающий список по его имени или идентификатору
# select = Select(driver.find_element_by_name('name-of-the-dropdown'))

# # Выберите опцию по видимому тексту
# select.select_by_visible_text('Option Text')

# # Выберите опцию по индексу
# select.select_by_index(index)

# # Выберите опцию по значению
# select.select_by_value('value')

# driver.quit()