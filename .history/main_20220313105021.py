from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import copy
PATH = 'C:\Program Files (x86)\chromedriver.exe'
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(ser = Service(PATH),options=op)


url = 'https://concung.com/bim-ta-khuyen-mai-101635.htmlx'

driver.get(url)

productName = driver.find_elements(By.CLASS_NAME,'item-title')
# productPrice = driver.find_element(By.CLASS_NAME,'block-prices').text
for i in productName:
    print("-",len(i.text))
print(len(productName))
# print(productPrice)

# driver.close()
