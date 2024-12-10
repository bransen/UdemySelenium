import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID,"autocomplete").send_keys("un")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(len(countries))

for country in countries:
    if country.text == "United States (USA)":
        country.click()
        break
#print(driver.find_element(By.ID,"autocomplete").text)
assert(driver.find_element(By.ID,"autocomplete").get_attribute("value")) == "United States (USA)"


time.sleep(10)