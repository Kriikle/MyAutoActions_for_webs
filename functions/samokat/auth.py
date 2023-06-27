import time

from selenium.webdriver.common.by import By


def login(driver, phone_number):
    """
    Функция авторизации в самокате
    :param driver:
    :param phone_number: Телефонный номер без (+7)
    :return:
    """
    elem_login_button = driver.find_element(By.XPATH, '//span[text()="Войти"]')
    elem_login_button.click()
    elem_phone_input = driver.find_element(By.CLASS_NAME, '_textInput_fov91_1')
    elem_phone_input.send_keys(phone_number)
    time.sleep(1)
    elem_get_code_button = driver.find_element(By.XPATH, '//span[text()="Получить код"]')
    elem_get_code_button.click()
    code = int(input('Введите код из сообщения: '))
    elem_inputs_code = driver.find_elements(By.XPATH,
                                            "//div[contains(@class, 'VerificationCodeInput_control__gqxuX')]//child::*")
    elem_inputs_code[0].send_keys(code)


def logout(driver):
    """
    Выйти
    :param driver:
    :return:
    """
    driver.find_element(By.XPATH, '//span[text()="Профиль"]').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//span[text()="Выйти"]').click()
    driver.find_element(By.XPATH, '//span[text()="Ухожу"]').click()
