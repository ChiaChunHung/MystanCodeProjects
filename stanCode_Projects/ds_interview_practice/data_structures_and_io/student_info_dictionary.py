"""
File: student_info_dict.py
Name: Chia-Chun, Hung
--------------------------------------------------
This script reads structured student information from a text file and
stores it into a nested Python dictionary. Each key in the outer dictionary
is a student's name, and its value is another dictionary containing the
student's age, email, and a list of favorite foods.

This exercise simulates a common real-world data ingestion and organization
task, such as parsing raw survey or log data into usable structured formats.
It helps develop essential data science skills including:

- File I/O operations for loading external datasets
- Text tokenization and parsing
- Dictionary (hash map) construction, including nested structures
- Understanding mutable objects and memory referencing in Python

These are foundational for working with formats like CSV/JSON or APIs, and
for preparing data before using pandas or other analysis libraries.
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
    all_d = {}  				   									# outer dictionary to store all student records
    with open(FILE, 'r') as f:
        for line in f:
            tokens = line.split()
            name = tokens[0]
            age = int(tokens[1])
            email = tokens[2]
            food = tokens[3:]
            d_student = {'AGE': age, 'EMAIL': email, 'FOOD': food}  # construct nested dictionary for one student
            all_d[name] = d_student
    print_out_d(all_d)  											# Nicely print out all student info


def print_out_d(d):
    """
    : param d: (dict) key of type str is the name of student value
    of type dict is the info of the student
    ---------------------------------------------------------------
    This function prints out a nested data structure on console
    """
    for student_name, student_info in d.items():
        print(student_name)
        print(student_info)
        print('-'*60)


if __name__ == '__main__':
    main()
