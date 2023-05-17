class Student:
    def __init__(self, name, age, major, GPA, school_year, availability, prevCourses):
        self.name = name
        self.age = age
        self.major = major
        self.GPA = GPA
        self.school_year = school_year
        self.availability = availability
        self.prevCourses = prevCourses
        self.courseList = []

print("Please enter the following information:")
print("----------------------------------------")
name = input("  Name: ")
age = input("  Age: ")
major = input("  Major: ")
gpa = input("  GPA: ")
school_year = input("  School Year: ")
availability = input("  Availability: ")
prevCourses = input(" previous courses: ")
courseList = input("Course list: ")
