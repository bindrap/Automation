from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time

class ReportingPage:
    def __init__(self, driver):
        self.driver = driver

    def click_issued_permits_button(self):
        try:
            issued_permits_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Issued permits')]"))
            )
            issued_permits_button.click()
            print("Clicked on 'Issued permits' button.")
        except TimeoutException:
            print("Timed out waiting for 'Issued permits' button to become clickable.")

    def locate_dropdown(self, dropdown_id):
        return self.driver.find_element(By.ID, dropdown_id)

    def interact_with_dropdown(self, dropdown_element, value):
        select = Select(dropdown_element)
        select.select_by_value(value)
        time.sleep(2)

    def locate_button_by_text(self, button_text):
        xpath = f"//button[contains(text(), '{button_text}')]"
        return self.driver.find_element(By.XPATH, xpath)

    def click_button(self, button_element):
        button_element.click()
        time.sleep(2)

    def execute_js_to_select_checkbox(self, checkbox_id):
        js_code = f'document.getElementById("{checkbox_id}").click()'
        self.driver.execute_script(js_code)
        time.sleep(2)

    def click_button_by_xpath(self, button_xpath):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, button_xpath))
            )
            button.click()
            print(f"Clicked on button with XPath: {button_xpath}")
        except TimeoutException:
            print(f"Timed out waiting for button with XPath: {button_xpath} to become clickable.")

    def click_button_by_title(self, button_title):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[@title='{button_title}']/parent::button"))
            )
            button.click()
            print(f"Clicked on button with title: {button_title}")
        except TimeoutException:
            print(f"Timed out waiting for button with title: {button_title} to become clickable.")
    
    def select_option_from_dropdown(self, dropdown_id, option_value):
        try:
            dropdown = Select(WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, dropdown_id))
            ))
            dropdown.select_by_value(option_value)
            print(f"Selected option with value: {option_value} from the dropdown with ID: {dropdown_id}.")
        except TimeoutException:
            print(f"Timed out waiting for the dropdown with ID: {dropdown_id} to become present or for option with value {option_value} to become selectable.")

    def click_button_by_class(self, button_class):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, button_class))
            )
            button.click()
            print(f"Clicked on button with class: {button_class}")
        except TimeoutException:
            print(f"Timed out waiting for button with class: {button_class} to become clickable.")
    
    def click_element_by_title(self, element_title):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[@title='{element_title}']/parent::span"))
            )
            element.click()
            print(f"Clicked on element with title: {element_title}")
        except TimeoutException:
            print(f"Timed out waiting for element with title: {element_title} to become clickable.")


