from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time
import selenium.webdriver.support.expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait

import allure
@allure.feature('Company Management')   
@allure.story('Company Management')
@allure.title('Test Company Management')
@allure.description('This test verifies the Company Management functionality in the dashboard.')
@allure.severity(allure.severity_level.NORMAL)

def test_company_management(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.load()
    time.sleep(5)  # Wait for the page to load
    login_page.enter_credentials()
    time.sleep(2)  # Wait for the credentials to be entered
    login_page.wait_for_captcha()
    time.sleep(2)  # Wait for the captcha to be solved
    print("✅ Credentials entered successfully")
    login_page.submit()
    time.sleep(5)  # Wait for the login to complete

    dashboard_page.go_to_company_management()
    time.sleep(5)  # Wait for the Company Management page to load
   
    
    
    
    assert dashboard_page.is_company_management_visible(), "❌ Company Management page not visible"
    print("✅ Navigated to Company Management page")
    
  
    