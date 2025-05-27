"""
File: pypal.py
Name: Chia-Chun, Hung
--------------------------------------------------
This script defines a class-based simulation of a basic banking system.
The `Pypal` class models a user account with the ability to:
- Withdraw funds with limits
- Access and modify user information using getter/setter methods
- Protect internal balance using strict and soft privacy conventions

The script also demonstrates how to interact with the object using a
sample `bank()` function, showcasing deposit limits, name changes, and
remaining balance retrieval.

This structure illustrates key object-oriented programming concepts,
including encapsulation, access control, and method encapsulation.
"""

WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    # Initialize user account with name, starting balance, and withdrawal limit
    def __init__(self, name, money=MONEY, limit=WITHDRAW_LIMIT):  # Keyword args 喜歡寫成Constant，因方便老闆改
        self._n = name
        self.__m = money  # Strictly private: prevents external modification of balance
        self._l = limit   # Soft private: not meant for external access but still modifiable

    def withdraw(self, amount):
        """
        Attempt to withdraw funds under the defined
        limit and available balance.
        """
        if amount > self._l:      # Exceeds per-withdraw limit
            print('Exceed limit')
        elif amount > self.__m:   # Exceeds account balance
            print('Illegal')
        else:
            self.__m = self.__m - amount
            print(f'{self._n} remains {self.__m}')

    def get_amount(self):
        """
        :return: the current balance (read-only access)
        """
        return self.__m

    def set_username(self, new_name):
        """
        update the account holder's name
        """
        self._n = new_name
        print(f'Successfully Updated! Now your username is {new_name}')

    def __str__(self):
        """
        :return: a formatted string representing the account status
        """
        return f'{self._n} remains {self.__m} / limit: {self._l}'


def bank():
    """
    Create a sample Pypal account and perform transactions
    """
    t_account = Pypal('Tony', money=1000, limit=700)
    t_account.withdraw(1000)
    t_account.withdraw(700)
    t_account.withdraw(700)

    # Get remaining money
    amount = t_account.get_amount()
    print('Remaining amount:', amount)

    # Set username
    t_account.set_username('Chia-Chun')


if __name__ == '__main__':
    bank()

