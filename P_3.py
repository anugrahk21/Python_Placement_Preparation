# Password validation program

correct_pass="admin123"
while True:
    entered_pass=input("Enter your password: ")
    if (entered_pass==correct_pass):
        print("Access Granted")
        break
    else:
        print("Access Denied")



# ATM dispensing cash

withdraw_amount=int(input("Enter amount to withdraw: "))
if (withdraw_amount<=0):
    print("Enter a valid amount")
elif (withdraw_amount % 200 != 0 and withdraw_amount % 500 != 0 and (withdraw_amount < 200 and withdraw_amount < 500)):
    print("Amount should be in multiples of 200 or 500")
   
# if withdraw_amount % 200 == 0 or withdraw_amount % 500 == 0 or withdraw_amount >= 700:
#     print("Discharging Amount:", withdraw_amount)

else:
    print("Discharging Amount:", withdraw_amount)



# Wishing program

time=int(input("Enter time in 24-hour format (0-23): "))
if (time<=0 or time>23):
    print("Enter valid time")
elif(time>=5 and time<12):
    print("Good Morning")
elif(time>=12 and time<16):
    print("Good Afternoon")
elif(time>=16 and time<19):
    print("Good Evening")
else:
    print("Good Night")



# Multiplication table of n program

n=int (input("Enter a number: "))
for i in range(1,11):
    print(n, "X",i,"=", n*i)



#prime number checker

num=int(input("Enter a number: "))
prime=True
if(num<=1):
    print(f"{num} is not a prime number")
for i in range(2,num): #or range(2,num//2+1) to optimize
    if(num%i==0):
        print(num,"is not a prime number")
        prime=False
        break
if prime:
    print(num,"is a prime number")



# Palindrome checker

a=input("Enter your string: ")
if(a==a[::-1]):
    print("Its a palindrome")

else:
    print("Its not a palindrome")
