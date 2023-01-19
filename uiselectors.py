import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# service_obj = Service("F:/Hacking_courses/Cypress Projects/Selenium Automation/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if (checkbox.get_attribute("value")) == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radioButton in radioButtons:
    if (radioButton.get_attribute("value")) == "radio2":
        radioButton.click()
        assert radioButton.is_selected()
        break
