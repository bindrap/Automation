# Import necessary modules
from behave import given, when, then
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from LoginPage import LoginPage
from UserPage import UserPage
from ReportingPage import ReportingPage
from DownloadPage import ReportDownload
from FileHandling import move_matching_file
from config import chrome_driver_path, source_folder, destination_folder, username
import time

# Initialize global variables and page objects
driver = None
login_page = "https://ca.cloudpermit.com/login"
user_page = None
reporting_page = None
download_page = None

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    global driver, login_page
    chrome_options = Options()
    chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
    driver = webdriver.Chrome(options=chrome_options)
    login_page = LoginPage(driver)
    login_page.open()

@when('the user logs in with username "{user}"')
def step_user_logs_in(context, user):
    global login_page
    login_page.input_username(user)
    login_page.click_next_button()
    login_page.wait_for_login()

@when('navigates to the Reporting page')
def step_user_navigates_to_reporting_page(context):
    global user_page, reporting_page
    user_page = UserPage(driver)
    user_page.click_reporting_link()
    reporting_page = ReportingPage(driver)

@when('selects the required options on the Reporting page')
def step_user_selects_options(context):
    # Interact with elements on the Reporting page
    reporting_page.click_issued_permits_button()
    # Select "Last year" in the dropdown
    reporting_page.interact_with_dropdown(reporting_page.locate_dropdown("csv-date-range-select"), "previous-month")
    # Click the "Select all" button
    reporting_page.click_button(reporting_page.locate_button_by_text("Select all"))
    reporting_page.click_button_by_title("Form fields (0 selected)")
    reporting_page.select_option_from_dropdown("form-field-", "Permit Information for Principal Authority")
    time.sleep(5)
    reporting_page.select_option_from_dropdown("variable-source-field-", "1")
    reporting_page.click_button_by_class("bx--btn--tertiary")
    time.sleep(5)
    reporting_page.select_option_from_dropdown("form-field-", "Permit Information for Principal Authority")
    time.sleep(5)
    reporting_page.select_option_from_dropdown("variable-source-field-", "11")
    reporting_page.click_button_by_class("bx--btn--tertiary")
    time.sleep(5)
    reporting_page.select_option_from_dropdown("form-field-", "Permit Information for Principal Authority")
    time.sleep(5)
    reporting_page.select_option_from_dropdown("variable-source-field-", "10")
    reporting_page.click_button_by_class("bx--btn--tertiary")
    time.sleep(5)
    reporting_page.click_button_by_title("Other optional fields (0 selected)")
    time.sleep(10)
    checkbox_id = "admin-reports:field:reporting/construction-cost"  # The ID of the checkbox you want to click
    reporting_page.execute_js_to_select_checkbox(checkbox_id)
    # Click the first checkbox
    checkbox_id1 = "admin-reports:field:reporting/statcan-building-code"
    reporting_page.execute_js_to_select_checkbox(checkbox_id1)
    # Click the second checkbox
    checkbox_id2 = "admin-reports:field:reporting/statcan-work-code"
    reporting_page.execute_js_to_select_checkbox(checkbox_id2)

@when('generates the report')
def step_user_generates_report(context):
    global download_page
    reporting_page.click_issued_permits_button()
    # Your code to generate the report

@then('the report should be downloaded successfully')
def step_report_downloaded_successfully(context):
    global download_page
    download_page = ReportDownload(driver)
    download_page.download_report()

@then('the downloaded report should be moved to the destination folder')
def step_move_downloaded_report(context):
    global source_folder, destination_folder
    move_matching_file(source_folder, destination_folder, "Issued permits")

@then('close the browser')
def step_close_browser(context):
    global driver
    driver.quit()
