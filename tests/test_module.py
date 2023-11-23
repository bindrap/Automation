import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from LoginPage import LoginPage
from UserPage import UserPage
from ReportingPage import ReportingPage
from DownloadPage import ReportDownload
from FileHandling import move_matching_file
from config import chrome_driver_path, source_folder, destination_folder, username
import pytest

@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.input_username(username)
    login_page.click_next_button()
    login_page.wait_for_login()

def test_navigate_to_reporting(browser):
    user_page = UserPage(browser)

    # Replace this part with actual navigation to the User page
    time.sleep(5)

    user_page.click_reporting_link()

def test_click_issued_permits(browser):
    reporting_page = ReportingPage(browser)
    reporting_page.click_issued_permits_button()

def test_select_last_year(browser):
    reporting_page = ReportingPage(browser)
    reporting_page.interact_with_dropdown(reporting_page.locate_dropdown("csv-date-range-select"), "last-year")

def test_select_all(browser):
    reporting_page = ReportingPage(browser)
    reporting_page.click_button(reporting_page.locate_button_by_text("Select all"))

def test_select_checkbox(browser):
    reporting_page = ReportingPage(browser)
    reporting_page.execute_js_to_select_checkbox("admin-reports:category17592186050415")

def test_download_report(browser):
    download_page = ReportDownload(browser)
    download_page.download_report()

def test_move_file():
    # No need for a browser fixture in this case
    move_matching_file(source_folder, destination_folder, "Issued permits")
