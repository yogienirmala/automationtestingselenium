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

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
options.add_argument("--windows-size-1920,1080")

# input skenario testing (1 passed dengan kondisi benar, 3 passed dengan kondisi negative)

Inputan = [
    ("testing_user", "password"),        #username salah, password salah > hasil test failed
    ("standard_user", "password"),       #username benar, password salah > hasil test failed
    ("testing_user", "secret_sauce"),    #username salah, password benar > hasil test failed 
]

# membuka Firefox dan maximize window

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # mengakses web demo
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.mark.positivetest     #untuk custom marker postive test  
def test_login_berhasil(setup):
    # input username dan password
    setup.find_element(by=By.ID, value="user-name").send_keys("standard_user")     #username benar
    password_login = setup.find_element(by=By.ID, value="password")
    password_login.send_keys("secret_sauce")                                        #password benar

    # klik button login
    button_login = setup.find_element(by=By.ID, value="login-button")
    button_login.click()
    time.sleep(5)

    # mengambil text berhasil login
    ValidText = setup.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/span").text

    # melakukan assert untuk memastikan muncul error dan tidak berhasil login
    assert ValidText == "Products"


@pytest.mark.negativetest     #untuk custom marker negative test 
@pytest.mark.parametrize('uname, pwd', Inputan)
def test_login_salah(setup, uname, pwd):
    # input username dan password
    setup.find_element(by=By.ID, value="user-name").send_keys(uname)
    password_login = setup.find_element(by=By.ID, value="password")
    password_login.send_keys(pwd)

    # klik button login
    button_login = setup.find_element(by=By.ID, value="login-button")
    button_login.click()
    time.sleep(5)
    
    # mengambil text gagal login
    InvalidText = setup.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text

    # melakukan assert untuk memastikan muncul error dan tidak berhasil login
    assert InvalidText == "Epic sadface: Username and password do not match any user in this service"