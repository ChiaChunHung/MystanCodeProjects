"""
File: word_occurrence.py
--------------------------------------------------
This script reads a text file, called romeojuliet.txt,
and computes the frequency of each word, after performing
basic text preprocessing (e.g., punctuation removal, case normalization).
The results are printed in ascending order of frequency.

This task simulates a core step in Natural Language Processing (NLP),
which is foundational to many data science applications involving
text data, such as sentiment analysis, topic modeling, and search indexing.

Concepts covered:
- File I/O
- Text tokenization
- Dictionary-based frequency counting
- Lambda functions for sorting
- Basic string preprocessing (case and punctuation handling)
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_d = {}										# Initialize an empty dictionary for word frequency counts
	with open(FILE, 'r') as f:						# load the file into memory line by line
		for line in f:
			tokens = line.split()					# Tokenize the line into words based on whitespace
			for token in tokens:
				token = string_manipulation(token)  # clean token by removing punctuation and standardize the word to lowercase
				if token not in word_d:
					word_d[token] = 1				# First occurrence of this word in our dictionary
				else:
					word_d[token] += 1				# Increment count for repeated word
		print_out_d(word_d)							# print the sorted word frequencies


def print_out_d(d):
	"""
	: param d: (dict) d is a dictionary mapping words to their occurrences.
	---------------------------------------------------------------
	Sort the dictionary by frequency (value) in ascending order and
	print each word with its count.
	"""
	for word, occurrence in sorted(d.items(), key=lambda t: t[1]):
		print(word, '->', occurrence)


def string_manipulation(token):
	"""
	: param token: token is each word in the text
	we load from the text file.
	----------------------------------------------
	Build the cleaned token and standardize every
	tokens to lowercase.
	"""
	ans = ''
	for ch in token:
		if ch.isdigit() or ch.isalpha():		# retain only alphanumeric characters
			ans += ch.lower()					# convert to lowercase for cas-insensitive counting
	return ans									# 因為user端那邊有接，故要return


if __name__ == '__main__':
	main()
