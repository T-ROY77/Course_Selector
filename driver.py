from Student import *
from Course import *


#John = Student("John", "CS", 3.2, [[8, 2], [10, 4]], ["46A", "46B", "47"])


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

John = Student(name, major, gpa, availability, prevCourses)



introToProg = Course("46A", "CS", [10.30, 11.45], 2.5, [])
introToProg3 = Course("46C", "CS", [10.30, 11.45], 2.5, [introToProg])

courseList = [introToProg, introToProg3]
potentialCourseList = courseList
prevCourseList = John.prevCourses

print(John.getName())
print(John.getGPA())
John.showAvailablitySchedule()
John.showTranscript()

introToProg.showCourseInfo()
introToProg3.showCourseInfo()


# traversing in input list 1( Here [:] is used to create shallow copy)
for element in potentialCourseList[:]:
   # Checking whether the element in list1 is present in list2
   if element.courseNumber in prevCourseList:
   # removing that element from the courseList
      potentialCourseList.remove(element)

# printing InputList_1 after removing the same or common elements
print("potentialCourseList after removing same elements:", potentialCourseList)



for x in courseList:
    if John.getGPA() >= x.requiredGPA:
        if John.getMajor() == x.getmajor():
            if John.getAvailability()[0][0] <= x.getTime()[0]:
                    print("John can take %s" %x.getCourseName())
                    John.courseList.append(x)


print(John.courseList)


