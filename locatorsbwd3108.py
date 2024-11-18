import time


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://bwd3108.cps.golf")
driver.maximize_window()
#ID, Xpath, CSSSelectory, Classname, name, linkText

time.sleep (3)
driver.find_element(By.XPATH, "//span[@class='mat-button-wrapper']").click()

driver.find_element(By.ID,"mat-input-1").send_keys("bransen.daniels@gmail.com")
time.sleep (3)
driver.find_element(By.XPATH, "//span[@class='mat-button-focus-overlay']").click()

#driver.find_element(By.ID,"lastName").send_keys("Daniels")
#driver.find_element(By.ID,"userEmail").send_keys("hello@gmail.com")
#driver.find_element(By.ID,"userNumber").send_keys("4125555343")
#driver.find_element(By.ID,"subjectsContainer").send_keys("My subjects")
#driver.find_element(By.ID,"currentAddress").send_keys("2720 College Park Rd")

#driver.find_elemet(By.)

#driver.find_element(By.XPATH, "//label[@for ='gender-radio-1']").click()
#driver.find_element(By.XPATH, "//label[@for ='hobbies-checkbox-1']").click()
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
#message = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
#print(message)
#test

#Xpath example
# //tagname[@attribute='value'] -->  //input[@type= 'submit']



#//label[@for='gender-radio-1' and text()='Male']
#//label[@for='gender-radio-1']




time.sleep(20)

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "login or register"))).click()