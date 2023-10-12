class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
    elif amount <= 0:
      print("Invalid withdrawal amount. Amount must be greater than 0.")
    else:
      print("Insufficient funds for withdrawal.")

  def display_balance(self):
    print(
        f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}"
    )


# Test the BankAccount class
if __name__ == "__main__":
  # Create a BankAccount instance
  account1 = BankAccount("123456789", "John Doe", 1000)

  # Test deposit and withdrawal functionality
  account1.display_balance()
  account1.deposit(500)
  account1.withdraw(200)
  account1.withdraw(1500)
  account1.display_balance()
