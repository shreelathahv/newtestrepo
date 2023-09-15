#Handling dynamic checkboxes or radio buttons using selenium python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_options = Service("C:/Users/Vishwanwnloads/chromedriver-win64/chromedriver-win64/msedgedriver.exe")
driver = webdriver.Chrome(service=service_options, options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

RadioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(RadioButtons))

for radio in RadioButtons:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break

#To verify hide/show assertions with .isdisplayed()
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()