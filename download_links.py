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

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": os.path.join(os.getcwd(), "sheetmusic"),  # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Set up the Chrome driver
#service = Service('path/to/chromedriver')  # Update with the path to your chromedriver
driver = webdriver.Chrome(options=chrome_options)

# Create the download directory if it doesn't exist
if not os.path.exists('sheetmusic'):
    os.makedirs('sheetmusic')

# Read the links from file_links.txt
with open('file_links.txt', 'r') as file:
    links = file.readlines()

# Open each link to trigger the download
for link in links:
    driver.get(link.strip())
    #time.sleep(5)  # Wait for the download to start

# Close the browser
driver.quit()