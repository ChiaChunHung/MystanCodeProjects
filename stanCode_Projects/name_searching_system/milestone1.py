"""
File: milestone1.py
Name: Chia-Chun Hung
-----------------------
Description:
Completed as part of SC101 Assignment 4. I implemented and tested the `add_data_for_name()`
function, which correctly merges ranking data across years for each baby name, handles duplicate
name entries, and ensures only the highest rank is stored for each year. This laid the foundation
for building the full baby name tracking system in babyname.py project.
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
        name_data[name] = {year: rank}
    else:
        if year in name_data[name]:
            if int(name_data[name][year]) <= int(rank):
                # Note: Original data is in str format; use int() to compare values numerically instead of by ASCII.
                pass
            else:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank

    # Another solution
    # if name not in name_data:
    #     name_data[name] = {year: rank}
    # elif name in name_data and year in name_data[name]:  # order
    #     if int(rank) <= int(name_data[name][year]):
    #         name_data[name][year] = rank
    # else:
    #     name_data[name][year] = rank


def test1():  # Test adding a name that hasn't been recorded before
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():  # Test handling a name that already exists
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():  # Test handling same name and year but different rank values
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():  # Test if all possible cases can be handled
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':  # This checks whether the user provided an argument.
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
