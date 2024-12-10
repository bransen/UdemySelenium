import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
#5 secs is the max timeout
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

driver.find_elements()
#time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']" ).click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(5) p')
sum = 0
for price in prices:
    sum = sum + int(price.text)   #48 + 160
print(sum)
totalAmount = driver.find_element(By.CSS_SELECTOR,".totAmt")

assert sum != totalAmount

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
discountapplied = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(discountapplied)
discountamt = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
print(discountamt)
#time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()




time.sleep(10)