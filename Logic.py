from Student import *
from Course import *

#Logic class
#
#contains the algorithm used to calculate the schedule
#also contains helper function to compare student's previously passed courses with the database

#function removePrevCourses
#
#compares the 2 entered lists of courses
#removes courses that are present in both list from the first list
#returns the updated courselist
def removePrevCourses(courseList, prevCourseList):
    # traversing course list 1([:] is used to create copy)
    for element in courseList[:]:
       # checking for same element
       if element.number in prevCourseList:
       # removing that element from the courseList
          courseList.remove(element)
       return courseList

#function makeSchedule
#
#calculates the schedule from the course list and the student parameters
#loops through the database of courses
#compares the course information with the student information
#if all information passes its rule, the course is added to the student's course list
#a total of 6 courses can be added to the student's course list
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
