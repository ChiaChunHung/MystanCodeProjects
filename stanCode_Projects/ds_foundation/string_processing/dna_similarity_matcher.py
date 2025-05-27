"""
File: dna_similarity_matcher.py
Name: Chia-Chun Hung
--------------------------------------------------
This program compares a short DNA sequence (match_seq)
against all possible substrings of a longer DNA sequence (given_dna_seq)
to find the most similar segment based on positional base matches.

It simulates a simplified approach to sequence alignment used
in bioinformatics, focusing on character-level similarity.
"""


def main():
    """
    Prompts the user for two DNA sequences: one to search within,
    and one to match. Prints the most similar substring from the
    search sequence that matches the input based on character position.
    """
    given_dna_seq = input('Pleas give me a DNA sequence to search: ')
    match_seq = input('What DNA sequence would you like to match? ')
    find_the_best_match(given_dna_seq, match_seq)


def find_the_best_match(given_dna_seq, match_seq):
    """
    : param given_dna_seq: string, the DNA sequence to search
    : param match_seq: string, the DNA sequence the user wants to match
    """
    given_dna_seq = given_dna_seq.upper()
    match_seq = match_seq.upper()

    count = 0
    compared_seg = given_dna_seq[:len(match_seq)]
    for i in range(len(match_seq)):
        if match_seq[i] == compared_seg[i]:
            count += 1
    maximum = count
    best_match_seq = compared_seg

    first_index_of_last_seg = (len(given_dna_seq) - 1) - (len(match_seq) - 1)
    for i in range(1, first_index_of_last_seg+1):
        compared_seg = given_dna_seq[i:i+(len(match_seq))]
        count = 0
        for j in range(len(match_seq)):
            if match_seq[j] == compared_seg[j]:
                count += 1
        if count >= maximum:
            maximum = count
            best_match_seq = compared_seg
    print('The best match is ' + best_match_seq)


if __name__ == '__main__':
    main()
