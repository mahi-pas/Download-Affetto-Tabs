import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
import os

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": os.path.join(os.getcwd(), "files")}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

hrefs = []

# Example usage: Open a webpage
driver.get("https://affettomnc.com/tabs/")

next_button = driver.find_element(By.CSS_SELECTOR, ".next-page a")
print (next_button)
while next_button:
    elems = driver.find_elements(By.CSS_SELECTOR, ".kboard-list-title a")
    for elem in elems:
        hrefs.append(elem.get_attribute("href"))
    next_button.click()
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, ".next-page a")
    except:
        break
    #next_button = None
# Go through and get hrefs

print(hrefs)
#save hrefs to a txt file
with open("hrefs.txt", "w") as f:
    for href in hrefs:
        f.write(href + "\n")


file_links = []
for href in hrefs:
    driver.get(href)
    try:
        download_buttons = driver.find_elements(By.CSS_SELECTOR, ".kboard-button-action.kboard-button-download")
        print(download_buttons)
        for b in download_buttons:
            attr = b.get_attribute("onclick")
            # Example attr:
            #"window.location.href='/tabs/?pageid=1&uid=530&action=kboard_file_download&kboard-file-download-nonce=527cf90edd&file=file1'"
            file_links.append("https://affettomnc.com"+attr.split("'")[1])
    except:
        print("No download button")
        continue
print(file_links)
#save file_links to a txt file
with open("file_links.txt", "w") as f:
    for link in file_links:
        f.write(link + "\n")

# Close the browser
driver.quit()