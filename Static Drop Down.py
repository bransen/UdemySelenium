import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://bwd3108.cps.golf")
driver.maximize_window()
# ID, Xpath, CSSSelectory, Classname, name, linkText
time.sleep (3)
driver.find_element(By.XPATH,"//span[@class='mat-button-wrapper']").click()

driver.find_element(By.ID,"mat-input-1").send_keys("bransen.daniels@gmail.com")
time.sleep (3)
driver.find_element(By.XPATH,"//span[normalize-space()='NEXT']").click()
time.sleep (3)

driver.find_element(By.ID,"mat-input-2").send_keys("SunnyDay2023!")
driver.find_element(By.XPATH,"//span[normalize-space()='SIGN IN']").click()
time.sleep (3)

dropdown = Select(driver.find_element(By.XPATH,"//div[@id='mat-select-value-5']"))
dropdown.select_by_index(1)

time.sleep(20)