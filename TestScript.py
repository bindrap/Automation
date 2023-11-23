from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from LoginPage import LoginPage
from UserPage import UserPage
from ReportingPage import ReportingPage
from DownloadPage import ReportDownload
from FileHandling import move_matching_file
import time
from config import chrome_driver_path, source_folder, destination_folder, username

# Set ChromeOptions and set the executable path
chrome_options = Options()
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)

# Create instances of page classes
login_page = LoginPage(driver)
user_page = UserPage(driver)
reporting_page = ReportingPage(driver)
download_page = ReportDownload(driver)

# Test script
login_page.open()
login_page.input_username(username)
login_page.click_next_button()
login_page.wait_for_login()

# Navigate to the User page
# Replace this part with actual navigation to the User page
time.sleep(5)

# Navigate to the Reporting page
# Replace this part with actual navigation to the Reporting page
user_page.click_reporting_link()
time.sleep(5)

# Interact with elements on the Reporting page
reporting_page.click_issued_permits_button()

# Select "Last year" in the dropdown
reporting_page.interact_with_dropdown(reporting_page.locate_dropdown("csv-date-range-select"), "previous-month")

# Click the "Select all" button
reporting_page.click_button(reporting_page.locate_button_by_text("Select all"))
reporting_page.click_button_by_title("Form fields (0 selected)")

time.sleep(5)

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

#element_title = "Other optional fields (0 selected)"  # The title of the element you want to click
#reporting_page.click_element_by_title(element_title)

# Click the "Select all" button
#reporting_page.click_button(reporting_page.locate_button_by_text("Select all"))

# Execute JavaScript to select the checkbox
#reporting_page.execute_js_to_select_checkbox("admin-reports:category17592186050415")

# Perform the report download using the ReportDownload class
download_page.download_report()

source_folder = r"C:\Users\bindrap\Downloads"
destination_folder = r"G:\MoveTest_Parteek"
# Move the downloaded file
move_matching_file(source_folder, destination_folder, "Issued permits")

# Continue your test interactions here
time.sleep(10)
# Close the browser
driver.quit()
