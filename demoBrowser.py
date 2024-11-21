import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://bwd3108.cps.golf")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(10)
