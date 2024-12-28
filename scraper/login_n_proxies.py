import csv
import time
import random
import requests
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

# Fetch proxies from ProxyScrape API
def fetch_proxies():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print("Error fetching proxies:", e)
        return []

# Set up Chrome options with proxy
def set_proxy(proxy):
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument(f'--proxy-server=http://{proxy}')
    return webdriver.Chrome(options=chrome_options)

# Initialize proxy list and starting proxy
proxy_list = fetch_proxies()
proxy_index = 0
start_time = time.time()

# Initialize WebDriver with the first proxy
driver = set_proxy(proxy_list[proxy_index])
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

# Step 2: Rotate through each link from the CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Define rotation interval and check if proxy needs to be changed
        rotation_interval = random.randint(300, 480)
        if time.time() - start_time > rotation_interval:
            driver.quit()
            proxy_index = (proxy_index + 1) % len(proxy_list)
            driver = set_proxy(proxy_list[proxy_index])
            stealth(driver,
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32"
            )
            start_time = time.time()
            login()  # Re-login after switching proxy

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
