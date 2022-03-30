import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
user_name=input("Enter Username")
user_pass=input("Enter Password")
driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element_by_name("username").send_keys(user_name)
driver.find_element_by_name("password").send_keys(user_pass)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.close()
print("Test case has successfully completed")