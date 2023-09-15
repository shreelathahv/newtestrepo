#Handling Java/Java script or Browser based alers in Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Shreelatha"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("C:/Users/Vishwanwnloads/chromedriver-win64/chromedriver-win64/msedgedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)       # using #name gets the css_selector
driver.find_element(By.ID, "alertbtn").click()
alerts = driver.switch_to.alert         #need to switch to alert mode from browser mode to read the alert message or work on alerts
alertText = alerts.text
print(alertText)
assert name in alertText
alerts.accept()         #is to accept or ok the alert message box
#alerts.dismiss()        #is to cancel the alert message box



