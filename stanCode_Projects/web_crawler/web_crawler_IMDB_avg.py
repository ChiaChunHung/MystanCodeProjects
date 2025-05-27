"""
File: web_crawler_avg.py
Name: Chia-Chun, Hung
-------------------------------------------------------
This script demonstrates how to use web scraping to compute
the average rating of top movies from the IMDb Top 250 page.

It retrieves the HTML content, parses the ratings using
BeautifulSoup, and calculates the average of the first 25
movie ratings available.

Skills practiced:
- Sending HTTP requests with custom headers
- Parsing HTML using BeautifulSoup
- Extracting and processing numerical data
- Basic statistical aggregation (mean calculation)

This exercise provides a foundation in data collection and
preprocessing, which is a key step in data science workflows.
Note: The script only captures the top 25 movies due to
IMDb's dynamic content loading.
"""

import requests
from bs4 import BeautifulSoup


def main():
	# Send an HTTP GET request with a fake User-Agent to mimic a browser
	url = 'http://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)

	# Extract raw HTML text from the response
	html = response.text

	# Parse HTML using BeautifulSoup to create a searchable DOM object
	soup = BeautifulSoup(html, features="html.parser")

	# Find all span tags with class matching the star rating value
	tags = soup.find_all('span', {'class': 'ipc-rating-star--rating'})

	# Extract rating text and compute total to later calculate average
	total = 0
	for tag in tags:
		total += float(tag.text)

	# Compute and print the average rating for the top 25 visible movies
	print(total/25)


if __name__ == '__main__':
	main()
