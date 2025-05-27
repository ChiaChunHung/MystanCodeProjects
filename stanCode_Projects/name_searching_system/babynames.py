"""
File: babynames.py
Name: Chia-Chun Hung
--------------------------
Description:
Completed as part of SC101 Assignment 4. I implemented the full backend logic for processing
baby name ranking data, including file parsing, data structuring, and search functionality.
This helped me practice nested dictionaries, string parsing, and case-insensitive lookup logic.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:
        # If the name is not yet in the dictionary, create a new entry
        name_data[name] = {year: rank}
    else:
        # if the year exists, update the rank only if the new rank is better, smaller
        if year in name_data[name]:
            if int(name_data[name][year]) <= int(rank):
                # Note: Convert strings to integers for numerical comparison
                pass
            else:
                name_data[name][year] = rank
        else:
            # if the year is not present under the name, add the new year-rank pair
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    switch = True
    with open(filename, 'r') as f:
        for line in f:
            if switch:
                year = line.strip()
                switch = False
            else:
                lst = line.split(',')
                # Split each subsequent line by comma to extract rank, name1, and name2
                rank = lst[0].strip()
                name1 = lst[1].strip()
                name2 = lst[2].strip()
                # Strip whitespace and pass data to add_data_for_name()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []                                           # store names that contain the target substring
    for name in name_data:
        # for each name, check if any substring matches the target (case-insensitive)
        switch = False
        for i in range(len(name)-len(target)+1):
            if name[i: i+len(target)].lower() == target.lower():
                switch = True
        # Append matched names to the result list
        if switch:
            matching_names.append(name)
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
