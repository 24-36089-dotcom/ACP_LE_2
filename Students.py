class Student:
    def __init__(self, student_id, student_name, email, grades, courses):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades
        self.courses = courses

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    
class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student1 = Student(student_id, student_name, email, grades, courses)
        self.students.append(student1) 
        return "Student added successfully!"
    
    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.student_id == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                return "Student information updated successfully!"  
            return f"Student with ID {student_id} not found."
