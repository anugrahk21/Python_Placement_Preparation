# a[5]=10
# a[90]=50
#Rest all elements are 0

a=[0]*100
a[5]=10
a[90]=50
for i in a:
    print(i,end=" ")
print("\n")



# Static Memory Allocation of List
b=[0,0,0,0,0] #List of fixed size 5
#or
c=[5] #List of fixed size 1 with initial value 5



# Dynamic Memory Allocation of List

Array=[] #Empty List
while True:
    choice=input("Do you want to add an element to the list? (y/n): ").lower()
    if choice=='y':
        n=int(input("Enter the element you want to add"))
        Array.append(n) #Appending element to the list 
    elif choice=='n':
        print("Current List:",Array)
        break
    else:
        print("Invalid Input! Please enter 'y' or 'n'.")

# The above code is similar to the concept of Dynamic Memory Allocation in C/C++ using malloc(),calloc(),realloc(),free() functions.
# In Python, memory management is handled automatically, and lists can dynamically resize as elements are added or removed.
