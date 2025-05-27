"""
File: binary_search.py
Name: CHia-Chun, Hung
--------------------------------------------------
This script demonstrates the binary search algorithm,
which efficiently finds the position of a target value
within a sorted list in O(log n) time.

While not core to data science modeling, binary search
is a foundational algorithm used in tasks like lookup
acceleration, search-sorted operations, and threshold
finding in sorted datasets.
"""


def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	high, low = len(lst)-1, 0   # Initialize low and high pointers for the search range
	while True:					# Repeat until the search range becomes invalid
		mid = (high + low)//2   # calculate the middle index (integer division)
		if lst[mid] == target:  # If target found at mid index, return True
			return True
		if lst[mid] > target:   # If target is smaller, search the left half
			high = mid - 1
		else:					# If target is larger, search the right half
			low = mid + 1
		if high < low:			# Target not found in the list
			return False


if __name__ == '__main__':
	main()
