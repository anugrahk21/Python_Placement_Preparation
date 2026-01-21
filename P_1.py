print("Hello World")

#Different types of data structures in Python

#Basic data types : Integer, String, Float, Boolean
#These are the fundamental data types in Python. They can be used to store single values.

# Integer
age=int(input("Enter Age: "))
print("Your age is:", age)

# String
name=input("Enter your name: ")
print("Hello,", name)

# Float
height=float(input("Enter your height including decimal: "))
print("Your height is:", height)

# Boolean
is_student=input("Are you a student? (yes/no): ").strip()=="yes"
print("Is student:", is_student)

# Find area of a square
length=int (input("Enter the length of a side: "))
area=length*length
print("The area of the square is:", area, "square units")

#Other data structures: List, Tuple, Set, Dictionary
#These are more complex data structures that can hold multiple values.