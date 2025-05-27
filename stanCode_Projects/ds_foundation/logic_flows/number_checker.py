"""
File: number_checker.py
Name: Chia-Chun, Hung
--------------------------------------------------
This program checks whether a user-inputted number is
a perfect, abundant, or deficient number based on the
sum of its proper divisors (excluding the number itself).

Definitions:
- Perfect number: sum of proper divisors equals the number
- Abundant number: sum of proper divisors is greater than the number
- Deficient number: sum of proper divisors is less than the number

The program repeatedly accepts integer input from the user
and performs classification until the user enters the EXIT value.
"""

EXIT = -100


def main():
    """
    After asking user to enter a number, this program will first find
    out all the proper factors of that number, and then it will calculate
    the sum of all those factors to determine whether the result is equal,
    higher, or lower than the number the user enters.
    """
    print("Welcome to the number Checker!")
    while True:
        number = int(input("n: "))
        if number == EXIT:
            break
        count_from = 1                                          # start checking from 1
        summary = 0                                             # SUm of proper divisors
        while True:
            if number == count_from:
                break
            else:
                if number % count_from == 0:
                    summary = summary + count_from              # Add proper divisor
                    count_from = count_from + 1                 # Increment counter
                else:
                    count_from = count_from + 1

        # Classification based on sum of proper divisors
        if summary == number:
            print(str(number)+" is a perfect number.")
        elif summary > number:
            print(str(number)+" is an abundant number.")
        else:
            print(str(number) + " is a deficient number.")
    print("Have a good one!")


if __name__ == '__main__':
    main()
