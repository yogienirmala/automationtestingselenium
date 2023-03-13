from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# input skenario testing (3 passed dengan kondisi negative)

Inputan = [
    ("testing_user", "password"),        #username salah, password salah > hasil test failed
    ("standard_user", "password"),       #username benar, password salah > hasil test failed
    ("testing_user", "secret_sauce"),    #username salah, password benar > hasil test failed 
]

# membuka Firefox dan maximize window
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.mark.parametrize('uname, pwd', Inputan)

def test_login(uname, pwd):
    # mengakses web demo
    driver.get("https://www.saucedemo.com/")

    # input username dan password
    driver.find_element(by=By.ID, value="user-name").send_keys(uname)
    password_login = driver.find_element(by=By.ID, value="password")
    password_login.send_keys(pwd)

    # klik button login
    button_login = driver.find_element(by=By.ID, value="login-button")
    button_login.click()
    time.sleep(5)
    
    # mengambil text gagal login
    InvalidText = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text

    # melakukan assert untuk memastikan muncul error dan tidak berhasil login
    assert InvalidText == "Epic sadface: Username and password do not match any user in this service"