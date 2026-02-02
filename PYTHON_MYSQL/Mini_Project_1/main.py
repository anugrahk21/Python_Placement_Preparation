from admission_db import AdmissionDB

def main():
    # Configure database credentials here
    HOST = "localhost"
    USER = "root"
    PASSWORD = "your_password" # Using credentials referencing main_menu.py context
    DATABASE = "admission_db"

    # Initialize the AdmissionDB class
    db = AdmissionDB(host=HOST, user=USER, password=PASSWORD, database=DATABASE)

    while True:
        print("\n=== College Admission Portal ===")
        print("1. Add Student")
        print("2. Apply for Admission")
        print("3. View Applications")
        print("4. Approve Application")
        print("5. Reject Application")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        
        match choice:
            case 1:
                print("\n--- Add Student ---")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                city = input("Enter City: ")
                db.add_student(name, email, phone, city)
            
            case 2:
                print("\n--- Apply for Admission ---")
                try:
                    student_id = int(input("Enter Student ID: "))
                    course = input("Enter Course Name: ")
                    marks = float(input("Enter Marks: "))
                    db.apply_for_admission(student_id, course, marks)
                except ValueError:
                    print("Invalid input for ID or Marks. Please enter numeric values.")
            
            case 3:
                db.view_all_applications()
            
            case 4:
                print("\n--- Approve Application ---")
                try:
                    app_id = int(input("Enter Application ID to Approve: "))
                    db.update_status(app_id, "Approved")
                except ValueError:
                    print("Invalid input. Application ID must be an integer.")
            
            case 5:
                print("\n--- Reject Application ---")
                try:
                    app_id = int(input("Enter Application ID to Reject: "))
                    db.update_status(app_id, "Rejected")
                except ValueError:
                    print("Invalid input. Application ID must be an integer.")
            
            case 6:
                db.close()
                print("Exiting the portal. Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
