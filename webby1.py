from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os,os.path
options = Options()
options.headless = True #

options.add_experimental_option("prefs", {
  "download.default_directory": r"/Users/martintin/Desktop/beat_generator/MIDI",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.set_window_size(1920, 1080)
midi = []
mp3 = []

def scrape_page(): 
	links = []
	duplicates = []
	table = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/table')
	rows = table.find_elements_by_tag_name("tr")
	rows.pop(0)
	for row in rows:
		column = row.find_elements_by_tag_name("td")[0].find_elements_by_tag_name("a")
		for cell in column:    
			links.append(cell.get_attribute('href'))
	
	for i in links:
		if links.count(i) != 1:
			links.remove(i)

	print(links)
	for link in links:
		print(link)
		driver.get(link) 
		try:
			driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[1]/table/tbody/tr[3]/td/a').click() 
		except:
			pass
		time.sleep(6)
		print(len([name for name in os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')]))


def main():
	i = 1
	driver.get(f'https://www.cprato.com/en/midi/all?page={i}')
	driver.find_element_by_xpath('/html/body/div/div/a').click()
	scrape_page()
	while len([name for name in os.listdir('/Users/martintin/Desktop/beat_generator/MIDI')]) < 480:
		i += 1
		driver.get(f'https://www.cprato.com/en/midi/all?page={i}')
		scrape_page()

main()
driver.quit()
