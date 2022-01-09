from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os,os.path

import time
options = Options()
options.headless = False

options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/martintin/Desktop/beat_generator/MIDI",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.set_window_size(1920, 1080)

def scrape_page(): 
  driver.get('https://bitmidi.com/random')
  driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div[4]/div[2]/p/a').click()

def main():
  for i in range(1):
    try:
      scrape_page()
    except:
      time.sleep(20)
    
main()

driver.quit()
