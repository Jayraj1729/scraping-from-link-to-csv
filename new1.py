import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)


#launch URL
driver.get("https://mohali.lgpunjab.gov.in/wtms/search/waterSearch/commonSearch/collecttax")
time.sleep(5)

#Select class for dropdown
l= driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[5]/div/select")
d= Select(l)
print('Options are: ')
#iterate over dropdown options
for opt in d.options:
#get option text
   print(opt.text)
   driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/form/div[7]/div/a[1]").click()
#browser quit
driver.quit()