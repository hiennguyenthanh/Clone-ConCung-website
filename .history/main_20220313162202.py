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

# prodName = driver.find_elements(By.CLASS_NAME,'item-title')
# prodPrice = driver.find_elements(By.CLASS_NAME,'product-price')


# for i in prodName:
#     cursor.execute("INSERT INTO PRODUCT VALUES (N'"+ i.text+"')")

# conn.commit()


# prodPrice = driver.find_elements(By.CLASS_NAME,'product-price')


# for i in prodPrice:
#     print(i.text)
# print(len(prodPrice))

prodName_arr = []
prodPrice_arr = []

ActionChains(driver).move_to_element(driver.find_element_by_css_selector('.footer')).perform()


prodName_el = driver.find_elements(By.CLASS_NAME,'item-title')
prodPrice_el = driver.find_elements(By.CLASS_NAME,'product-price')

# for i in prodName_el:
#     prodName_arr.append(i.text)


time.sleep(10)   
driver.close()
