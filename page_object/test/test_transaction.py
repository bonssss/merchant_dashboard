import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
import allure
@allure.feature('QR Code Management')
@allure.story('QR Code Management')
@allure.title('Test QR Code Management')
@allure.description('This test verifies the QR Code Management functionality in the dashboard.')
@allure.severity(allure.severity_level.NORMAL)

def test_transaction(driver):
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

    dashboard_page.go_to_transactions()
    time.sleep(5)

    print("✅ Navigated to Transactions tab")
