# This is a sample Python script.
import time
import functions.samokat as sm

from selenium import webdriver
from selenium.webdriver.common.by import By




if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('https://web.samokat.ru/')
    time.sleep(3)
    sm.input_first_address(browser, 'Санкт-Петербург', 'Каменноостровский проспект', '17', 93)
    time.sleep(3)
    sm.add_to_cart(browser, 1)

    # login(browser, '9212341221')
    # time.sleep(3)
    # logout(browser)
    #
    #

    # browser.quit()
