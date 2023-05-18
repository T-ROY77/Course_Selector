from Student import *
from Course import *
from logic import *

#function to sort the course list by starting time
def timeSort(val):
    return val.time[0]


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


student = Student("John", "CS", 4.0, [[1,23], [1,23]], [])

courseList = course_array
courseList.sort(key=timeSort)

print(student.name)
print(student.GPA)
#student.showAvailablitySchedule()
#student.showTranscript()

newCourseList = removePrevCourses(courseList, student.prevCourses)

# printing InputList_1 after removing the same or common elements
print("CourseList after removing same elements:", newCourseList)

makeSchedule(newCourseList, student)

student.showCourseList()
student.showSchedule()


