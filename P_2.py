#Simple Calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division: ", a/b)

#Expense tracker
food=int(input("Enter your food expense: "))
transport=int(input("Enter your transport expense: "))
other=int(input("Enter your other expenses: "))
total_exp=food+transport+other
print("Your total expenses are:", total_exp)

#Item details
n=int(input("Enter number of items: "))
#array of size n to store item details
item_details=[]
gst=18
for i in range(n):
    item_name=input(f"Enter name of item {i+1}: ") #i+1 because indexing starts from 0
    price_per_item=float(input(f"Enter price per item of {item_name}: "))
    final_cost=price_per_item + (price_per_item*gst/100)
    item_details.append([item_name, price_per_item, final_cost]) #Appending a list of item details to the main list
    #Therefore, its called a nested list
print(item_details) #Printing the entire list, which contains sub-lists
print("Item Details (Name, Price per item, Final cost including GST):")
for i in item_details:
    print(i)
    #or
    print(f"Price per item of {i[0]} is {i[1]} and final cost including GST is {i[2]}")


#Largest of three numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if (num1>num2) and (num1>num3):
    print(f"{num1} is the largest number")
elif (num2>num1) and (num2>num3):
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")

# Simple Interest Calculator
p=float(input("Enter principal amount: "))
r=float(input("Enter rate: "))
t=float(input("Enter time: "))
si=(p*r*t)/100
print("Simple Interest is:", si)