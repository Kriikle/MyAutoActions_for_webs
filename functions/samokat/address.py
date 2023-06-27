import time

from selenium.webdriver.common.by import By


def input_address_on_map(driver, city, street, house, flat=None):
    """
    Функция ввода адреса на карте
    Если объект не найден вызовет ошибку
    :param driver:
    :param city:
    :param street:
    :param house:
    :param flat:
    :return:
    """
    time.sleep(3)
    elem_input_address = driver.find_element(By.XPATH, '//span[text()="Ввести адрес"]')
    elem_input_address.click()
    time.sleep(1)
    element_click_city = driver.find_element(By.XPATH, '//span[text()="' + city + '"]')
    element_click_city.click()
    elements_input = driver.find_elements(By.CLASS_NAME, '_textInput_fov91_1')
    for elem in elements_input:
        if elem.get_attribute('placeholder') == 'Улица и дом':
            elem_input_street_house = elem
            elem_input_street_house.send_keys(street + ', ' + str(house))
            time.sleep(5)
            element_click_street_house = driver.find_element(
                By.XPATH,
                '//span[text()="' + street + ', ' + str(house) + '"]'
            )
            element_click_street_house.click()
            time.sleep(1)
            element_click_accept_address = driver.find_element(By.XPATH, '//span[text()="Да, всё верно"]')
            element_click_accept_address.click()
            break
    if flat is not None:
        elements_input = driver.find_elements(By.CLASS_NAME, '_textInput_fov91_1')
        for elem in elements_input:
            if elem.get_attribute('placeholder') == 'Квартира или офис':
                elem_input_flat = elem
                elem_input_flat.send_keys(str(flat))
    elem_save_address_click = driver.find_element(By.XPATH, '//span[text()="Сохранить"]')
    elem_save_address_click.click()


def input_first_address(driver, city, street, house, flat=None):
    """
    Функция ввода адреса для не авторизованного пользователя (первого адреса)
    :param driver: Объект драйвер
    :param city: Название города
    :param street: Название улицы
    :param house: Номер дома
    :param flat: Номер квартиры
    :return: void
    """
    elem_address_select = driver.find_element(By.CLASS_NAME, '_control_8rylp_4')
    elem_address_select.click()
    input_address_on_map(driver, city, street, house, flat=None)


def input_new_address(driver, city, street, house, flat=None):
    """
    Функция ввода адреса для авторизованного пользователя у которого есть хотя бы один адрес
    :param driver: Объект драйвер
    :param city: Название города
    :param street: Название улицы
    :param house: Номер дома
    :param flat: Номер квартиры
    :return: void
    """
    elem_address_select = driver.find(By.CLASS_NAME, '_icon_1c7va_1 CartHeader_chevron__6tRBV')
    elem_address_select.click()
