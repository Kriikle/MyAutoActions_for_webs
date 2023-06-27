import time

import pandas as pd
from selenium.webdriver.common.by import By


def add_to_cart(driver, shop_list_num, path_to_list='data/samokat/shopping_lists/'):
    df = pd.read_csv(path_to_list+str(shop_list_num)+'.csv')
    elem_find = driver.find_element(By.CLASS_NAME, '_input_1pil0_25')
    for item in df.itertuples():
        elem_find.send_keys(item.product_name)
        time.sleep(3)
        elem_add = driver.find_element(By.CLASS_NAME, 'ProductCardActions_action__PEuo7')
        for i in range(int(item.count)):
            elem_add.click()
            time.sleep(3)
        elem_find.clear()

