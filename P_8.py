# OOPs in Python

class Bank:
    def __init__(self,name,amount=0):
        self.name=name
        self.amount=amount
    def deposit(self,dep_amount):
        self.amount+=dep_amount
        print(f"Amount :{dep_amount} deposited successfully")
    def withdraw(self,wd_amount):
        if(wd_amount>self.amount):
            print("Insufficient balance")
            return
        self.amount-=wd_amount
        print(f"Amount :{wd_amount} withdrawn successfully")
    def balance(self):
        print(f"Available balance is :{self.amount}")
    
if __name__ == "__main__":
    name=input("Enter your name:")
    user1=Bank(name)
    dep_amount=int(input("Enter amount to be deposited:"))
    user1.deposit(dep_amount)
    user1.balance()
    wd_amount=int(input("Enter amount to be withdrawn:"))
    user1.withdraw(wd_amount)
    user1.balance()