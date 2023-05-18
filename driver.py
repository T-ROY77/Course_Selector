from Student import *
from Course import *
from logic import *

#John = Student("John", "CS", 3.2, [[8, 2], [10, 4]], ["46A", "46B", "47"])


# print("Please enter the following information:")
# print("----------------------------------------")
# name = input("  Name: ")
# age = input("  Age: ")
# major = input("  Major: ")
# gpa = input("  GPA: ")
# school_year = input("  School Year: ")
# availability = input("  Availability: ")
# prevCourses = input(" previous courses: ")
#
# student = Student(name, major, gpa, availability, prevCourses)


student = Student("John", "CS", 2.5, [[1-23], [1-23], [1-23]], [])

courseList = course_array

print(student.name)
print(student.GPA)
#student.showAvailablitySchedule()
#student.showTranscript()

newCourseList = removePrevCourses(courseList, student.prevCourses)

# printing InputList_1 after removing the same or common elements
print("potentialCourseList after removing same elements:", newCourseList)

makeSchedule(newCourseList, student)

print(student.courseList)


