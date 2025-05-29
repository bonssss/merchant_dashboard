import time
from selenium import webdriver
from pages.login_page import LoginPage
import allure
@allure.feature('Login Functionality')
@allure.story('User Login')
@allure.title('Test User Login')
@allure.description('This test verifies the user login functionality in the application.')
@allure.severity(allure.severity_level.NORMAL)
@allure.step('Starting the login test')

def test_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    with allure.step('Loading the login page'):
        print("Loading the login page...")
        login_page.load()
        time.sleep(5)
    with allure.step('Entering user credentials'):
        login_page.enter_credentials()
        time.sleep(2)
    with allure.step('Waiting for captcha to be solved'):
        print("Waiting for captcha to be solved...")
        
        login_page.wait_for_captcha()
        time.sleep(2)
    with allure.step('Submitting the login form'):
        login_page.submit()
        time.sleep(5)

    assert login_page.is_dashboard_displayed(), "❌ Login failed: Dashboard not found."
    print("✅ Login successful: Dashboard is displayed.")

    driver.quit()
