from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "(//h1[normalize-space()='Dashboard'])[1]")
        self.transactions_tab = (By.XPATH, "(//span[normalize-space()='Transactions'])[1]")
        self.event_tab = (By.XPATH, "(//span[normalize-space()='Events Management'])[1]")

    def is_dashboard_visible(self):
        return self.driver.find_element(*self.dashboard_header).is_displayed()

    def go_to_transactions(self):
        self.driver.find_element(*self.transactions_tab).click()
    
    def go_to_event_management(self):
        self.driver.find_element(*self.event_tab).click()
        # Optionally, you can wait for the event management page to load
        # self.driver.implicitly_wait(10)  # Adjust the wait time as necessary
