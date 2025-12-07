# Demonstration of Data Validation using Encapsulation

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = 0      # private attribute
        self.deposit(initial_balance)  # validate initial amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: {self.__balance}"

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Yogesh", 1000)

    print(account.deposit(500))
    print(account.withdraw(200))
    print("Final Balance:", account.get_balance())
