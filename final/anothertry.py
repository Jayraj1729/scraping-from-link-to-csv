import time
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#driver mention
driver = webdriver.Chrome()

# navigate to website
driver.get("https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax")
#time.sleep(5)
#get current window handle
p = driver.current_window_handle


#locate the dropdown list
select = Select(driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[5]/div/select"))
options = select.options
print(select)
#iterate the dropdown list
for index in range(1, len(options) - 1):

    #open workbook and add worksheet
    workbook = xlsxwriter.Workbook('option{}.xlsx'.format(index))
    worksheet = workbook.add_worksheet()

    #select option and click search
    select.select_by_index(index)    
    driver.find_element(By.XPATH , "/html/body/div/div/div/div/div/div[3]/form/div[7]/div/a[1]").click()
    time.sleep(5)

    #show 100 entries
    driver.find_element(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/div[2]/div[2]/div/label/select/option[3]").click()
    time.sleep(5)


    # to identify the table rows
    r = driver.find_elements(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/table/tbody/tr")
    print(len(r))
    # to identify table columns
    c = driver.find_elements(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/table/thead/tr/th")
    print(len(c))

    check = driver.find_elements(By.CLASS_NAME, "paginate_button ")   
    p= len(check)
    print("number of pagitation blocks"+str(p)+":")

    for num_pages in range(1,p-2):
        #scraer code 

        driver.find_element(By.CSS_SELECTOR , "#aplicationSearchResults_next").click()
        time.sleep(5) 