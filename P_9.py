# OOPs

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

