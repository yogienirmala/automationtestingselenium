from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# input skenario testing (3 failed, 1 passed)
Inputan = [
    ("yogie12345", "password"),         #username salah, password salah > hasil test failed
    ("yogietesting", "password"),       #username benar, password salah > hasil test failed
    ("yogie12345", "password123"),      #username salah, password benar > hasil test failed
    ("yogietesting", "password123")     #username benar, password benar > hasil test passed 
]

# membuka Firefox dan maximize window
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.mark.parametrize('uname, pwd', Inputan)

def test_login(uname, pwd):
    driver.get("https://demoblaze.com")
    
    # login ke web demoblaze store
    driver.find_element(by=By.ID, value="login2").click()
    time.sleep(5)

    # input username dan password
    driver.find_element(by=By.ID, value="loginusername").send_keys(uname)
    password_login = driver.find_element(by=By.ID, value="loginpassword")
    password_login.send_keys(pwd)

    # klik button login
    button_login = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[3]/button[2]")
    button_login.click()
    time.sleep(5)
    
    # mengambil text "Welcome (nama user)" > berhasil login
    Nameuser = driver.find_element(by=By.ID, value="nameofuser").text

    # melakukan assert untuk memastikan user telah berhasil login
    assert Nameuser == "Welcome yogietesting"