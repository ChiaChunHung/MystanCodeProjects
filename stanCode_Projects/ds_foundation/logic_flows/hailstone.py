"""
File: hailstone.py
Name: Chia-Chun, Hung
--------------------------------------------------
This program simulates the Hailstone sequence, also known
as the Collatz sequence. Given a starting integer greater
than 0, the program repeatedly applies the following rules
until the value reaches 1:

- If the number is odd, multiply by 3 and add 1
- If the number is even, divide by 2

The program prints each step and reports the total number
of steps taken to reach 1.
"""


def main():
    """
    Prompts the user to enter a positive integer and
    computes how many steps it takes to reach 1
    using the Hailstone sequence rules.
    """
    print("This program computes Hailstone sequences.")
    n = int(input("Enter a number: "))
    if n == 1:
        print("It took 0 steps to reach 1.")
    else:
        steps = 0
        while n != 1:
            if n % 2 == 1:
                n_1 = n * 3 + 1
                print(str(n)+" is odd"+", so I make 3n+1: "+str(n_1))
                n = n_1
                steps += 1
            else:
                n_1 = int(n/2)
                print(str(n) + " is even" + ", so I take half: " + str(n_1))
                n = n_1
                steps += 1
        print("It took "+str(steps)+" steps to reach 1.")


if __name__ == "__main__":
    main()
