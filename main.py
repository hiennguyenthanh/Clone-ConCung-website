from math import prod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

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
url = "https://concung.com/sua-bot-101586.html"
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
    
# direct to each link to get Diapers info
# with open('Products/Diapers.txt', 'w', encoding='utf-8') as writer:
#     writer.write('[ \n')
#     for link in prodLinks:
#         driver.get(link)
#         time.sleep(1)
#         try:
#             Name = driver.find_element(By.CLASS_NAME,'product-name').text
#         except NoSuchElementException:
#             continue
#         Price = driver.find_element(By.CLASS_NAME,'product-price').text
#         Images = []
#         img_el = driver.find_elements(By.CSS_SELECTOR,'.slick-track >.slick-slide > div > .thumb-img > img')[:3]
#         for image in img_el:
#             Images.append(image.get_attribute('src'))

#         # prodRating = driver.find_element(By.CLASS_NAME,'product-name')

#         script = "document.querySelector('#content-product').scrollIntoView({behavior: 'smooth', block: 'end', inline: 'nearest'});"
#         driver.execute_script(script)
#         time.sleep(1)

#         tableRows = driver.find_elements(By.CSS_SELECTOR,'.table tbody tr')
        
#         Brand = ''
#         Origin = ''
#         Size = ''
#         Count = ''
#         Component = ''
#         UserGuide = ''
        
#         for i in tableRows:
#             if ('Thương hiệu' in i.text):
#                 Brand = i.text.replace('Thương hiệu ','')
#                 continue
#             if ('Xuất xứ sản phẩm' in i.text):
#                 Origin = i.text.replace('Xuất xứ sản phẩm ','')
#                 continue
#             if ('Trọng lượng sản phẩm' in i.text):
#                 Size = i.text.replace('Trọng lượng sản phẩm (size) ','')
#                 continue
#             if ('Độ tuổi phù hợp' in i.text):
#                 Count = i.text.replace('Độ tuổi phù hợp ','')
#                 continue
#             if ('Thành phần' in i.text):
#                 Component = i.text.replace('Thành phần ','')
#                 continue
#             if ('Hướng dẫn sử dụng' in i.text):
#                 UserGuide = i.text.replace('Hướng dẫn sử dụng ','')
#                 continue
#         script ="document.querySelector('.text-center > .btn').click();"
#         driver.execute_script(script)
#         time.sleep(1)
#         Description = driver.find_element(By.CLASS_NAME,'content-product').text
#         # write to file
#         writer.write("{ \n")
#         writer.write('"Name":' + '"' + Name + '"' + ',\n')
#         writer.write('"Price":' + '"' + Price + '"' + ',\n') 
#         writer.write('"Images":' + '[')
#         for image in Images:
#             writer.write( '"' + image + '"' ',')
#         writer.write( '] ,\n')
#         writer.write('"Brand":' + '"' + Brand + '"' + ',\n')
#         writer.write('"Origin":' + '"' + Origin + '"' + ',\n')
#         writer.write('"Size":' + '"' + Size + '"' + ',\n')
#         writer.write('"Count":' + '"' + Count + '"' + ',\n')
#         writer.write('"Component":' + '"' + Component + '"' + ',\n')
#         writer.write('"UserGuide":' + '"' + UserGuide + '"' + ',\n')
#         writer.write('"Description":'+ '"' + Description+ '"' + ',\n')
#         writer.write("},\n")
#     writer.write('] \n')
# --------------------------------------------------------------------------------------------
# direct to each link to get Diapers info
with open('Products/MilkPowder.txt', 'w', encoding='utf-8') as writer:
    writer.write('[ \n')
    for link in prodLinks:
        driver.get(link)
        time.sleep(1)
        try:
            Name = driver.find_element(By.CLASS_NAME,'product-name').text
        except NoSuchElementException:
            continue
        Price = driver.find_element(By.CLASS_NAME,'product-price').text
        Images = []
        img_el = driver.find_elements(By.CSS_SELECTOR,'.slick-track >.slick-slide > div > .thumb-img > img')[:3]
        for image in img_el:
            Images.append(image.get_attribute('src'))

        # prodRating = driver.find_element(By.CLASS_NAME,'product-name')

        script = "document.querySelector('#content-product').scrollIntoView({behavior: 'smooth', block: 'end', inline: 'nearest'});"
        driver.execute_script(script)
        time.sleep(1)

        tableRows = driver.find_elements(By.CSS_SELECTOR,'.table tbody tr')
        
        Brand = ''
        Origin = ''
        Weight = ''
        Age = ''
        Component = ''
        UserGuide = ''
        Description =''

        for i in tableRows:
            if ('Thương hiệu' in i.text):
                Brand = i.text.replace('Thương hiệu ','')
                continue
            if ('Xuất xứ sản phẩm' in i.text):
                Origin = i.text.replace('Xuất xứ sản phẩm ','')
                continue
            if ('Trọng lượng sản phẩm' in i.text):
                Weight = i.text.replace('Trọng lượng sản phẩm (kg) ','')
                continue
            if ('Độ tuổi phù hợp' in i.text):
                Age = i.text.replace('Độ tuổi phù hợp ','')
                continue
            if ('Thành phần' in i.text):
                Component = i.text.replace('Thành phần ','')
                continue
            if ('Hướng dẫn bảo quản' in i.text):
                UserGuide = i.text.replace('Hướng dẫn bảo quản ','')
                continue
        script ="document.querySelector('.text-center > .btn').click();"
        driver.execute_script(script)
        time.sleep(1)

        try:
            Description = driver.find_element(By.CLASS_NAME,'content-product').text
        except NoSuchElementException:
            Description = ''
        # write to file
        writer.write("{ \n")
        writer.write('\t"Name":' + '"' + Name + '"' + ',\n')
        writer.write('\t"Price":' + '"' + Price + '"' + ',\n') 
        writer.write('\t"Images":' + '[')
        for image in Images:
            writer.write( '"' + image + '"' ',')
        writer.write( '""] ,\n')
        writer.write('\t"Brand":' + '"' + Brand + '"' + ',\n')
        writer.write('\t"Origin":' + '"' + Origin + '"' + ',\n')
        writer.write('\t"Weight":' + '"' + Weight + '"' + ',\n')
        writer.write('\t"Age":' + '"' + Age + '"' + ',\n')
        writer.write('\t"Component":' + '"' + Component + '"' + ',\n')
        writer.write('\t"UserGuide":' + '"' + UserGuide + '"' + ',\n')
        writer.write('\t"Description":'+ '"' + Description+ '"' + ',\n')
        writer.write("},\n")
    writer.write('] \n')
driver.close()

