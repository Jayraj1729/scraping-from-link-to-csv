import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys

driver = webdriver.Chrome()

# navigate to website
driver.get("https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax")
time.sleep(5)

#select dropodown and iterate through it

select = Select(driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[5]/div/select"))
options = select.options
for index in range(1, len(options) - 1):
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='testing']/ul[@class='dd']//li/a/span[text()='New Test']"))).click()
    select.select_by_index(index)
    #do stuff
    #WebDriverWait(driver, 5000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[7]/div/a[1]"))).click()
    
    
    #click search
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[7]/div/a[1]").click()
    time.sleep(10)
    
    
    #pay charges for loop


    # to identify the table rows
    r = driver.find_elements(By.XPATH, "//*[@id="aplicationSearchResults"]/tbody/tr[1]")
    print(r)
    # to identify table columns
    c = driver.find_elements(By.XPATH, "//*[@id="aplicationSearchResults"]/thead/tr/th")
    print(c)
    # to get row count with len method
    rc = len (r)
    # to get column count with len method
    #cc = len (c)
    # to traverse through the table rows excluding headers
    for i in range (2, rc + 1) :
        print("table row")
    # to traverse through the table column 
    #for j in range (1, cc + 1) :

    select = Select(driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[5]/div/select"))
    tablerow = select.tablerow 
    for i in range(1, len(tablerow)):
        print()
   
   
   
    #click next
    driver.find_element(By.XPATH, "/html/body/div/div/strong/div/div[4]/div/div[2]/div[4]/div/ul/li[4]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div/div/strong/div/div[4]/div/div[2]/div[4]/div/ul/li[4]").click()
    time.sleep(10)
    print("index.text")
