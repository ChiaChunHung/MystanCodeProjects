"""
File: Cinema_ticketing_system.py
Name: Chia-Chun, Hung
--------------------------------------------------
This script defines the Theater class, which simulates a basic
cinema seat reservation and cancellation system.

The system supports:
- Automatically reserving the smallest available seat
- Allowing users to cancel (unreserve) their seat
- Maintaining the internal seat list in ascending order

This structure is useful for scenarios involving seat
allocation in ticketing platforms, queue management systems,
or any application where priority-based resource assignment
is needed.
"""


class Theater:
    def __init__(self, n):
        # Initialize a list of available seats from 1 to n
        self.seat_num = []
        for i in range(1, n + 1):
            self.seat_num.append(i)

    def reserve(self):
        """
        Reserve the smallest available seat (front of the list)
        """
        given_num = self.seat_num[0]
        self.seat_num.pop(0)
        return given_num

    def unreserved(self, given_num):
        """
        Add the seat back and sort to maintain order
        """
        self.seat_num.append(given_num)
        self.seat_num = sorted(self.seat_num)


def main():
    auditorium_a = Theater(5)
    print(auditorium_a.reserve())  # Should return 1
    print(auditorium_a.reserve())  # Should return 2
    print(auditorium_a.reserve())  # Should return 3
    auditorium_a.unreserved(1)     # Make seat 1 available again
    auditorium_a.unreserved(2)     # Make seat 2 available again
    print(auditorium_a.reserve())  # Should return 1
    auditorium_a.unreserved(1)     # Make seat 1 available again
    print(auditorium_a.reserve())  # Should return 1


if __name__ == "__main__":
    main()
