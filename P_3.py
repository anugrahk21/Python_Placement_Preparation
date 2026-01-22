# Password validation program
while True:
    entered_pass=input("Enter your password: ")
    correct_pass="admin123"
    if (entered_pass==correct_pass):
        print("Access Granted")
        break
    else:
        print("Access Denied")