from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query  = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=CZ78HY13BM0Q&sprefix=phon%2Caps%2C394&ref=nb_sb_noss_2")


elem = driver.find_element(By.CLASS_NAME, "puisg-row")
print(elem.text)


time.sleep(3)
driver.close()