import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# set up webdriver
driver = webdriver.Chrome()

# navigate to website
driver.get("https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax")

# wait for page to load
time.sleep(3)

# select dropdown
# select dropdown
dropdown = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/form/div[5]/div/select")
options = dropdown.find_elements_by_tag_name("option")


# create a list to store the data
all_data = []

# loop through each option in the dropdown
for i in range(1, len(options)):
    # select the option
    dropdown.select_by_index(i)
    
    # click the search button
    driver.find_element_by_id("submitSearch").click()
    
    # wait for results to load
    time.sleep(3)
    
    # get all "pay charges" buttons
    pay_buttons = driver.find_elements_by_xpath("//button[contains(text(), 'Pay Charges')]")
    
    # loop through each button and click it
    for button in pay_buttons:
        button.click()
        
        # switch to new window
        driver.switch_to.window(driver.window_handles[1])
        
        # get data from table
        table = driver.find_element_by_xpath("//table[@class='table table-striped table-bordered table-condensed table-hover']")
        rows = table.find_elements_by_tag_name("tr")
        
        # extract data from table rows
        data = []
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            row_data = []
            for cell in cells:
                row_data.append(cell.text)
            data.append(row_data)
            
        # add data to all_data list
        all_data.extend(data)
        
        # close window
        driver.close()
        
        # switch back to original window
        driver.switch_to.window(driver.window_handles[0])
    
    # write data to CSV file for this option
    with open(f"{options[i].text}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# write all data to combined CSV file
with open("all_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(all_data)

# close webdriver
driver.quit()
