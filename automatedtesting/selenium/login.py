# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime

# Start the browser and login with standard_user

def login (user, password):
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    input_username = driver.find_element(By.ID, 'user-name')
    input_password = driver.find_element(By.ID, 'password')
    btn_login = driver.find_element(By.ID, 'login-button')

    input_username.send_keys(user)
    input_password.send_keys(password)
    btn_login.click()

    product_label = driver.find_element(By.XPATH, "//*[@id='header_container']/div[@class='header_secondary_container']/span[@class='title']")
    assert product_label.text == 'PRODUCTS'

    print('{}: Login with username {} and password {} successfully'.format(datetime.now(), user, password))

    return driver
