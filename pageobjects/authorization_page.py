from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import TimeoutException
from pageobjects.basepage import BasePage
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
    button_submit = (By.XPATH, "//*[@id='submit']")

    select_div_option = (
        By.XPATH,
        "//*[contains(@id, 'select')][contains(@id, 'option')]",
    )

    option_year = (By.XPATH, "//select[contains(@class, 'year')]")
    option_month = (By.XPATH, "//select[contains(@class, 'month')]")
    option_day_of_month = (
        By.XPATH,
        "//div[contains(text(), '{}')][contains(@aria-label, '{}')]",
    )

    def navigate(self):
        try:
            self._driver.get("https://demoqa.com/automation-practice-form")
        except TimeoutException:
            pass

    def div_select_by_index(self, locator: tuple, index: int) -> str:
        select = self.find_element(locator)
        select.click()
        options = self.find_elements(self.select_div_option)
        value = options[index].text
        options[index].click()
        return value

    def fill_in_subjects_field(self, value: str):
        self.click(self.div_subjects_container)
        self.send_keys(self.input_subjects, value)
        options = self.find_elements(self.select_div_option)
        options[0].click()

    def upload_picture(self, locator: tuple, file_path: str):
        upload = self._driver.find_element(locator)
        upload.send_keys(file_path)

    def set_option_datepicker_day(self, day: str, month: str):
        self.option_day_of_month = (
            self.option_day_of_month[0],
            self.option_day_of_month[1].format(day, month),
        )

    def upload_test_picture(self):
        upload = self.find_element(self.input_upload_picture)
        upload.send_keys(str(BASE_DIR / "data/1.png"))

    def fill_in_datepicker(self, day: str, month: str, year: str):
        self.scroll_to_element(self.input_date_of_birth)
        self.click(self.input_date_of_birth)
        self.select_by_visible_text(self.option_month, str(month).capitalize())
        self.select_by_visible_text(self.option_year, str(year))
        self.set_option_datepicker_day(str(day), str(month).capitalize())
        self.click(self.option_day_of_month)
