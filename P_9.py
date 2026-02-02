# OOPs
# Encapsulation example
class Student:
    def __init__(self,name,age,grade,address):
        self.name=name
        self.age=age
        self.grade=grade
        self.__address=address  # private member variable
    
    def get_details(self):
        print("Student Name : ",self.name)
        print("Student Age : ",self.age)
        print("Student Grade : ",self.grade)
        print("Student Address : ",self.__address)
    
    def get_address(self):  # Sep fun to access the private member
        print(self.__address)
    
if __name__=="__main__":
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    grade=input("Enter student grade: ")
    address=input("Enter student address: ")
    student1=Student(name,age,grade,address)
    student1.get_details()
    #print(student1.__address) # This will raise an AttributeError as __address is private member variable
    #to access it we need to make a separate member function
    student1.get_address()



# Inheritance example
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
    
class GraduateStudent(Student):
    def __init__(self,name,age,degree):
        super().__init__(name,age)  # calling parent class constructor
        self.degree=degree
    
    def display(self):
        super().display()  # calling parent class method display
        print("Degree : ",self.degree)

if __name__=="__main__":
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    degree=input("Enter the degree: ")
    grad_student=GraduateStudent(name,age,degree)
    grad_student.display()  #1st-parent(Student) display : Name, Age ;
                            #2nd-child(GraduateStudent) display : Degree

                            

# Teacher Base class and Online teacher child class example

class Teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def display(self):
        print("Name of teacher: ",self.name)
        print("ID of teacher: ",self.id)

class OnlineTeacher(Teacher):
    def __init__(self,name,id,mode):
        super().__init__(name,id)
        self.mode=mode
        self.platform=input("Enter your platform: ")
    
    def display(self):
        super().display()
        print("The mode of teaching: ",self.mode)
        print("The platform of teaching: ",self.platform)

if __name__=="__main__":
    name=input("Enter the name: ")
    id=int(input("enter the id: "))
    mode=input("Enter the mode: ")
    teacher1=OnlineTeacher(name,id,mode)
    teacher1.display()



# Polymorphism
# Payment class with details such as payee name, amount and method of payment
class Payment:
    def __init__(self,payee,amount,method):
        self.payee=payee
        self.amount=amount
        self.method=method
    
    def process_payment(self):
        print(f"Process of payment of {self.amount} to {self.payee} using {self.method} method")

class CardPayment(Payment):
    def __init__(self,payee,amount,card_number):
        super().__init__(payee,amount,"Credit Card")
        self.card_number=card_number
    
    def process_payment(self):
        super().process_payment()
        print(f"Successfully transmitted card payment of {self.amount} to {self.payee} using card number {self.card_number}")
    
class UPIPayment(Payment):
    def __init__(self,payee,amount,upi_id):
        super().__init__(payee,amount,"UPI Payment")
        self.upi_id=upi_id

    def process_payment(self):
        super().process_payment()
        print(f"Successfully transmitted UPI payment of {self.amount} to {self.payee} using UPI Id {self.upi_id}")

if __name__=="__main__":
    name=input("Enter payee name: ")
    amount=int(input("Enter your amount: "))
    mode=input("Enter mode of payment ('upi','card'): ")
    if mode.lower()=="upi":
        id=input("Enter your UPI ID: ")
        payment1=UPIPayment(name,amount,id)
        payment1.process_payment()
    elif mode.lower()=="card":
        card_no=input("Enter your card number: ")
        payment1=CardPayment(name,amount,card_no)
        payment1.process_payment()
    else:
        print("Invalid mode of payment selected")
        
