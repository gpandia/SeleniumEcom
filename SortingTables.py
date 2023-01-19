from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

browserSortVeggies=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
VeggieElements=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeggieElements:
    browserSortVeggies.append(ele.text)

originalBrowserSorted = browserSortVeggies.copy()

browserSortVeggies.sort()

assert browserSortVeggies == originalBrowserSorted