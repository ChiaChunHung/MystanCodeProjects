"""
File: narcissistic_checker.py
Name: Chia-Chun, Hung
------------------------
This program checks whether a given integer is a
narcissistic number.

A narcissistic number is a positive integer equal to the sum
of its digits, each raised to the power of the number of digits.
All single-digit numbers are considered narcissistic.

The program repeatedly accepts input until the user enters
a sentinel value to exit. This exercise reinforces digit
manipulation, exponentiation, and loop control.
"""
EXIT = -100


def main():
    """
    After asking user to enter a number, this program will begin to identify
    whether the number is a narcissistic number, by counting the number of the digit of it,
    calculating the sum of its own digits each raised to the power of the number of digits,
    and comparing the sum with the number itself.
    """
    print("Welcome to the narcissistic number checker!")
    while True:
        number = int(input("n: "))
        if number == EXIT:
            break
        if number < 10:                                         # All single-digit number are narcissistic
            print(str(number) + " is a narcissistic number.")
        else:                                                   # Step1 : Determine number of digits
            num_for_figure = number
            figure = 2
            while True:
                if num_for_figure // 10 >= 10:
                    figure += 1
                    num_for_figure = num_for_figure // 10
                else:
                    break

            # Step2：Calculate the sum of digits raised to the digit count power
            sum_of_power = 0
            power = figure - 1
            num_for_digit = number
            while True:
                sum_of_power = sum_of_power + ((num_for_digit // (10**power))**figure)
                num_for_digit = num_for_digit - ((num_for_digit // (10**power)) * 10**power)
                power -= 1
                if power == 0:
                    sum_of_power = sum_of_power + num_for_digit**figure
                    break

            # Step 3: Compare result to original number
            if sum_of_power == number:
                print(str(number) + " is a narcissistic number.")
            else:
                print(str(number) + " is not a narcissistic number.")
    print("Have a good one!")


if __name__ == '__main__':
    main()
