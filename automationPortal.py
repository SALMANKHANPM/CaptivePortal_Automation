# Using Selenium Python Library to Automate the CaptivePortal of KLU.

## Packages  ##
# Selenium ,Chrome WebDriver
"""Source : https://github.com/SergeyPirogov/webdriver_manager#use-with-chrome """
import pwinput as pwd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


## Initialization ##
# Credentials
username = int(input("Enter Your Student ID No : "))
password = pwd.pwinput(prompt='Password: ', mask='*')

# Webdriver Installation & Launch
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


## Automating ##
# Captive Portal Login Page
driver.get("https://captiveportal.kluniversity.in/portal/login/")

# """Test WebPage"""
# driver.get("file:///C:/Users/bujji/OneDrive/Documents/Captive%20Portal%20Automation/CaptivePortal.html")

# # Bypass
# driver.find_element(by=By.ID, value="primary-button").click()

# Login Form fields
usr_name = driver.find_element(by=By.ID, value="id_username")
usr_pwd  = driver.find_element(by=By.ID, value="id_password")

# Submit button field
submit = driver.find_element(by=By.CLASS_NAME, value="submit")

# Sending input to the field
usr_name.send_keys(username)
usr_pwd.send_keys(password)

# Pressing the button
submit.click()
