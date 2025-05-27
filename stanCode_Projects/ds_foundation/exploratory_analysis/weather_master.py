"""
File: weather_master.py
Name: Chia-Chun, Hung
--------------------------------------------------
This program collects a series of daily temperature readings
from the user, then reports summary statistics:

- Highest temperature
- Lowest temperature
- Average temperature
- Count of cold days (temperature below 16°C)

This program demonstrates fundamental data processing logic
used in data science: accumulation, conditional evaluation,
and summary statistics aggregation.
"""

EXIT = -1


def main():
	"""
	This program asks users to enter temperature data,
	and it will then indicate the highest and the lowest temperature;
	the average temperature; and how many days had temperature lower than 16 degree,
	days that we call them cold days.
	"""
	print('stanCode "Weather Master 4.0"!')												# print program title
	degree = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
	if degree == EXIT:
		print("No temperatures were entered.")
	else:
		maximum = degree  																# Initialize max temperature
		minimum = degree  																# Initialize min temperature
		average_need_sum = degree  														# Sum for average calculation
		average_need_number = 1  														# sample count
		cold_days = 0  																	# Initial cold day check
		if degree < 16:
			cold_days += 1
		while True:
			degree = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
			if degree == EXIT:
				break
			average_need_sum = average_need_sum + degree
			average_need_number += 1
			if degree < 16:
				cold_days += 1
			if degree >= maximum:
				maximum = degree
			elif degree < minimum:
				minimum = degree
		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		average = average_need_sum / average_need_number
		print("Average = " + str(average))
		print(str(cold_days) + " cold day(s)")


if __name__ == "__main__":
	main()
