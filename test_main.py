import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixtures import browser
import locators
from constants import UsernamePasswords

class TestIrctcTicketCreation():
    def test_irctc_select_source_destination(self,browser):
        browser.get("https://www.irctc.co.in/nget/train-search")
        browser.find_element(By.XPATH, locators.BookTicketPage.from_box).send_keys(UsernamePasswords.from_dest)
        browser.find_element(By.XPATH, locators.BookTicketPage.to_box).send_keys(UsernamePasswords.to_dest)
        browser.find_element(By.XPATH, locators.BookTicketPage.submit).click()
