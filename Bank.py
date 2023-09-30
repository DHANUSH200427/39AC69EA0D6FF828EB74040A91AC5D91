class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self._account_number = account_number
    self._account_holder_name = account_holder_name
    self._account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self._account_balance += amount
      return f"Deposited ${amount}. New balance: ${self._account_balance}"
    else:
      return "Invalid deposit amount. Amount must be greater than 0."

  def withdraw(self, amount):
    if amount > 0 and amount <= self._account_balance:
      self._account_balance -= amount
      return f"Withdrew ${amount}. New balance: ${self._account_balance}"
    elif amount <= 0:
      return "Invalid withdrawal amount. Amount must be greater than 0."
    else:
      return "Insufficient balance for withdrawal."

  def display_balance(self):
    return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"


# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000.0)

# Test deposit functionality
print(account.deposit(500))  # Deposited $500. New balance: $1500.0

# Test withdrawal functionality
print(account.withdraw(200))  # Withdrew $200. New balance: $1300.0
print(account.withdraw(1600))  # Insufficient balance for withdrawal.

# Display the account balance
print(account.display_balance())  # Account Balance for John Doe: $1300.0
