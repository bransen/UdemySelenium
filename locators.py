import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
# ID, Xpath, CSSSelectory, Classname, name, linkText

driver.find_element(By.ID, "firstName").send_keys("Bransen")
driver.find_element(By.ID, "lastName").send_keys("Daniels")
driver.find_element(By.ID, "userEmail").send_keys("hello@gmail.com")
driver.find_element(By.ID, "userNumber").send_keys("4125555343")
# driver.find_element(By.ID,"subjectsContainer").send_keys("My subjects")
driver.find_element(By.ID, "currentAddress").send_keys("2720 College Park Rd")

# driver.find_elemet(By.)

driver.find_element(By.XPATH, "//label[@for ='gender-radio-1']").click()
driver.find_element(By.XPATH, "//label[@for ='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
message = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
print(message)
# test

# Xpath example
# //tagname[@attribute='value'] -->  //input[@type= 'submit']


# //label[@for='gender-radio-1' and text()='Male']
# //label[@for='gender-radio-1']


time.sleep(20)
