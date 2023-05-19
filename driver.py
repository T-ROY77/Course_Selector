from Student import *
from Course import *
from Logic import *

#utility functions
#

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

#--------------------------------------------------------------------------------------
#MAIN

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
availability = [availabilityMW, availabilityTT]
print(" Courses Previously Passed")
prevCourses = input(" (Enter course names as a comma separated list): ")

student = Student(name, major, float(gpa), availability, prevCourses)

#hardcoded student
#student = Student("John", "BIOL", 4.0, [[8,20], [7,18]], ["BIOL30", "BIOL54"])

# list of courses
courseList = course_array
courseList.sort(key=timeSort)
newCourseList = removePrevCourses(courseList, student.prevCourses)

#print availability schedule
print(student.name)
print("Availability Schedule")
student.showAvailabilitySchedule()
print()

#calculate the schedule for the student using the algorithm
makeSchedule(newCourseList, student)

#print the output of the algorithm
print()
print("List of courses:")
student.showCourseList()
print()
print("Course Schedule:")
student.showSchedule()


