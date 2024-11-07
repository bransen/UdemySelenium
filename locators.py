import time


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
#ID, Xpath, CSSSelectory, Classname, name, linkText

driver.find_element(By.ID,"useremail").send_keys("hello@gmail.com")
driver.find_element(By.ID).send_keys("hello@gmail.com")

#test








time.sleep(10)