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

# for i in prodName:
#     cursor.execute("INSERT INTO PRODUCT VALUES (N'"+ i.text+"')")

# conn.commit()

prodLinks = []

#auto scroll to bottom of the page using element x to get full data needed

script_1 ="document.querySelector('#shop-box-app-open div div span').click();"
script_2 ="var x = document.createElement('div');"\
        "x.id = x;"\
        "document.body.appendChild(x);"\
        "x.scrollIntoView({behavior: 'smooth', block: 'end', inline: 'nearest'});"
driver.execute_script(script_1)
# give a 2 seconds break after closing the modal, to load top page data
time.sleep(1)
driver.execute_script(script_2)

prodLinks_el = driver.find_elements(By.CLASS_NAME,'line-clamp-2')

for item in prodLinks_el:
    prodLinks.append(item.get_attribute("href"))
    
Products = []
# direct to each link to get product info
for link in prodLinks:
    driver.get(link)
    time.sleep(1)
    prod = []
    Name = driver.find_element(By.CLASS_NAME,'product-name').text
    Price = driver.find_element(By.CLASS_NAME,'product-price').text
    # prodRating = driver.find_element(By.CLASS_NAME,'product-name')

    script = "document.querySelector('#content-product').scrollIntoView({behavior: 'smooth', block: 'end', inline: 'nearest'});"
    driver.execute_script(script)
    time.sleep(1)

    tableRows = driver.find_elements(By.CSS_SELECTOR,'.table tbody tr')
    
    Brand = ''
    Origin = ''
    Size = ''
    Count = ''
    Component = ''
    UserGuide = ''
    for i in tableRows:
        if ('Thương hiệu' in i.text):
            Brand = i.text.replace('Thương hiệu ','')
            prod.append(Brand)
            continue
        if ('Xuất xứ sản phẩm' in i.text):
            Origin = i.text.replace('Xuất xứ sản phẩm ','')
            prod.append(Origin)
            continue
        if ('Kích cỡ' in i.text):
            Size = i.text.replace('Kích cỡ (size) ','')
            prod.append(Size)
            continue
        if ('Số miếng' in i.text):
            Count = i.text.replace('Số miếng ','')
            prod.append(Count)
            continue
        if ('Thành phần' in i.text):
            Component = i.text.replace('Thành phần ','')
            prod.append(Component)
            continue
        if ('Hướng dẫn sử dụng' in i.text):
            UserGuide = i.text.replace('Hướng dẫn sử dụng ','')
            prod.append(UserGuide)
            continue
    Description = driver.find_element(By.CLASS_NAME,'content-product').text
    prod.append(Description)
   
    # brandOrigin = tableRows[1].text
    # Origin = tableRows[2].text
    # Size = tableRows[3].text
    # Count = tableRows[4].text
    # Component = tableRows[5].text

    Products.append(prod)
for i in Products:
    print(i)
driver.close()
