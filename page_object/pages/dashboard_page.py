from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "(//h1[normalize-space()='Dashboard'])[1]")
        self.transactions_tab = (By.XPATH, "(//span[normalize-space()='Transactions'])[1]")
        self.event_tab = (By.XPATH, "(//span[normalize-space()='Events Management'])[1]")
        self.event_details = (By.XPATH, "(//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-gl123g'][normalize-space()='hello clone'])[1]")
        self.qr_code_management_tab = (By.XPATH, "(//span[normalize-space()='QR Code Management'])[1]")
        self.qr_code_management_header = (By.XPATH, "(//h1[normalize-space()='QR Management'])[1]")

    def is_dashboard_visible(self):
        return self.driver.find_element(*self.dashboard_header).is_displayed()

    def go_to_transactions(self):
        self.driver.find_element(*self.transactions_tab).click()
    
    def go_to_event_management(self):
        self.driver.find_element(*self.event_tab).click()
       
    def go_to_event_details(self):
        self.driver.find_element(*self.event_details).click()
    def is_qr_code_management_visible(self):
        return self.driver.find_element(*self.qr_code_management_header).is_displayed()
    def go_to_qr_code_management(self):
        self.driver.find_element(*self.qr_code_management_tab).click()
       