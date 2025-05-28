from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.phone_input = (By.XPATH, "(//input[@id=':r0:'])[1]")
        self.password_input = (By.XPATH, "(//input[@id=':r1:'])[1]")
        self.login_button = (By.XPATH, "(//button[normalize-space()='Sign in'])[1]")
        self.dashboard_header = (By.XPATH, "(//h1[normalize-space()='Dashboard'])[1]")

    def load(self):
        self.driver.get("https://merchantapp-dashboard.arifpay.org/")
        self.driver.maximize_window()

    def enter_credentials(self):
        self.driver.find_element(*self.phone_input).send_keys(os.getenv("PHONE_NO"))
        self.driver.find_element(*self.password_input).send_keys(os.getenv("PASSWORD"))

    def wait_for_captcha(self):
        input("🧠 Please solve the CAPTCHA and press Enter to continue...")

    def submit(self):
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.dashboard_header).is_displayed()
