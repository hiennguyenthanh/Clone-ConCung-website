from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

url = 'https://concung.com/'

driver.get(url)
# print(driver.)
driver.quit()
