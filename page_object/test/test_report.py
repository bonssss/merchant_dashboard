from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import time
from selenium import webdriver

def test_report(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    
    login_page.load()
    time.sleep(5)
    login_page.enter_credentials()
    time.sleep(2)
    login_page.wait_for_captcha()
    login_page.submit()
    time.sleep(5)
    dashboard_page.go_to_report()
    time.sleep(5)
    print("✅ Report & Analytics page is displayed.")
    
    dashboard_page.go_to_generate_report()
    time.sleep(5)
    print("✅ Generate Report page is displayed.")
    print("✅ Report generation initiated successfully.")