"""
File: rotten_tomato.py
Name: Chia-Chun Hung
--------------------------------------------------------
This script implements a basic sentiment analysis tool
using a dictionary-based Bag-of-Words model.

The input file contains movie reviews, each labeled with
a score. The program tokenizes each review, processes
each word, and builds a word-score dictionary based on
cumulative scores across all reviews.

This foundational project demonstrates key data science
concepts in NLP:
- Text preprocessing and tokenization
- Dictionary construction for feature aggregation
- Basic sentiment modeling using score accumulation
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	"""
	Read the labeled review dataset and build a
	word-score dictionary using Bag-of-words logic.
	"""
	with open(FILENAME, 'r') as f:
		word_d = {}							 		# Dictionary to store each word and its cumulative sentiment score
		for line in f:
			score, review = line.split(':')  		# Split line into score and review text
			real_score = int(score[1:3])			# Extract numerical score, handling potential '+' or '-' signs
			tokens = review.split()			 		# Tokenize review by whitespace
			for token in tokens:
				token = string_manipulation(token)  # Clean punctuation from word
				if token not in word_d:
					word_d[token] = real_score		# First occurrence: assign score
				else:
					word_d[token] += real_score		# Repeated occurrence: accumulate score
		print(word_d)


def string_manipulation(token):
	"""
	Remove punctuation and return cleaned,
	alphabet-only token.
	"""
	ans = ''
	for ch in token:
		if ch.isalpha():
			ans += ch
	return ans


if __name__ == '__main__':
	main()
