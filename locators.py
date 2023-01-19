from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# # Chrome
# service_obj = Service("F:/Hacking_courses/Cypress Projects/Selenium Automation/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# Locators
# ID, Xpath, CSSSelector, Classname, name, linkText

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1" ).send_keys("12356")
driver.find_element(By.ID,"exampleCheck1").click()
# tagname[attribute='value']- CSS selector
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Gokul");

# //tagname[@attribute='value']- Xpath
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

# Static Dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")


