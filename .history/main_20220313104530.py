from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import copy
PATH = 'C:\Program Files (x86)\chromedriver.exe'


driver = webdriver.Chrome(PATH)

url = 'https://concung.com/bim-ta-khuyen-mai-101635.htmlx'

driver.get(url)

productName = driver.find_elements(By.CLASS_NAME,'item-title')
# productPrice = driver.find_element(By.CLASS_NAME,'block-prices').text
for i in productName:
    print("-",i.text)
print(len(productName))
# print(productPrice)

driver.close()
