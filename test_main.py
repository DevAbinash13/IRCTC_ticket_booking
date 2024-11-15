import requests
from selenium import webdriver
from fixtures import open_browser

class TestIrctcTicketCreation():
    def test_irctc_select_source_destination(self,open_browser):
        open_browser.get("https://www.irctc.co.in/nget/train-search")