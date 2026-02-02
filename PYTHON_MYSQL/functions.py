# Python MSQL connectivity example
import mysql.connector as mysql

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None # Contains the connection object

    def connect(self):
        try:
            self.connection = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection to MySQL database established successfully.")
        except mysql.Error as err:
            print(f"Error: {err}")

    def create_table(self):
        if not self.connection:
            print("Error: Not connected to the database. Please connect first.")
            return
        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
        """
        cursor = self.connection.cursor() # cursor() -> to execute SQL queries
        cursor.execute(query) # .execute() -> to execute the SQL query
        print("Table 'students' verified/created successfully.")

    def insert_data(self,id,name,age):
        if not self.connection:
            print("Error: Not connected to the database. Please connect first.")
            return
        query="INSERT IGNORE INTO students (id, name, age) VALUES (%s, %s, %s)"
        values = (id, name, age) # Assigning values to be inserted
        cursor = self.connection.cursor() # cursor() -> to execute SQL queries
        cursor.execute(query, values) # .execute() -> to execute the SQL query
        self.connection.commit() # .commit() -> to save the changes
        if cursor.rowcount > 0:
            print("Data inserted successfully.")
        else:
            print("Data already exists or insertion skipped.")
    
    def update_data(self,id,name,age):
        if not self.connection:
            print("Error: Not connected to the database. Please connect first.")
            return
        query="UPDATE students SET name=%s, age=%s WHERE id=%s"
        values = (name, age, id) # Assigning values to be updated
        cursor = self.connection.cursor() # cursor() -> to execute SQL queries
        cursor.execute(query, values) # .execute() -> to execute the SQL query
        self.connection.commit() # .commit() -> to save the changes
        if cursor.rowcount > 0:
            print("Data updated successfully.")
        else:
            print("No matching record found or update skipped.")

    def fetch_data(self):
        if not self.connection:
            print("Error: Not connected to the database. Please connect first.")
            return
        query = "SELECT * FROM students"
        cursor = self.connection.cursor() # cursor() -> to execute SQL queries
        cursor.execute(query) # .execute() -> to execute the SQL query
        results = cursor.fetchall() # Fetch all results
        for row in results:
            print(row)

    def close(self):
        if self.connection:
            self.connection.close()
            print("MySQL connection closed.")

#if __name__ == "__main__":
    #db = MySQLConnection(host="localhost", user="root", password="your_password", database="student")
    #db.connect()
    # db.create_table() # Uncomment if a table needs to created.
    #db.insert_data(6, "Aimika K", 1)
    #db.update_data(2, "Anugrah K", 19)
    #db.fetch_data()
    #db.close()