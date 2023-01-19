from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

# Chrome
service_obj = Service("F:/Hacking_courses/Cypress Projects/Selenium Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Firefox
# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'F:\Hacking_courses\Cypress Projects\Selenium Automation\geckodriver-v0.32.0-win32\geckodriver.exe', options=options)

driver.get("https://rahulshettyacademy.com")
while(True):
    pass
print(driver.title)
print(driver.current_url)
driver.close()
