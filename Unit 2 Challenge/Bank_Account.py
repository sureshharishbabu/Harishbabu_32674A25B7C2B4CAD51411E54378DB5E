class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited \t:₹{}.\nNew Balance\t:₹{}.".format(
          amount, self.__account_balance))
    else:
      print("Invalid deposit amount. Please enter a positive amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw \t:₹{}.\nNew balance\t:₹{}.".format(
          amount, self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("\nAccount balance for {} (Account no:{}):₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


account = BankAccount(account_number="1119943568729",
                      account_holder_name="AnbuSelven",
                      initial_balance=100000)

account.display_balance()
account.deposit(50000)
account.withdraw(20000)
account.display_balance()
