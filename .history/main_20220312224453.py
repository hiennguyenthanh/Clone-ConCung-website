from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import copy
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

url = 'https://concung.com/'

driver.get(url)

productName = driver.find_element(By.CLASS_NAME,'item-title font-weight-normal  ').text
driver.quit()
