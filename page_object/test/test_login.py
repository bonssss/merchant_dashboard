import time
from selenium import webdriver
from pages.login_page import LoginPage

def test_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    login_page.load()
    time.sleep(5)
    login_page.enter_credentials()
    time.sleep(2)
    login_page.wait_for_captcha()
    login_page.submit()
    time.sleep(5)

    assert login_page.is_dashboard_displayed(), "❌ Login failed: Dashboard not found."
    print("✅ Login successful: Dashboard is displayed.")

    driver.quit()
