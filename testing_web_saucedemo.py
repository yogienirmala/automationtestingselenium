from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest 
from _pytest import mark
from _pytest.mark.structures import Mark
import time

#Testing web https://www.saucedemo.com 

# membuka Firefox dan maximize window
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)


def test_login():
    # mengakses web demo
    driver.get("https://www.saucedemo.com/")

    # input username dan password
    driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
    password_login = driver.find_element(by=By.ID, value="password")
    password_login.send_keys("secret_sauce")

    # klik button login
    button_login = driver.find_element(by=By.ID, value="login-button")
    button_login.click()
    time.sleep(5)

def test_add_to_cart():
    # mengakses web demo dengan kondisi sudah login
    driver.get("https://www.saucedemo.com/inventory.html")

    # menambahkan barang ke cart
    driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-backpack").click()
    driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(by=By.ID, value="add-to-cart-test.allthethings()-t-shirt-(red)").click()

Inputan = [
    ("","",""),                       #test case failed, karena inputan kosong
    ("", "Testing", "123456"),        #test case failed, karena first name kosong
    ("Test", "", "123456"),           #test case failed, karena last name kosong
    ("Test", "Testing", ""),           #test case failed, karena postal code kosong
    ("Test", "Testing", "123456"),    #test case passed, data benar
]

@pytest.mark.parametrize('firstname, lastname, postalcode', Inputan)

def test_checkout(firstname, lastname, postalcode):
    # mengakses web demo dengan kondisi sudah add to cart beberapa item
    driver.get("https://www.saucedemo.com/inventory.html")
    
    # menuju ke halaman cart
    driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

    # klik button checkout
    driver.find_element(by=By.ID, value="checkout").click()

    # melengkapi form informasi
    driver.find_element(by=By.ID, value="first-name").send_keys(firstname)
    driver.find_element(by=By.ID, value="last-name").send_keys(lastname)
    driver.find_element(by=By.ID, value="postal-code").send_keys(postalcode)

    # klik button continue
    driver.find_element(by=By.ID, value="continue").click()

    # mengambil text berhasil checkout
    Overview = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/span").text

    # melakukan assert untuk memastikan checkout berhasil
    assert Overview == "Checkout: Overview"

    # klik button finish
    driver.find_element(by=By.ID, value="finish").click()

    # klik button back to home
    driver.find_element(by=By.ID, value="back-to-products").click()
