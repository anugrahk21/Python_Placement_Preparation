import mysql.connector as mysql

class AdmissionDB:
    def __init__(self, host, user, password, database="admission_db"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self._establish_connection() #self. because we are calling a method of the class from within the class
        # but when outside the class we use db.method()     here db is a object of the class

    def _establish_connection(self):
        """Establishes connection and creates database/tables if needed."""
        try:
            # Connect to MySQL Server to ensure DB exists
            temp_conn = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = temp_conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            temp_conn.close()

            # Connect to the specific database
            self.connection = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"Connection to MySQL database '{self.database}' established successfully.")
            self._create_tables()

        except mysql.Error as err:
            print(f"Error connecting to database: {err}")

    def _create_tables(self):
        """Creates the required tables if they do not exist."""
        if not self.connection:
            print("Error: Not connected to the database.")
            return
        
        try:
            cursor = self.connection.cursor()
            
            # Create students table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                phone VARCHAR(15),
                city VARCHAR(50)
            )
            """)

            # Create applications table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                application_id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT,
                course VARCHAR(100) NOT NULL,
                marks FLOAT,
                status VARCHAR(20),
                applied_date DATE,
                FOREIGN KEY (student_id) REFERENCES students(student_id)
            )
            """)
            
            self.connection.commit()
            print("Required tables ('students', 'applications') verified/created successfully.")
            
        except mysql.Error as err:
            print(f"Error creating tables: {err}")

    def add_student(self, name, email, phone, city):
        """Add a new student to the students table."""
        if not self.connection:
            print("Error: Not connected to the database.")
            return

        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO students (name, email, phone, city) VALUES (%s, %s, %s, %s)"
            values = (name, email, phone, city)
            cursor.execute(query, values)
            self.connection.commit()
            print(f"Student '{name}' added successfully with ID: {cursor.lastrowid}")
        except mysql.Error as err:
            print(f"Error adding student: {err}")

    def apply_for_admission(self, student_id, course, marks):
        """Insert an admission application."""
        if not self.connection:
            print("Error: Not connected to the database.")
            return

        try:
            cursor = self.connection.cursor()
            # Check if student exists first
            cursor.execute("SELECT student_id FROM students WHERE student_id = %s", (student_id,))
            if not cursor.fetchone():
                print(f"Error: Student with ID {student_id} does not exist.")
                return

            query = "INSERT INTO applications (student_id, course, marks, status, applied_date) VALUES (%s, %s, %s, 'Pending', CURDATE())"
            values = (student_id, course, marks) # Values for the placeholders in the query
            cursor.execute(query, values)
            self.connection.commit()
            print("Application submitted successfully. Status: Pending")
        except mysql.Error as err:
            print(f"Error applying for admission: {err}")

    def view_all_applications(self):
        """Display all applications joined with student names."""
        if not self.connection:
            print("Error: Not connected to the database.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.application_id, s.name, a.course, a.marks, a.status, a.applied_date 
            FROM applications a
            JOIN students s ON a.student_id = s.student_id
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            if not results:
                print("No applications found.")
                return

            print("\n--- All Applications ---")
            print(f"{'App ID':<8} {'Student Name':<20} {'Course':<15} {'Marks':<8} {'Status':<10} {'Date':<12}")
            print("-" * 75)
            for row in results:
                # 'row' structure: (id, name, course, marks, status, date)
                app_id, name, course, marks, status, date = row  # row is a tuple of values
                # like a,b,c=(1,2,3)    , a=1,b=2,c=3
                print(f"{app_id:<8} {name:<20} {course:<15} {marks:<8} {status:<10} {date}")
            print("-" * 75)
            
        except mysql.Error as err:
            print(f"Error fetching applications: {err}")

    def update_status(self, application_id, status):
        """Approve or reject an application."""
        if not self.connection:
            print("Error: Not connected to the database.")
            return

        if status not in ['Approved', 'Rejected']:
            print("Invalid status. Please choose 'Approved' or 'Rejected'.")
            return

        try:
            cursor = self.connection.cursor()
            # Check if application exists
            cursor.execute("SELECT application_id FROM applications WHERE application_id = %s", (application_id,))
            if not cursor.fetchone():
                print(f"Error: Application with ID {application_id} does not exist.")
                return

            query = "UPDATE applications SET status = %s WHERE application_id = %s"
            values = (status, application_id)
            cursor.execute(query, values)
            self.connection.commit()
            print(f"Application {application_id} status updated to '{status}'.")
        except mysql.Error as err:
            print(f"Error updating status: {err}")

    def close(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()
            print("MySQL connection closed.")
