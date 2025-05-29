import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import allure
@allure.feature('Sales Management')
@allure.story('Sales Agent Management')
@allure.title('Test Sales Agent Management')
@allure.description('This test verifies the Sales Agent Management functionality in the dashboard.')
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
    
    
    # click sales tab
    dashboard_page.go_to_sales_management()
    time.sleep(5)
    # verify sales header
    assert dashboard_page.is_sales_management_visible(), "❌ Sales Management header not visible"
    print("✅ Sales Management header is visible")
    