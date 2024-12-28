from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Keywords to enter into the search URL
keywords = ["ui ux", "web development"]

# Function to format keywords into URL-compatible string
def format_keywords(keywords):
    return ','.join(keyword.replace(' ', '-') for keyword in keywords)

# Initialize Chrome options and set incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Initialize WebDriver with incognito mode
driver = webdriver.Chrome(options=chrome_options)

# Format keywords into URL-compatible string
formatted_keywords = format_keywords(keywords)

# Visit each page using the formatted keywords
base_url = f"https://internshala.com/internships/{formatted_keywords}-internship/"

# Loop through the first 5 pages (adjust as needed)
for page in range(1, 6):
    if page == 1:
        url = base_url  # First page has no "page-#" in the URL
    else:
        url = f"{base_url}page-{page}/"  # Add pagination to URL

    # Visit the URL
    driver.get(url)
    print(f"Visiting: {url}")
    time.sleep(2)  # Wait for the page to load

    # Handle potential popup
    try:
        close_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ic-24-cross"))
        )
        close_button.click()
        print("Popup closed successfully.")
    except:
        print("No popup found or timeout reached.")

    # Extract the internship elements
    elems = driver.find_elements(By.CLASS_NAME, "individual_internship")
    print(f"{len(elems)} items found on page {page}")

    # Save each internship's HTML
    file = 0
    for elem in elems:
        internship_html = elem.get_attribute("outerHTML")
        with open(f"data/page_{page}_item_{file}.html", "w", encoding="utf-8") as f:
            f.write(internship_html)
        file += 1

    time.sleep(2)  # Wait between pages

# Close the browser after completion
driver.close()
