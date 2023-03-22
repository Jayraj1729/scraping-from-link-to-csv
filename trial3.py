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
#get current window handle
p = driver.current_window_handle

select = Select(driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[5]/div/select"))
options = select.options
for index in range(1, len(options) - 1):
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='testing']/ul[@class='dd']//li/a/span[text()='New Test']"))).click()
    select.select_by_index(index)
    #do stuff
    #WebDriverWait(driver, 5000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[7]/div/a[1]"))).click()
    
    
    #click search
    driver.find_element(By.XPATH , "/html/body/div/div/div/div/div/div[3]/form/div[7]/div/a[1]").click()
    time.sleep(10)

     # to identify the table rows
    r = driver.find_elements(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/table/tbody/tr")
    print(len(r))
    # to identify table columns
    c = driver.find_elements(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/table/thead/tr/th")
    print(len(c))
    # to get row count with len method
    #rc = len (r)
    #print(rc)
    #iterate the loop
    for i in range(1,len(r)):
        #clicks on pay charges
        driver.find_element(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/table/tbody/tr["+str(i)+"]/td[11]/select/option[2]").click()
        #switches back to main windowgit
        driver.switch_to.window(p)
        time.sleep(10)
        print("hello")