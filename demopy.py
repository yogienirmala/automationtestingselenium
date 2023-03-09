# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
# inherit TestCase Class and create a new test class
class DemoblazeTest(unittest.TestCase):
 
    # initialization of webdriver (Firefox)
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    # Test case method. It should always start with test_
    def test_search_in_demoblaze(self):
         
        # get driver
        driver = self.driver
        # get url demoblaze using selenium
        driver.get("https://demoblaze.com")
 
        # assertion to confirm if title has STORE keyword in it
        self.assertIn("STORE", driver.title)

        # sign up ke web demoblaze store

        # driver.find_element(by=By.ID, value="signin2").click()
        # time.sleep(5)

        # input username dan password

        # driver.find_element(by=By.ID, value="sign-username").send_keys("testingyogie")
        # driver.find_element(by=By.ID, value="sign-password").send_keys("password123")
        # button_signup = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[3]/button[2]")
        # button_signup.click()

        # login ke web demoblaze store
        driver.find_element(by=By.ID, value="login2").click()
        time.sleep(5)

        # input username dan password
        driver.find_element(by=By.ID, value="loginusername").send_keys("testingyogie")
        password_login = driver.find_element(by=By.ID, value="loginpassword")
        password_login.send_keys("password123")

        # klik button login
        button_login = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[3]/button[2]")
        button_login.click()
        time.sleep(5)

        # memilih produk yang akan dimasukkan ke cartt
        product = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a")
        driver.execute_script("arguments[0].click();", product)
        time.sleep(5)

        # klik button add to cart
        driver.find_element(by=By.CSS_SELECTOR, value="a.btn").click()
        
        # klik button ok pada popup notifikasi
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        # mengakses menu cart
        driver.find_element(by=By.CSS_SELECTOR, value="#cartur").click()

        # klik button place order
        driver.find_element(by=By.CSS_SELECTOR, value="button.btn:nth-child(3)").click()
        time.sleep(5)

        # mengisi form place order
        driver.find_element(by=By.CSS_SELECTOR, value="#name").send_keys("Testing Yogie")
        driver.find_element(by=By.CSS_SELECTOR, value="#country").send_keys("Indonesia")
        driver.find_element(by=By.CSS_SELECTOR, value="#city").send_keys("Denpasar")
        driver.find_element(by=By.CSS_SELECTOR, value="#card").send_keys("1234567890")
        driver.find_element(by=By.CSS_SELECTOR, value="#month").send_keys("March")
        driver.find_element(by=By.CSS_SELECTOR, value="#year").send_keys("2023")

        # klik button purchase
        driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div[3]/button[2]").click()
       
        # locate element using XPATH (memastikan bahwa muncul pop up thankyou for purchase)
        button_ok = driver.find_element(by=By.XPATH, value="/html/body/div[10]/div[7]/div/button")
 
        # send data (klik button ok pada pop up berhasil purchase)
        button_ok.click()
        # button_ok.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
 
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()