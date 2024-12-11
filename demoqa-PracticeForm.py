import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
time.sleep(1)
#Static Dropdown
dropdown = Select(driver.find_element(By.XPATH,"//div[contains(text(),'Select State'"))
dropdown.select_by_visible_text("Saab")



//div[contains(text(),'Select State')]

time.sleep(20)