"""
File: sorting_algorithm.py
Name: Chia-Chun Hung
--------------------------------------------------
This script demonstrates three fundamental sorting algorithms:
Bubble Sort, Selection Sort, and Insertion Sort.

Each function operates on a sample list and sorts it in ascending order.
These algorithms are commonly used in introductory computer science and
are valuable for developing core algorithmic understanding.

Though inefficient for large datasets, they illustrate important concepts:
- Element comparison and conditional swapping
- Loop control and iteration bounds
- In-place sorting (modifying the list directly)
"""


def main():
    """
    Runs all sorting algorithms on a sample list.
    Each algorithm prints the sorted result for comparison.
    """
    lst = [4, 2, 5, 6, 1, 0, 7, -1, 5]
    bubble_sort(lst)

    lst = [4, 2, 5, 6, 1, 0, 7, -1, 5]
    selection_sort(lst)

    lst = [4, 2, 5, 6, 1, 0, 7, -1, 5]
    insertion_sort(lst)


def bubble_sort(lst):
    """
    Sorts the input list in ascending order using the Bubble Sort algorithm.
    Repeatedly compares adjacent elements and swaps them if they are in the
    wrong order. Time complexity: O(n^2)
    """
    n = len(lst)
    for i in range(n):                                   # Outer loop runs n time
        for j in range(0, n - i - 1):                    # Inner loop runs fewer times each pass (one less than before)
            if lst[j] > lst[j + 1]:                      # Compare and swap if elements are out of order
                lst[j + 1], lst[j] = lst[j], lst[j + 1]  # pythonic swap of two list elements
    print(lst)


def selection_sort(lst):
    """
    Sorts the input list in ascending order using the Selection Sort algorithm.
    Finds the minimum element from the unsorted part and places it at the beginning.
    Time complexity: O(n^2)
    """
    n = len(lst)
    for i in range(n-1):
        m = i                                            # Assume current index is the minimum
        for j in range(i+1, n):                          # Find the index of the smallest item
            if lst[j] < lst[m]:
                m = j
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]              # Swap current index with the found minumum
    print(lst)


def insertion_sort(lst):
    """
    Sorts the input list in ascending order using the Insertion Sort algorithm.
    Builds the sorted list one item at a time by shifting larger elements to the right.
    Time complexity: O(n^2)
    """
    n = len(lst)
    for i in range(1, n):                               # Start from the second element
        temp = lst[i]                                   # temporarily hold the value to be inserted
        j = i-1
        while j >= 0 and temp < lst[j]:                 # Shift elements greater than tempt to the right
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp                                 # Insert temp at the correct position
    print(lst)


if __name__ == '__main__':
    main()
