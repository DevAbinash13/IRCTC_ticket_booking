import time
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import constants
from fixtures import browser
import locators
from constants import UsernamePasswords

class TestIrctcTicketCreation():
    def test_irctc_select_source_destination(self,browser):
        #initializing waits
        wait = WebDriverWait(browser, 10)
        browser.get("https://www.irctc.co.in/nget/train-search")
        browser.maximize_window()

        #from destination
        fromdest = wait.until(EC.presence_of_element_located((By.XPATH, locators.BookTicketPage.from_box)))
        fromdest.send_keys(UsernamePasswords.from_dest)

        #to destination
        todest= wait.until(EC.presence_of_element_located((By.XPATH, locators.BookTicketPage.to_box)))
        todest.send_keys(UsernamePasswords.to_dest)

        #selecting date
        date_dict = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
                     "07": "July", "08": "August", "09": "September", "10": "October", "11": "November",
                     "12": "December"}
        month = date_dict[constants.UsernamePasswords.date.split("/")[1]]
        month_locator = wait.until(EC.presence_of_element_located((By.XPATH,locators.BookTicketPage.month_name)))
        month_text = month_locator.text
        next_button = wait.until(EC.presence_of_element_located((By.XPATH,locators.BookTicketPage.next_button_on_calendar)))
        while True:
            if month != month_text:
                next_button.click()
            else:
                print("monthtext",month_text)
                break
        #click on the submit button
        wait.until(EC.presence_of_element_located((By.XPATH, locators.BookTicketPage.submit))).click()
