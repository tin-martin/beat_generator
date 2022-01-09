from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os,os.path
from datetime import *
import datetime


import time
options = Options()
options.headless = False

options.add_experimental_option("prefs", {
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.set_window_size(1920, 1080)

def main():
  while(True):
    driver.get("https://tms.managebac.com/student/classes/11843945/discussions/20504861")
    actual_time = datetime.datetime.now()
    time = datetime.strptime(actual_time, "%d/%m/%y %H:%M")
    print(str(time.hour,time.minute))
    if (str(time.hour,time.minute) == "3:35"):
      element_enter = _driver.findElement(By.xpath('//*[@id="new_reply"]/div[1]/div/div[2]'))
      element_enter.findElement(By.xpath("//html/body/div[1]/div[3]/div[1]/form/div/div/input")).sendKeys("football")

    
main()

driver.quit()
