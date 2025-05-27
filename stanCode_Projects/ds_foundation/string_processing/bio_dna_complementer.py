"""
File: bio_dna_complementer.py
Name: Chia-Chun Hung
--------------------------------------------------
This program solves a basic bioinformatics problem:
given a DNA strand as a string input, it returns the
complementary DNA strand.

The program maps each nitrogenous base (A, T, C, G) to
its biological complement:
- A <-> T
- C <-> G
If the input is an empty string, an error message is returned.

This script reinforces basic string manipulation and control flow.
"""


def main():
    """
    Demonstrates the build_complement() function on
    a series of test cases.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    : param dna: string
    : return: string, return complementary fragments of nitrogenous bases
    that the users enter.
    """
    if dna == '':                           # Handle empty input case
        return 'DNA strand is missing.'
    else:
        ans = ''
        for i in range(len(dna)):
            if dna[i] == 'A':
                ans += 'T'
            elif dna[i] == 'T':
                ans += 'A'
            elif dna[i] == 'C':
                ans += 'G'
            else:
                ans += 'C'
        return ans


if __name__ == '__main__':
    main()
