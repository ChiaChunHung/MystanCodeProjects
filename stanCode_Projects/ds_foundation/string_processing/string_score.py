"""
File: string_score.py
Name: Chia-Chun, Hung
------------------------------
This program calculates a score for a given string based on
the types of characters it contains:

- Digits contribute 1 point each
- Uppercase letters contribute 2 points each
- Lowercase letters contribute 3 points each

This script demonstrates control flow, character classification,
and loop-based accumulation — common in string preprocessing
and feature engineering for data science tasks.


It assigns points as follows:
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    Demonstrates the score() function on sample inputs.
    """
    score('1aB4rC')
    score('aaaaA3')


def score(string):
    """
    : param string: string, the string that is used to calculate a score.
    """
    summary = 0
    for i in range(len(string)):
        if string[i].isdigit():
            summary += 1
        elif string[i].isupper():
            summary += 2
        else:
            summary += 3
    print(summary)


if __name__ == '__main__':
    main()
