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
is_student=input("Are you a student? (yes/no): ").strip()=="yes" #strip() is used to remove any extra spaces. Ex " yes " becomes "yes"
print("Is student:", is_student)

# Find area of a square
length=int (input("Enter the length of a side: "))
area=length*length
print("The area of the square is:", area, "square units")
#or
print(f"The area of the square is: {length**2} square units")


#Type conversion
#Converting one data type to another
#int + float will result in float, if we convert float to int, we will lose the decimal part
#int + int will result in int
#float + float will result in float
#str + str will result in concatenation of strings
#str + int/float will result in error

a=int(50)
b=float(50.5)
c=a+b
print("Addition of a and b is:", c, "    its type is:", type(c))

a1="abc"
b1="def"
c1=a1+b1
print("Adding of a1 and b1 is:", c1, "    its type is:", type(c1))


# Marks in 3 subjects
marks1=int(input("Enter marks in subject 1: "))
marks2=int(input("Enter marks in subject 2: "))
marks3=int(input("Enter marks in subject 3: "))
total_marks=marks1+marks2+marks3
avg_marks=total_marks/3
print("Average marks:", avg_marks, "    its type is:", type(avg_marks))
print("Total marks obtained:", total_marks)

#Other data structures: List, Tuple, Set, Dictionary
#These are more complex data structures that can hold multiple values.


#Other data structures: List, Tuple, Set, Dictionary

#List

# Marks of 5 subjects
marks=eval(input("Enter marks of 5 subjects separated by commas: "))
print("Marks entered:", marks)
print(f"Average marks is: {sum(marks)/len(marks):.2f}")
# :.2f is used to format the float value to 2 decimal places, E.g., 75.67


#Tuple
# Coordinates of a point in 2D space

point=eval(input("Enter coordinates of a point (x,y) separated by comma: "))
print("Point coordinates:", point)
for i in point:
    print(i)
print(point[0])  #x coordinate


#Set
# Unique marks obtained in different subjects

marks={1,2,3,4,1,2}
print(marks) #removes duplicates

#Dictionary
# Key-Value pairs

class_a={"Anu":100,"Appu":99}
print(class_a)
for student in class_a:
    print(student, ":", class_a[student]) #student -> key, class_a[student] -> value
