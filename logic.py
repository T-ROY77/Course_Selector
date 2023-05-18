from Student import *
from Course import *

def removePrevCourses(courseList, prevCourseList):
    # traversing in input list 1( Here [:] is used to create shallow copy)
    for element in courseList[:]:
       # Checking whether the element in list1 is present in list2
       if element.number in prevCourseList:
       # removing that element from the courseList
          courseList.remove(element)
       return courseList


def makeSchedule(courseList, student):
    for x in courseList:
        if student.GPA >= x.requiredGPA:
            if student.major == x.major:
                if student.availability[0][0] <= x.time[0]:
                        print("student can take %s" %x.getCourseName())
                        student.courseList.append(x)
