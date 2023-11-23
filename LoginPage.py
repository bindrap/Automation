from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://ca.cloudpermit.com/login')

    def input_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'input-email'))
        )
        username_field.send_keys(username)

    def click_next_button(self):
        next_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
        next_button.click()

    def wait_for_login(self):
        user_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Parteek Bindra')]"))
        )
        user_element.click()
