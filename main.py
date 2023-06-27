# This is a sample Python script.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from functions.samokat.address import input_first_address

from functions.samokat.auth import login,logout

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('https://web.samokat.ru/')
    time.sleep(3)
    # login(browser, '9212341221')
    # time.sleep(3)
    # logout(browser)
    # input_first_address(browser, 'Санкт-Петербург', 'Каменноостровский проспект', '12', 93)
    # elem_find = browser.find_element(By.CLASS_NAME, '_input_1pil0_25')
    # elem_find.send_keys('Закуски к пиву')

    browser.quit()
