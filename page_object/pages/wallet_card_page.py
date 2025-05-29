from selenium.webdriver.common.by import By
class WalletCardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wallet_card_header = (By.XPATH, "(//h1[normalize-space()='Wallet & Card Management'])[1]")
        self.add_wallet_card_button = (By.XPATH, "(//span[normalize-space()='Wallet & Card Management'])[1]")
        self.card_list = (By.XPATH, "(//button[normalize-space()='Cards'])[1]")

    def is_wallet_card_visible(self):
        return self.driver.find_element(*self.wallet_card_header).is_displayed()

    def click_add_wallet_card(self):
        self.driver.find_element(*self.add_wallet_card_button).click()
        

    def click_card_list(self):
        self.driver.find_element(*self.card_list).click()