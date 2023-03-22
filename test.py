import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL of the webpage with the dropdown menu
url = 'https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax'

# Define the function to scrape the data for a given keyword
def scrape_data(keyword):
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # Navigate to the URL
    driver.get(url)

    # Wait for the dropdown menu to appear and select the specified keyword
    try:
        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search_param')))
        Select(dropdown).select_by_visible_text(keyword)
    except:
        print('Error: could not find the dropdown menu')
        driver.quit()
        return

    # Click the "Search" button to view the results for the selected keyword
    try:
        search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'submit')))
        search_button.click()
    except:
        print(f'Error: could not click the "Search" button for {keyword}')
        driver.quit()
        return

    # Wait for the results page to load
    time.sleep(5)

    # Find the "Pay Charges" button for each result and follow the link to the next page
    try:
        pay_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="btn btn-primary btn-sm"]')))
        for i, button in enumerate(pay_buttons):
            button.click()
            time.sleep(5)

            # Extract the data from the table on the page
            table = driver.find_element(By.TAG_NAME, 'table')
            df = pd.read_html(table.get_attribute('outerHTML'))[0]

            # Save the data to a CSV file for the current keyword
            filename = f'{keyword}_{i+1}.csv'
            df.to_csv(filename, index=False)

            # Return to the previous page to view the next result
            driver.back()
            time.sleep(5)
    except:
        print(f'Error: could not extract data for {keyword}')

    # Combine all the CSV files for the current keyword into a single file
    combined_filename = f'{keyword}_combined.csv'
    combined_df = pd.concat([pd.read_csv(f'{keyword}_{i+1}.csv') for i in range(len(pay_buttons))])
    combined_df.to_csv(combined_filename, index=False)

    # Quit the driver
    driver.quit()

# Define the list of keywords to scrape
keywords = ['Owner Name', 'Address', 'Connection ID']

# Scrape the data for each keyword
for keyword in keywords:
    scrape_data(keyword)