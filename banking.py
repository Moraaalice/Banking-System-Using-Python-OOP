# I am creating a banking system with OOP
# My fiirst class is class User which carries the user details
class User:
    def __init__(self,name,age,identification_number,gender,):
        self.name = name
        self.age = age
        self.identification_number = identification_number
        self.gender = gender
        
    def user_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Identification Number:",self.identification_number)
        print("Gender:",self.gender)   
        
user = User("Mary Ongongo",28,33133095,"Female")
user.user_details()

#Creating a child class which is inheriting from our User class
class Bank(User):
    def __init__(self, name, age, identification_number, gender):
        super().__init__(name, age, identification_number, gender)
        self.balance = 0
        
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"The balance has been updated to {self.balance}")
        
    def withdrawals(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient funds to withdraw {self.amount}")
        else:
            self.balance = self.balance - amount
            print(f"{self.amount} withdrawn successfully the balance is {self.balance}")
            
            
    def show_account_balance(self):
        self.user_details()
        print("Account Balance:",self.balance)        
                   

#Instantiating the bank class and testing if it is working        
dante = Bank("Dante",4,38493531,"male")
print(dante.name)
print(dante.age)
print(dante.identification_number)
print(dante.gender)
dante.deposit(40000)
dante.withdrawals(20000)
dante.show_account_balance()

#This is my small accounting system by use of Object Oriented Programming

 
              
         