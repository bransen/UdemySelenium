import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://bwd3108.cps.golf")
driver.maximize_window()
# ID, Xpath, CSSSelectory, Classname, name, linkText
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[contains(text(),'Sign In')]").click()
# driver.find_element(By.CLASS_NAME, "mat-button-focus-wrapper").click()
# driver.find_element(By.ID,"lastName").send_keys("Daniels")
driver.find_element(By.ID,"mat-input-1").send_keys("bransen.daniels@gmail.com")
# driver.find_element(By.ID,"userNumber").send_keys("4125555343")
# driver.find_element(By.ID,"subjectsContainer").send_keys("My subjects")
# driver.find_element(By.ID,"currentAddress").send_keys("2720 College Park Rd")
driver.find_element(By.XPATH,"//span[normalize-space()='NEXT']").click()
driver.find_element(By.ID,"mat-input-2").send_keys("SunnyDay2023!")
driver.find_element(By.XPATH,"//span[normalize-space()='SIGN IN']").click()
# driver.find_element(By.XPATH, "//label[@for ='gender-radio-1']").click()
# driver.find_element(By.XPATH, "//label[@for ='hobbies-checkbox-1']").click()
# driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
# message = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
# print(message)
# test
# //span[contains(text(),'Sign In')]
# Xpath example
# //tagname[@attribute='value'] -->  //input[@type= 'submit']
# //*[contains(text(), 'Your Text Here')]

# //button[@aria-haspopup='true' and contains(@class, 'mat-button') and .//span[contains(text(), 'Sign In')]]

# <span class="mat-button-wrapper"> Sign In </span>
# //label[@for='gender-radio-1' and text()='Male']
# //label[@for='gender-radio-1']


time.sleep(10)
