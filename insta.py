from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome
driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
time.sleep(3)

# Login
driver.find_element(By.NAME, 'username').send_keys('insta@123')  # Replace with your username
driver.find_element(By.NAME, 'password').send_keys('insta@#$%')  # Replace with your password
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(7)

# Navigate to post
driver.get('https://www.instagram.com/p/CwMfpUrNzrY/')
time.sleep(5)

# Click "View all comments"
try:
    view_comments = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'View all comments')]"))
    )
    view_comments.click()
    time.sleep(2)
except:
    print("All comments already visible or button not found")

# Scroll and like comments
def like_visible_comments():
    liked = 0
    comments = driver.find_elements(By.XPATH, "//ul/ul//li//button//*[name()='svg'][@aria-label='Like']/ancestor::button")
    for btn in comments:
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            btn.click()
            liked += 1
            print(f"❤️ Liked comment #{liked}")
            time.sleep(1)
        except Exception as e:
            print("⚠️ Failed to like:", e)
    return liked

def scroll_comments():
    scroll_area = driver.find_element(By.XPATH, "//ul[contains(@class, 'Mr508')]//ancestor::div[contains(@role,'dialog')]")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_area)
    time.sleep(2)

print("🚀 Starting auto-like on comments...")
previous_count = -1

while True:
    current_count = like_visible_comments()
    if current_count == previous_count:
        print("✅ No new comments found. Done.")
        break
    previous_count = current_count
    scroll_comments()

# Done
driver.close()
