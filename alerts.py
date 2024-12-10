v
name = "Bransen"
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)

assert name in alerttext
alert.accept()


time.sleep(5)