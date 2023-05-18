from Student import *
from Course import *
from logic import *

#function to sort the course list by starting time
def timeSort(val):
    return val.time[0]



# user input

print("Welcome to the Student Schedule Builder")
print()
print("Please enter the following information:")
print("----------------------------------------")
name = input("  Name: ")
major = input("  Abbreviated Major: ")
gpa = input("  GPA: ")
print("  Availability on Monday and Wednesday")
availabilityMW = input(" (Enter 2 numbers space separated in military time): ")
print("  Availability on Tuesday and Thursday")
availabilityTT = input(" (Enter 2 numbers space separated in military time): ")
print(" Courses Previously Passed")
prevCourses = input(" (Enter course names as a comma separated list): ")

#transfer user input
MW = availabilityMW.split()
TT = availabilityTT.split()
availability = [TT, MW]
availability[0] = [float(i) for i in availability[0]]
availability[1] = [float(i) for i in availability[1]]

student = Student(name, major, float(gpa), availability, prevCourses)

#hardcoded student
# student = Student("John", "CS", 4.0, [[1,23], [1,23]], ["CS160"])

# list of courses
courseList = course_array
courseList.sort(key=timeSort)

print(student.name)
print(student.GPA)
print("Availability Schedule")
student.showAvailablitySchedule()
print()
#student.showTranscript()

newCourseList = removePrevCourses(courseList, student.prevCourses)
makeSchedule(newCourseList, student)

print()
print("List of courses:")
student.showCourseList()
print()
print("Course Schedule:")
student.showSchedule()


