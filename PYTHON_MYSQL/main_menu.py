# Menu for interacting with the MySQL database module
from functions import MySQLConnection
def main():
    db = MySQLConnection(host="localhost", user="root", password="your_password", database="student")
    db.connect()  # Automatically attempt connection on startup
    while True:
        print("MySQL Database Menu")
        print("1. Connect to Database")
        print("2. Create Table")
        print("3. Insert Data")
        print("4. Update Data")
        print("5. Fetch Data")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        try:
            choice=int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        match choice:
            case 1:
                db.connect()

            case 2:
                db.create_table()

            case 3:
                id=int(input("Enter the id: "))
                name=input("Enter the name: ")
                age=int(input("Enter the age: "))
                db.insert_data(id,name,age)
            
            case 4:
                id=int(input("Enter the id to update: "))
                name=input("Enter the new name: ")
                age=int(input("Enter the new age: "))
                db.update_data(id,name,age)
            
            case 5:
                db.fetch_data()
            
            case 6:
                db.close()
                print("Exiting the program.")
                break 
    
if __name__ == "__main__":  
    main()
