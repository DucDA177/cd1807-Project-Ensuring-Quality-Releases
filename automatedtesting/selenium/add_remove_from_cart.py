from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import *
from datetime import datetime

def add_to_cart(driver, total_items):
    print ('Adding items to cart...')
    n_items = 0
    for i in range(total_items):
        try:
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            n_items = int(cart_badge)
        except NoSuchElementException:
            print("Cart is empty.")


        product_link = driver.find_element(By.ID, "item_" + str(i) + "_title_link")
        product_name = product_link.find_element(By.CLASS_NAME, "inventory_item_name").text
        product_link.click()

        product_name_2 = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        assert product_name == product_name_2

        add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
        add_to_cart_button.click()

        n_items += 1
        wait = WebDriverWait(driver, 10)
        new_cart_badge = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), str(n_items)))

        print('{}: {} added to cart.'.format(datetime.now(), product_name))
        print('Number of items in the cart: {}.'.format(n_items))

        driver.find_element(By.ID, "back-to-products").click()

    print ('{} items added to cart.'.format(n_items))


def remove_items(driver, total_items):
    print ('---------------------------')
    print ('Removing items from cart...')
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    n_items = int(cart_badge)
    for i in range(total_items):
        product_link = driver.find_element(By.ID, "item_" + str(i) + "_title_link")
        product_name = product_link.find_element(By.CLASS_NAME, "inventory_item_name").text
        product_link.click()

        product_name_2 = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        assert product_name == product_name_2

        remove_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
        remove_button.click()

        n_items -= 1
        wait = WebDriverWait(driver, 10)

        if n_items > 0:
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), str(n_items)))
        else:
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        print('{}: {} removed from cart.'.format(datetime.now(), product_name))
        print('Number of items in the cart: {}.'.format(n_items))

        driver.find_element(By.ID, "back-to-products").click()


if __name__ == "__main__":
    total_items = 6
    driver = login('standard_user', 'secret_sauce')
    add_to_cart(driver, total_items)
    remove_items(driver, total_items)
    driver.quit()

