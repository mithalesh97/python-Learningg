class BankAccount:
    def __init__(self,owner,balance):
        self.__balance = balance
        self.owner = owner

    def deposit(self,amount):
        self.__balance += amount
        print(f"deposited amount: {amount}. Balance: {self.__balance}")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficient funds!")
        else:
            self.__balance -= amount
            print(f"withdraw amount: {amount}. Balance: {self.__balance}")

    def checkbalance(self):
        print(f"Balance: {self.__balance}")

name = input("enter the name of the owner")
balance = int(input("enter the balance of your account: "))
acc = BankAccount(name,balance)
dep = int(input("enter the balance to deposit in your account: "))
acc.deposit(dep)
withd = int(input("enter the balance to withdraw in your account: "))
acc.withdraw(withd)
acc.checkbalance()