import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import dotenv
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


def test_Login():
    driver = webdriver.Chrome()
    driver.get("https://merchantapp-dashboard.arifpay.org/")
    driver.maximize_window()
    time.sleep(5)
    # driver.implicitly_wait(10)
    phone_number = driver.find_element(By.XPATH, "(//input[@id=':r0:'])[1]")
    phone_number.send_keys(os.getenv("PHONE_NO"))
    time.sleep(2)
    password = driver.find_element(By.XPATH, "(//input[@id=':r1:'])[1]")
    password.send_keys(os.getenv("PASSWORD"))
    time.sleep(2)
    
    #handle the captcha
    input("Please solve the CAPTCHA and press Enter to continue...")
    # Wait for the user to solve the CAPTCHA
    # After solving the CAPTCHA, you can proceed with the login
    # Click the login button 
    login_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Sign in'])[1]")
    login_button.click()
    time.sleep(5)
    #assert
    element = driver.find_element(By.XPATH, "(//h1[normalize-space()='Dashboard'])[1]")
    assert element.is_displayed(), "Login failed, dashboard not displayed."
    print("Login successful, dashboard displayed.")

    driver.quit()