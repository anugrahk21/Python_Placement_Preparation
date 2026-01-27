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

    del user.amount  # Deleting member variable amount of object user
    # We dont do Bank.amount as amount is not a class variable, its an instance variable(object variable)
    #check if exists
    print(hasattr(user,'amount'))  # False
    # i.e. print(user.amount) will give error now
    user.amount=0  # Re-adding member variable amount
    print(hasattr(user,'amount'))  # True



#Calculator class with 4 operations and 2 operands
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self): # self is used to access member variables and methods of the class
        print(f"{self.a} + {self.b} = ",self.a+self.b)
        # self.a because a is member variable of the class Calculator that is initialized using constructor
        # and now we are accessing it using self
    
    def div(self):
        print(f"{self.a} / {self.b} = ",self.a/self.b)
    
    def sub(self):
        print(f"{self.a} - {self.b} = ",self.a-self.b)
    
    def mul(self):
        print(f"{self.a} * {self.b} = ",self.a*self.b)
    
if __name__=="__main__":
    a=int(input("Enter your 1st operand: "))
    b=int(input("Enter your 2nd operand: "))
    operation=Calculator(a,b)
    operation.add()
    operation.sub()
    operation.div()
    operation.mul()



# Employee details class
class Employee:
    def __init__(self,name,id,m_sal):
        self.name=name
        self.id=id
        self.m_sal=m_sal
    
    def details(self):
        print("Name : ",self.name)
        print("ID : ",self.id)
        print("Yearly Salary : ",self.m_sal*12)

    
if __name__=="__main__":
    name=input("Enter Employee Name: ")
    id=int(input("Enter Employee ID: "))
    m_sal=int(input("Enter Employee Monthly Salary: "))
    emp=Employee(name,id,m_sal)
    emp.details()