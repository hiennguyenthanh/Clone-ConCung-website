from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import copy
PATH = 'C:\Program Files (x86)\chromedriver.exe'
ser = Service(PATH)
op = webdriver.ChromeOptions()
op.add_argument("--user-data-dir=C:\\Users\\hieun\AppData\\Local\\Google\\Chrome\\User Data")
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ser, options=op)

driver = webdriver.Chrome(PATH)

url = 'https://concung.com/'

driver.get(url)

productName = driver.find_element(By.CLASS_NAME,'item-title').text
driver.quit()
