"""
File: web_crawler_dynamically_loaded.py
Name: Chia-Chun, Hung
-------------------------------------------------------
This script demonstrates how to scrape the full set of movie
ratings from IMDb's Top 250 movies page (www.imdb.com/chart/top),
which is dynamically loaded.

It uses Selenium to simulate browser behavior and scrolls through
the page to ensure all data is loaded before extracting content
using BeautifulSoup.

This task is relevant for data science projects that require:
- Handling JavaScript-rendered or infinite scroll web pages
- Extracting data from modern web applications
- Combining automation (Selenium) with HTML parsing (BeautifulSoup)
"""

from bs4 import BeautifulSoup

# 安裝 Selenium 套件，來去使用他底下的檔案、函數等等
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
	# Launch Chrome browser using Selenium
	driver = webdriver.Chrome()

	# Open IMDB Top 250 movies page
	driver.get('http://www.imdb.com/chart/top')

	# Wait for the page to load completely
	# Use explicit waits to wait for a specific element to be present
	try:
		element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
		WebDriverWait(driver, 5).until(element_present)
	except TimeoutException:
		print("Timed out waiting for page to load")

	# Extract the entire HTML content after the page finishes loading
	html_content = driver.page_source

	# Parse HTML using BeautifulSoup
	soup = BeautifulSoup(html_content)

	# Find all span tags that contain IMDB star rating
	tags = soup.find_all('span', {'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})

	# Count the number of movie ratings found (expecting 250)
	count = 0
	for tag in tags:
		count += 1
	print(count)


if __name__ == '__main__':
	main()
