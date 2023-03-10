from selenium import webdriver
import pytest

driver = webdriver.Firefox()
driver.maximize_window()

#parameter yang digunakan alamat website
Alamat = [
    ("https://www.google.com", "Google"),
    ("https://demoblaze.com", "STORE")
]

@pytest.mark.parametrize('address, result', Alamat)

def test_bukaweb(address,result):
    driver.get(address)
    Title = driver.title

    assert Title == result