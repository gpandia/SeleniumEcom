from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# a[contains(@href,"shop")] a[href*='shop']
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName=product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div/label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
confirmationText=driver.find_element(By.CSS_SELECTOR,".alert-success").text
assert "Success! Thank you!" in confirmationText