import requests
import selenium
import pytest
from selenium import webdriver

@pytest.fixture
def open_browser():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    yield driver 
    driver.quit()
    