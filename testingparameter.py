from selenium import webdriver
import pytest

driver = webdriver.Firefox()
driver.maximize_window()

Alamat = [
    ("https://www.google.com", "Google"),
    ("https://demoblaze.com", "STORE")
]

@pytest.mark.parametrize('address, result', Alamat)

def test_bukaweb(address,result):
    driver.get(address)
    Title = driver.title

    assert Title == result