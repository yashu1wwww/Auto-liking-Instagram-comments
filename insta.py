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
driver.get('https://www.instagram.com/p/CwMfpUrNzrY/') #Change the URL of the Instagram comments you like..

#it will like from 1st cmt to 10th cmt..

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/span/div/div/div/div'))) 
element.click()                                              

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/span/div/div/div/div'))) 
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[4]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[5]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[6]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[7]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[8]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[9]/div/div[2]/div[2]/span/div/div/div/div')))
element.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/div[10]/div/div[2]/div[2]/span/div/div/div/div'))) 
element.click()

driver.close()




