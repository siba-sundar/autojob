import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from form_filling import fill_form  # Import the form-filling function
import pyautogui

# Function to simulate typing with a delay between each character
def type_like_human(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.2, 0.4))  # Slower typing to mimic human behavior

# Function to move mouse randomly
def move_mouse_randomly():
    pyautogui.moveTo(random.randint(100, 800), random.randint(100, 600), duration=random.uniform(0.5, 1.5))

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)

# Apply stealth to avoid bot detection
stealth(driver,
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32"
)

# Step 1: Log in to the website
def login():
    driver.get("https://internshala.com/login/user")
    time.sleep(random.uniform(3, 6))  # Adjust delay

    # Locate email, password fields, and login button
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login_submit")

    # Type credentials
    type_like_human(email_input, "luffy18122003@gmail.com")  # Replace with your email
    time.sleep(random.uniform(2, 4))
    type_like_human(password_input, "password18122003")  # Replace with your password
    time.sleep(random.uniform(2, 4))

    # Click login
    login_button.click()
    time.sleep(random.uniform(6, 10))  # Adjust delay to mimic real behavior

login()

# Step 2: Visit each link from the CSV file
with open('scraper\data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Visit each link in the CSV
        link = row['link']
        driver.get(link)
        move_mouse_randomly()  # Simulate human-like mouse movement
        time.sleep(random.uniform(3, 5))  # Delay to mimic page interaction

        print("Visited:", driver.title)  # Confirm page title

        # Step 3: Fill out the form
        fill_form(driver)  # Use the imported form-filling function

# Close browser after completing all tasks
driver.quit()
