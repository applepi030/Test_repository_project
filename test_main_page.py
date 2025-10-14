import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
   # page.go_to_login_page()
    #login_page = LoginPage(browser, link)
     #login_page.should_be_login_page()
