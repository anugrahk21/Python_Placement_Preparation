# OOPs in Python

class Bank:
    # Constructor
    def __init__(self,name,amount=0):
        self.name=name
        self.amount=amount  # Balance amount, initially 0

    # self represents the current object

    # Member Functions (Methods)
    def deposit(self,dep_amount):
        self.amount+=dep_amount
        print(f"Amount :{dep_amount} deposited successfully")
        self.balance()
    def withdraw(self,wd_amount):
        if(wd_amount>self.amount):
            print("Insufficient balance")
            return
        self.amount-=wd_amount
        print(f"Amount :{wd_amount} withdrawn successfully")
        self.balance()
    def balance(self):
        print(f"Available balance is :{self.amount}\n")
    
if __name__ == "__main__":
    name=input("Enter your name:")
    user=Bank(name)
    dep_amount=int(input("Enter amount to be deposited:"))
    user.deposit(dep_amount)
    wd_amount=int(input("Enter amount to be withdrawn:"))
    user.withdraw(wd_amount)