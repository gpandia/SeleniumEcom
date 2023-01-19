from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsOpened=driver.window_handles

driver.switch_to.window(windowsOpened[1])
emailTextLine=driver.find_element(By.CSS_SELECTOR,".im-para.red").text
emailText=emailTextLine.split(" ")[4]
driver.close()

driver.implicitly_wait(5)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(emailText)
driver.find_element(By.ID,"password").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)