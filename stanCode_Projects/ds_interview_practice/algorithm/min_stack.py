"""
File: min_stack.py
Name: Chia-Chun, Hung
--------------------------------------------------
This script implements a custom stack class that supports
push, pop, top, and retrieving the minimum value—all with
constant time complexity for get_min().

This problem is a common coding interview question focused on:
- Designing auxiliary data structures to optimize performance
- Achieving O(1) time complexity for minimum retrieval
- Understanding stack behavior and state tracking

It is foundational for building algorithmic thinking relevant
to system design and data structure manipulation in data science.
"""


class MinStack:
    def __init__(self):
        # main stack to store values
        self.ds = []

        # Auxiliary stack to track minimums
        self.my_min = []

    def push(self, val: int) -> None:         # -> None means no return value
        """
        :param val: (int), the value user push into stack
        -----------------------------
        Add value to main stack
        If it's the first element or smaller than current min, record in min stack
        """
        self.ds.append(val)
        if len(self.ds) == 1:
            self.my_min.append(val)
        if val < self.my_min[-1]:
            self.my_min.append(val)

    def pop(self) -> None:
        """
        Pop value from main stack
        If it's equal to current min, also pop from min stack
        """
        if len(self.ds) != 0:
            if self.ds[-1] in self.my_min:
                self.my_min.pop()
            self.ds.pop()

    def top(self) -> int:
        """
        :return: Return the top value of the stack if not empty
        """
        if len(self.ds) != 0:
            return self.ds[-1]

    def get_min(self) -> int:
        """
        :return: Return the minimum value in stack using linear scan (O(N))
        """
        if len(self.ds) != 0:
            my_min = self.ds[0]
            for num in self.ds:
                if num < my_min:
                    my_min = num
            return my_min

    def faster_get_min(self):
        """
        Optimized O(1) version using auxiliary min stack
        -----------------------------------------------
        :return: Return the minimum value in stack
        """
        if len(self.my_min) != 0:
            return self.my_min[-1]


if __name__ == '__main__':
    """
    this function is used to test the MinStack Class above
    """
    my_stack = MinStack()
    print(my_stack.top(), end=', ')
    print(my_stack.get_min(), end=', ')
    my_stack.pop()
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top(), end=', ')
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top())

    my_stack = MinStack()
    my_stack.push(5)
    my_stack.push(9)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(6)
    my_stack.push(1)
    my_stack.push(8)
    my_stack.pop()
    my_stack.pop()
    print(my_stack.faster_get_min(), end=', ')
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(my_stack.faster_get_min(), end=', ')
    my_stack.pop()
    print(my_stack.faster_get_min(), end=', ')
    my_stack.pop()
    print(my_stack.faster_get_min())

