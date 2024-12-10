import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
#5 secs is the max timeout
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(10)
products = driver.find_element(By.CLASS_NAME,'product-name').text
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedlist == actuallist
print(actuallist)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']" ).click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(5) p')
sum = 0
for price in prices:
    sum = sum + int(price.text)   #48 + 160
print(sum)
totalAmount = float(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == totalAmount

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
discountapplied = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(discountapplied)
discountPercent = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
print(discountPercent)
discountAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalAmount > discountAmt
print(discountAmt)

#time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()




time.sleep(10)
