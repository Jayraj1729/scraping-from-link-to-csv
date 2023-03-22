import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize the webdriver
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

# navigate to the website
driver.get("https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax")

# wait for the locality dropdown to load
wait = WebDriverWait(driver, 10)
locality_dropdown = wait.until(EC.presence_of_element_located((By.NAME, "localityId")))

# get the options from the locality dropdown
locality_options = Select(locality_dropdown).options

# loop through each option in the locality dropdown
for i in range(1, len(locality_options)):
    # select the option from the dropdown
    Select(locality_dropdown).select_by_index(i)

    # click the search button
    search_button = driver.find_element_by_id("searchButton")
    search_button.click()

    # wait for the search results to load
    wait.until(EC.presence_of_element_located((By.ID, "applicationSearchResult")))

    # create a list to hold the data
    data_list = []

    # get the table rows
    rows = driver.find_elements_by_xpath("//table[@id='applicationSearchResult']/tbody/tr")

    # loop through each row in the table
    for row in rows:
        # get the columns
        columns = row.find_elements_by_tag_name("td")

        # check if the water charge due is not 0
        water_charge_due = float(columns[7].text.replace(",", ""))
        if water_charge_due > 0:
            # click the pay charges button
            action_dropdown = columns[8].find_element_by_class_name("actiondropdown")
            action_dropdown.click()
            pay_charges_button = columns[8].find_element_by_link_text("Pay Charges")
            pay_charges_button.click()

            # wait for the payment page to load
            wait.until(EC.presence_of_element_located((By.NAME, "amount")))

            # get the data from the payment page
            name = driver.find_element_by_id("name").text
            address = driver.find_element_by_id("address").text
            connection_id = driver.find_element_by_id("connectionId").text
            water_charges = driver.find_element_by_id("waterCharges").text
            arrears = driver.find_element_by_id("arrears").text
            total_charges = driver.find_element_by_id("totalCharges").text

            # add the data to the list
            data_list.append([name, address, connection_id, water_charges, arrears, total_charges])

            # go back to the search results page
            driver.back()

            # wait for the search results to load
            wait.until(EC.presence_of_element_located((By.ID, "applicationSearchResult")))

    # create a separate CSV file for each locality
    filename = locality_options[i].text + ".csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Address", "Connection ID", "Water Charges", "Arrears", "Total Charges"])
        writer.writerows(data_list)

# create a combined CSV file for all localities
#filename = "all_localities.csv"
#with open(filename, "w", newline="
