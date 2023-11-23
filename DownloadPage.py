from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys

class ReportDownload:
    def __init__(self, driver):
        self.driver = driver

    def click_generate_report(self):
        generate_report_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate report')]"))
        )
        print("Generate button is clicked")
        generate_report_button.click()

    def wait_for_report_generation(self):
        time.sleep(300)

    def find_matching_elements(self):
        return self.driver.find_elements(
            By.XPATH,
            "//a[contains(@class, 'bx--btn--primary') and contains(@href, '/api/command/report/download-report')]",
        )

    def click_last_matching_element(self, matching_elements):
        if matching_elements:
            last_matching_element = matching_elements[-1]
            last_matching_element.click()
        else:
            print("No matching files found.")
        print("Download successful")

    def wait_for_selection(self):
        time.sleep(10)

    def retrieve_file_name(self):
        response = requests.get(self.driver.current_url, stream=True)
        content_disposition = response.headers.get('Content-Disposition')
        filename = content_disposition.split("filename=")[-1] if content_disposition else 'downloaded_file'
        print(f"Downloaded file name: {filename}")

    def download_report(self):
        self.click_generate_report()
        self.wait_for_report_generation()
        matching_elements = self.find_matching_elements()
        self.click_last_matching_element(matching_elements)
        self.wait_for_selection()
        self.retrieve_file_name()
