from pages.login_page import LoginPage
from pages.wallet_card_page import WalletCardPage
import time
def test_wallet_card(driver):
    login_page = LoginPage(driver)
    wallet_card_page = WalletCardPage(driver)

    login_page.load()
    time.sleep(5)  # Wait for the page to load
    login_page.enter_credentials()
    time.sleep(2)  # Wait for the credentials to be entered
    login_page.wait_for_captcha()
    time.sleep(2)  # Wait for the captcha to be solved
    login_page.submit()
    time.sleep(5)  # Wait for the login to complete

  

    wallet_card_page.click_add_wallet_card()
    time.sleep(5)  # Wait for the Wallet & Card Management page to load
    assert wallet_card_page.is_wallet_card_visible(), "❌ Add Wallet Card button not visible"
    print("✅ Add Wallet Card button clicked successfully")
    # Add further assertions or actions as needed
    assert wallet_card_page.is_wallet_card_visible(), "❌ Wallet & Card Management page not visible"
    time.sleep(2)  # Wait for the Wallet & Card Management page to load
    print("✅ Navigated to Wallet & Card Management page")
    
    wallet_card_page.click_card_list()
    time.sleep(5)  # Wait for the card list to load
    print("✅ Card list clicked successfully")