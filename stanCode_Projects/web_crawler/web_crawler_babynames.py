"""
File: webcrawler.py
Name: Chia-Chun, Hung
--------------------------
Description:
Completed as part of SC101 Assignment 4. I implemented a web scraper using `requests` and
`BeautifulSoup` to extract and sum top-200 baby name counts by gender from SSA.gov across
three decades. This helped reinforce my understanding of HTML parsing and data aggregation.
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # features="html.parser" is added to resolve the warning PyCharm shows, and it also offers a solution.

        tags = soup.find_all('tbody')
        # .find_all('tag name') is used to find all matching tags and store them in a list.
        # Since the website has only one <tbody>, tags contains only one element (tbody), and its data type is list.
        # We cannot directly call .text on tags because it’s a list;
        # we must call .text on the individual element inside the list—hence the for-each loop below.

        female = 0
        male = 0

        # tags is a list containing only one element named tbody, so this loop runs only once.
        # The extracted element is named tag, and it is the entire <tbody></tbody> content.
        for tag in tags:
            tag = tag.text.split()
            # Because .split() splits all the text by whitespace and stores it into a list, tag is now a list.
            tag = tag[:1000]
            # We have 200 lines, each with 5 pieces of data, so we limit it to 1000 items.

            # male number
            for i in range(2, len(tag)-2, 5):
                # The last male number appears at position len(tag)-3, and starting from position 2,
                # every +5 index is the next male number.

                # Some numbers include non-numeric characters like commas (e.g., '123,456'),
                # so we remove them and generate a clean number string.
                num_wo_comma = ''
                for j in range(len(tag[i])):
                    if tag[i][j] != ',':
                        num_wo_comma += tag[i][j]

                male += int(num_wo_comma)

            # Same as above, but for female numbers.
            for i in range(4, len(tag), 5):

                num_wo_comma = ''
                for j in range(len(tag[i])):
                    if tag[i][j] != ',':
                        num_wo_comma += tag[i][j]

                female += int(num_wo_comma)

        print('Male number:', male)
        print('Female number:', female)


if __name__ == '__main__':
    main()
