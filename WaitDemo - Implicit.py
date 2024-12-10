import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

#time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
#time.sleep(5)
discountapplied = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(discountapplied)
discountamt = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
print(discountamt)
#time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()




time.sleep(10)