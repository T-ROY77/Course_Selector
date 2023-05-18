from Student import *
from Course import *

def removePrevCourses(courseList, prevCourseList):
    # traversing course list 1([:] is used to create copy)
    for element in courseList[:]:
       # checking for same element
       if element.number in prevCourseList:
       # removing that element from the courseList
          courseList.remove(element)
       return courseList


def makeSchedule(courseList, student):
    dayIndex = -1
    for x in courseList:
        if x.getCourseName() in student.prevCourses:    #check if student previously passed the course
            print("%s already passed" %x.getCourseName())
        else:
            if student.GPA >= x.requiredGPA:            #check student gpa
                if student.major == x.major:            #check that major matches
                    #check what day course is offered
                    if x.day == "M":
                        dayIndex = 0
                    if x.day == "T":
                        dayIndex = 1
                    if student.availability[dayIndex][0] <= x.time[0]:          #check that student is available at class start
                        if student.availability[dayIndex][1] >= x.time[1]:      #check that student is available at class end
                            #add course to student schedule
                            if len(student.courseList) <= 5:
                                student.courseList.append(x)
