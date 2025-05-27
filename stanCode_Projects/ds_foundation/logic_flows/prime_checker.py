"""
File: prime_checker.py
Name: Chia-Chun, Hung
--------------------------------------------------
This program prompts the user to input an integer greater than 1
and checks whether the number is a prime number.

The user can repeatedly enter values to test for primality.
The program terminates when the user enters the sentinel EXIT value.

This script reinforces control flow, loop logic, and
fundamental number theory in Python.
"""

EXIT = -100


def main():
	"""
	Prompts the user for integers and checks if each is a prime number.
	Ends when the user enters the EXIT value.
	"""
	print("Welcome to the prime checker!")  			# Introduction message
	while True:
		number = int(input("n: "))
		if number == EXIT:
			break
		divisor = 2  									# start checking from the smallest prime divisor
		while True:
			if number % divisor != 0:
				divisor += 1
			elif divisor == number:
				print(str(number) + " is a prime number.")
				break
			else:
				print(str(number) + " is not a prime number.")
				break
	print("Have a good one!")


if __name__ == "__main__":
	main()
