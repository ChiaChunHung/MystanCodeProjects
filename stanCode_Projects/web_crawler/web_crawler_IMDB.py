"""
File name: web_crawler.py
Name: Chia-Chun, Hung
-------------------------------------------------------
This script demonstrates how to perform web scraping on IMDB's Top 250 movies page.
It extracts and counts the number of movies released each year from the page using
HTTP requests and HTML parsing (via BeautifulSoup). Since the page is dynamically
loaded, only partial results can be retrieved without JavaScript simulation.

Skills practiced in this script are fundamental to data science workflows involving:
- Web scraping from public sites
- Parsing HTML content using BeautifulSoup
- Text cleaning and tag selection
- Frequency analysis with dictionaries
- Sorting dictionary results

Note: This version only retrieves the first 25 results due to IMDB’s dynamic content loading.
See 'web_crawler_dynamically_loaded.py' for a Selenium-based approach that scrolls the page.
"""


import requests  				# 引入此套件，來讓python可以對網站伺服器發送http request（讓pycharm可以連上網路）
from bs4 import BeautifulSoup   # bs4中的一個物件BeautifulSoup->幫我們把正個HTML變成一個物件，讓我們比較好找到目標


def main():
	# send a GET request to IMDB with a fake User-Agent header to bypass basic bot detection
	url = 'http://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)

	# Check HTTP response status; <Response [200]> means success
	print(response)

	# Convert the HTML response content to a string
	html = response.text

	# Parse HTML using BeautifulSoup
	soup = BeautifulSoup(html, features="html.parser")

	# Extract metadata from specific tags to consolidate year info per movie
	tags = soup.find_all('div', {'class': 'sc-5179a348-6 bnnHxo cli-title-metadata'})
	for tag in tags:
		print(tag.text)

	# Count how many times each year appears using a dictionary
	years_dict = {}
	for tag in tags:
		if tag.text[:4] not in years_dict:
			years_dict[tag.text[:4]] = 1
		else:
			years_dict[tag.text[:4]] += 1

	# print results sorted by frequency
	for year, occur_freq in sorted(years_dict.items(), key=lambda tup: tup[1]):
		print(year, '->', occur_freq)


if __name__ == '__main__':
	main()
