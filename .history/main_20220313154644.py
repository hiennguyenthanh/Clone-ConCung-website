from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import copy
import time
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-642FBA3\HIEN;'
                      'Database=ConCung;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()


PATH = 'C:\Program Files (x86)\chromedriver.exe'
op = webdriver.ChromeOptions()
ser = Service(PATH)
driver = webdriver.Chrome(service = ser,options=op)


url = 'https://concung.com/bim-ta-khuyen-mai-101635.html'


driver.get(url)

productName1 = driver.find_elements(By.CLASS_NAME,'line-clamp-2')

for i in productName1:
    cursor.execute("INSERT INTO PRODUCT VALUES (N'"+ i.text+"')")

conn.commit()
   

# productPrice = driver.find_element(By.CLASS_NAME,'block-prices').text
# for i in productName1:
#     print("-",i.text)
# print(len(productName1))
# print(productPrice)
time.sleep(5)   
driver.close()
