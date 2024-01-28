import allure
from pageobjects.authorization_page import AuthorizationPage


def test_authorization_form(driver):
    with allure.step("Перейти на страницу 'https://demoqa.com/automation-practice-form'"):
        page = AuthorizationPage(driver)
        page.navigate()

    with allure.step("1 Заполнить поле First Name произвольной строкой"):
        page.send_keys(page.input_first_name, 'Maria')

    with allure.step("2 Заполнить поле Last Name произвольной строкой"):
        page.send_keys(page.input_last_name, 'Adoevskaia')

    with allure.step("3 Заполнить поле Email строкой формата name@example.com"):
        page.send_keys(page.input_user_email, 'Adoevskaia@gmail.com')

    with allure.step("4 Выбрать любое значение в Gender с помощью переключателя"):
        page.click(page.label_female)

    with allure.step("5 Заполнить поле Mobile произвольными 10 цифрами"):
        page.send_keys(page.input_user_number, '79090909909')

    with allure.step("6 Заполнить поле Date of birth произвольной датой с помощью всплывающего календаря "):
        page.click(page.input_date_of_birth)
        page.select_by_visible_text(page.option_month, 'March')
        page.select_by_visible_text(page.option_year, '2007')
        page.set_option_datepicker_day(10, 'March')
        page.click(page.option_10_march)

    with allure.step("7 Заполнить поле Subjects произвольной строкой"):
        page.fill_in_subjects_field('English')

    with allure.step("8 Загрузить любое изображение в поле Picture"):
        page.upload_test_picture()

    with allure.step("9 Заполнить поле Current Address произвольной строкой"):
        page.send_keys(page.text_current_address, 'SAMARA')

    with allure.step("10 Выбрать любое значение в Select State с помощью выпадающего списка"):
        page.div_select_by_index(page.div_state, 1)

    with allure.step("11 Выбрать любое значение в Select City с помощью выпадающего списка"):
        page.div_select_by_index(page.div_city, 1)

    with allure.step("12 Нажать кнопку Submit"):
        page.click(page.button_city)

    with allure.step("Появилось всплывающее окно с заголовком Thanks for submitting the form"):
        pass

    with allure.step("В таблице на окне отображаются введенные ранее значени"):
        pass
