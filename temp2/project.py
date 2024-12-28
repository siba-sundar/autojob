from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query  = "laptop"
file = 0
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=CZ78HY13BM0Q&sprefix=phon%2Caps%2C394&ref=nb_sb_noss_2")
    elems = driver.find_elements (By.CLASS_NAME, "puisg-row")
    print(f"{len(elems)} items found")
    # print(elem.text)

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file +=1


time.sleep(3)
driver.close()