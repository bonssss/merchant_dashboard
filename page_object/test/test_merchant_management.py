import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

import allure
@allure.feature('Event Management')     
@allure.story('Event Management')
@allure.title('Test Event Management')

@allure.description('This test verifies the Event Management functionality in the dashboard.')
@allure.severity(allure.severity_level.NORMAL)

def test_event(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.load()
    time.sleep(5)
    login_page.enter_credentials()
    time.sleep(2)
    login_page.wait_for_captcha()
    login_page.submit()
    time.sleep(5)

    assert dashboard_page.is_dashboard_visible(), "❌ Login failed, dashboard not visible"
    print("✅ Login successful")
    
    dashboard_page.go_to_merchant_management()
    time.sleep(5)
    
    assert dashboard_page.is_merchant_management_visible(), "❌ Merchant Management header not visible"
    print("✅ Merchant Management header is visible")
    
    
    dashboard_page.go_to_pending_merchant()
    time.sleep(5)
    