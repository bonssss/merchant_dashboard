from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "(//h1[normalize-space()='Dashboard'])[1]")
        self.transactions_tab = (By.XPATH, "(//span[normalize-space()='Transactions'])[1]")
        self.event_tab = (By.XPATH, "(//span[normalize-space()='Events Management'])[1]")
        self.event_details = (By.XPATH, "(//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1tyocmc'][normalize-space()='Sat Oct 18 2025'])[2]")
        self.qr_code_management_tab = (By.XPATH, "(//span[normalize-space()='QR Code Management'])[1]")
        self.qr_code_management_header = (By.XPATH, "(//h1[normalize-space()='QR Management'])[1]")
        self.company_management_tab =(By.XPATH, "(//span[normalize-space()='Company Management'])[1]")
        self.company_management_header = (By.XPATH, "(//h1[normalize-space()='ETH-SWITCH Configuration'])[1]")
        self.sales_tab = (By.XPATH, "(//span[normalize-space()='Sales Agent Management'])[1]")
        self.sales_header = (By.XPATH, "(//h1[normalize-space()='Sales Management'])[1]")
        self.merchnant_management_tab = (By.XPATH, "(//span[normalize-space()='Merchant Management'])[1]")
        self.merchnant_management_header = (By.XPATH, "(//h1[normalize-space()='Merchant Management'])[1]")
        self.pending_merchant= (By.XPATH, "(//button[normalize-space()='Pending Approval (1)'])[1]")
        self.report_tab = (By.XPATH,"(//span[normalize-space()='Reporting & Analytics'])[1]")
        self.generate_report_button =(By.XPATH,"(//button[normalize-space()='Generate Report'])[1]")

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
    def is_company_management_visible(self):
        return self.driver.find_element(*self.company_management_header).is_displayed()
    def go_to_company_management(self):
        self.driver.find_element(*self.company_management_tab).click()
        
    def is_sales_management_visible(self):
        return self.driver.find_element(*self.sales_header).is_displayed()
        
    def go_to_sales_management(self):
        self.driver.find_element(*self.sales_tab).click()
        
    def is_merchant_management_visible(self):
        return self.driver.find_element(*self.merchnant_management_header).is_displayed()
    def go_to_merchant_management(self):
        self.driver.find_element(*self.merchnant_management_tab).click()
    def go_to_pending_merchant(self):
        self.driver.find_element(*self.pending_merchant).click()
    def go_to_report(self):
        self.driver.find_element(*self.report_tab).click()
    def go_to_generate_report(self):
        self.driver.find_element(*self.generate_report_button).click()