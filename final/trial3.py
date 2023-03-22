import time
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys

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
for index in range(14, len(options) - 1):

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
    

    #iterate the loop
    for i in range(1,len(r)):
        #clicks on pay charges
        WebDriverWait(driver, 5000).until(EC.element_to_be_clickable(driver.find_element(By.XPATH , "/html/body/div/div/strong/div/div[4]/div/table/tbody/tr["+str(i)+"]/td[11]/select/option[2]"))).click()
        time.sleep(5)
        
        #child window switch to child window
        chwd = driver.window_handles
        for w in chwd:
            if(w!=p):
                driver.switch_to.window(w)
        
        #DATA APPEND
        #next page info 
        data_list1 = []
        for num in range(1,8):
            data2 = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[1]/div[2]/div["+str(num)+"]/div[2]").text
            data4 = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[1]/div[2]/div["+str(num)+"]/div[4]").text
            data_list1.append(data2)
            data_list1.append(data4)
            #print(data_list1)
       
        #data append exception in tr/td structure
        dataA = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div[1]/div[2]").text
        dataB = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div[1]/div[4]").text
        data_list1.append(dataA)
        data_list1.append(dataB)
        #print(data_list1)

        #data append next panel
        for num1 in range(2,4):
            data1 = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div["+str(num1)+"]/div[1]").text
            data3 = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div["+str(num1)+"]/div[3]").text
            data_list1.append(data1)
            data_list1.append(data3)
            #print(data_list1)

        #data append next panel exception tr/td struscure
        dataC = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div[4]/div[1]").text
        dataD = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div[4]/div[2]/div").text
        data_list1.append(dataC)
        data_list1.append(dataD)
        #print(data_list1)
        
        #data append next panel exception tr/td struscure
        for num1 in range(5,9):
            dataX = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div["+str(num1)+"]/div[1]").text
            dataY = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div["+str(num1)+"]/div[2]").text
            data_list1.append(dataX)
            data_list1.append(dataY)
            #print(data_list1)
        
        #data append next panel exception tr/td struscure
        dataE = driver.find_element(By.XPATH , "/html/body/div/div/div/div/strong/div/form/div[2]/div/div/div[2]/div[9]/div").text
        data_list1.append(dataE)
        print(data_list1)
        

        #write into excel
        #workbook = xlsxwriter.Workbook('temp1.xlsx')
        #worksheet = workbook.add_worksheet()
        worksheet.write_row(1+i,0,data_list1)
        
       
        #switches back to main window
        driver.switch_to.window(p)
        time.sleep(1)
        print("now next row in table")

    
    #workbook close
    workbook.close()