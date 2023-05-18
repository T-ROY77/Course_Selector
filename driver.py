from Student import *
from Course import *
from logic import *

#function to sort the course list by starting time
def timeSort(val):
    return val.time[0]

#function to check user input of GPA
def uiNumber():
    while True:
        try:
            gpa = float(input("  GPA: "))
            return gpa
        except ValueError:
            print("Please enter a number")

#function to check user input of availability
def uiAvailability():
    while True:
        user_input = input(" (Enter 2 numbers space separated in military time): ")
        numbers = user_input.split()

        if len(numbers) == 2:
            try:
                number1 = float(numbers[0])
                number2 = float(numbers[1])
                return [number1, number2]
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        else:
            print("Invalid input. Please enter two numbers separated by a space.")


# user input

print("Welcome to the Student Schedule Builder")
print()
print("Please enter the following information:")
print("----------------------------------------")
name = input("  Name: ")
major = input("  Abbreviated Major: ")
gpa = uiNumber()
print("  Availability on Monday and Wednesday")
availabilityMW = uiAvailability()
print("  Availability on Tuesday and Thursday")
availabilityTT = uiAvailability()
print(" Courses Previously Passed")
prevCourses = input(" (Enter course names as a comma separated list): ")

#transfer user input
availability = [availabilityMW, availabilityTT]

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


