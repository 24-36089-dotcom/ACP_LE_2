# Define the Student class to hold individual student information
class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (str(student_id), student_name)                              # Store ID as string for consistency
        self.email = email
        self.grades = grades if grades else {}                                      # Initialize as empty dictionary if None
        self.courses = courses if courses else set()                                # Initialize as empty set if None

# String representation of the Student object
    def __str__(self):
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {list(self.courses)}") # Convert set to list for better readability

# Method to calculate GPA based on grades
    def calculate_gpa(self):
        if not self.grades:
            return "No grades available to calculate GPA."
        
        gpa_value = 0.0
        for score in self.grades.values():
            if score >= 90:
                gpa_value += 4.0
            elif score >= 80:
                gpa_value += 3.0
            elif score >= 70:
                gpa_value += 2.0
            elif score >= 60:
                gpa_value += 1.0
            else:
                gpa_value += 0.0

        gpa = round(gpa_value / len(self.grades), 2)
        return f"GPA: {gpa}"

# Define the StudentRecords class to manage multiple students   
class StudentRecords:
    def __init__(self):
        self.students = [] # List to store Student objects

# Methods to manage student records
    def add_student(self, student_id, student_name, email=None, grades=None, courses=None): #
        student_id = str(student_id)
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student) # Add new student to the list
        return "Student added successfully!"

# Method to update student information   
    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name [0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)
                if courses:
                    student.courses.update(courses)
                return "Student information updated successfully!"  
        return f"Student with ID {student_id} not found."

# Method to delete a student record   
    def delete_student(self, student_id):
        student_id = str(student_id)
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully."
        return f"Student with ID {student_id} not found."

# Method to enroll a student in a course  
    def enroll_course(self, student_id, courses):
        student_id = str(student_id)
        for student in self.students:
            # Check if the student is already enrolled in the course
            if student.id_name[0] == student_id:
                if courses in student.courses:
                    return f"{student.id_name[1]} is already enrolled in course {courses}."
                else:
                    student.courses.add(courses)
                return f"Student {student_id} enrolled in course {courses}."
        return f"Student with ID {student_id} not found."

# Method to search for a student by ID or name    
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)                       
        return f"Student with ID {student_id} not found."

# Method to search for a student by name (case insensitive)    
    def search_name(self, student_name):
        matches = []                                                                # List to hold matching students
        for student in self.students:
            if student_name.lower() in student.id_name[1].lower():                  # Case insensitive search
                matches.append(student)                                             # Add matching student to the list
        if matches:
            return "\n".join(str(student) for student in matches)                   # Return all matches as a string
        return f"Student with name {student_name} not found."

# Method to display all students in the records    
    def display_all_students(self):
        if not self.students:
            return "No students in the records."
        return "\n".join(str(student) for student in self.students)
    
record = StudentRecords()

# Add student information
print("Adding students:")
print(record.add_student("2004", "Hanni Pham", "hanni@gmail.com", {"Math": 95, "Science": 90}, {"Math", "Science"}))
print(record.add_student("2006", "Kang Haerin", "vanessakang@gmail.com", {"Math": 95, "Science": 97}, {"Math", "Science"}))
print(record.add_student("2001", "Kim Min-jeong", "winter@gmail.com", {"Math": 95, "Science": 94}, {"Math", "Science"}))

# Show all students
print("\nAll students:")
print(record.display_all_students())

# Update student information
print("\nUpdating student information for Student ID 2004:")
print(record.update_student("2004", email="hannibunny@gmail.com", grades={"English": 88}, courses={"English"}))
print(record.display_all_students())

# Delete a student
print("\nDelete student:")
print(record.delete_student("2001"))
print(record.delete_student("2010"))  # Non-existent student
print(record.display_all_students())

# Enroll a student in a course
print("\nEnrolling student in a course:")
print(record.enroll_course("2006", "History"))
print(record.enroll_course("2006", "Math"))  # Already enrolled
print(record.enroll_course("2010", "History"))  # Non-existent student
print(record.display_all_students())

# Search for a student by ID
print("\nSearching for student by ID:")
print(record.search_student("2004"))
print(record.search_student("2010"))  # Non-existent student

# Search for a student by name
print("\nSearching for student by name:")
print(record.search_name("Kang Haerin"))
print(record.search_name("John Doe"))  # Non-existent student

# Calculate GPA for a student
print("\nCalculating GPA:")
for student in record.students:
    print(f"Student ID {student.id_name[0]}: {student.calculate_gpa()}")
