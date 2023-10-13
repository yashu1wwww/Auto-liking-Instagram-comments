from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
import random

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
time.sleep(3)
driver.find_element_by_name('username').send_keys('insta@123') #replace with your insta username
time.sleep(1)
driver.find_element_by_name('password').send_keys('insta@#$%') #replace with your insta password
time.sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(6)
driver.get('https://www.instagram.com/p/CyEH1pGrB-k/') #Change the URL of the Instagram comments you like..
time.sleep(5)

while True:
    try:
        like_buttons = driver.find_elements_by_xpath("//span[@aria-label='Like']") #it will like the comments in the instagram post..
        like_buttons.click()
        
        time.sleep(3)  

    except Exception as e:
        print("An error occurred:", e)
        break  





