from selenium.webdriver.common.by import By

class UserPage:
    def __init__(self, driver):
        self.driver = driver

    def click_reporting_link(self):
        reporting_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Reporting')
        reporting_link.click()
