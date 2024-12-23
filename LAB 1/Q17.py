#Create a class BankAccount with private attributes balance and account_number. Implement methods deposit() and withdraw() to modify the balance. Ensure that the balance cannot be accessed directly from outside the class.

class BankAccount:
    def __init__(self,accountNumber,Balance):
        self.__account_number = accountNumber
        self.__balance= Balance
    
    def deposit(self,accountNumber,amount):
        if accountNumber == self.__account_number:
            self.__balance+= amount
            print(f"{amount} Deposited")
            print(f"The total amount is {self.__balance}")
        else:
            print("Account number didn't matched")
    
    def withdraw(self,accountNumber, withdrawAmount):
        if accountNumber == self.__account_number:
            if self.__balance > withdrawAmount:
                self.__balance -= withdrawAmount
                print(f"{withdrawAmount} Withdrawn")
                print(f"The total amount remaining is {self.__balance}")
            else:
                print("Not sufficient Balance")
        else:
            print("Account number didn't matched")

Account = BankAccount(1124,500)
Account.deposit(1125,200)
Account.deposit(1124,200)
Account.withdraw(1124,200)