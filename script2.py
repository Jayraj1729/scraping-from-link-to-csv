import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax")

# Wait for the page to load
time.sleep(2)

# Initialize a list to hold the data for all dropdown options
all_data = []

# Get the dropdown element
dropdown_element = driver.find_element_by_id("searchBy")

# Get all the options in the dropdown
options = Select(dropdown_element).options

# Iterate over all the options
for i in range(1, len(options)):

    # Get the current option
    current_option = options[i]

    # Select the current option
    Select(dropdown_element).select_by_index(i)

    # Click the search button
    driver.find_element_by_id("searchBtn").click()

    # Wait for the results to load
    time.sleep(2)

    # Get the result table
    result_table = driver.find_element_by_id("taxRecordsTable")

    # Get all the rows in the table
    rows = result_table.find_elements_by_tag_name("tr")

    # Iterate over all the rows
    for row in rows:

        # Get the "Pay Charges" button for the current row
        pay_charges_button = row.find_element_by_css_selector("button[data-toggle='modal']")

        # Click the "Pay Charges" button
        pay_charges_button.click()

        # Wait for the next page to load
        time.sleep(2)

        # Get the data from the next page
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find("table", {"class": "table table-striped table-bordered table-hover"})
        rows = table.find_all("tr")
        data = []

        # Iterate over all the rows in the table and get the data
        for row in rows:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            data.append(cols)

        # Close the modal
        driver.find_element_by_css_selector(".modal-header button.close").click()

        # Wait for the modal to close
        time.sleep(1)

        # Append the data to the list for the current dropdown option
        all_data.append(data)

    # Write the data for the current dropdown option to a CSV file
    with open(f"{current_option.text}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for data in all_data:
            for row in data:
                writer.writerow(row)

    # Clear the list for the next dropdown option
    all_data = []

# Write the data for all dropdown options to a combined CSV file
with open("combined_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for data in all_data:
        for row in data:
            writer.writerow(row)

# Close the webdriver
driver.quit()
