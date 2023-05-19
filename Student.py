from Course import *
from Logic import *

#student class
#represents a college student
#
#student has a name
#student has a major
#student has a current GPA
#student has an availability
#student has a list of previously passed courses

class Student:
    def __init__(self, name, major, GPA, availability, prevCourses):
        self.name = name
        self.major = major
        self.GPA = GPA
        self.availability = availability
        self.prevCourses = prevCourses
        self.courseList = []

    #function showAvailabilitySchedule
    #
    #prints the availability schedule for the student
    #only prints availability for Monday through Thursday
    #assumes availability is the same on Monday and Wednesday
    #assumes availability is the same on Tuesday and Thursday
    def showAvailabilitySchedule(self):
        print("-------------------------")
        print("   Mon/Wed      Tues/Thurs")
        print("    %s - %s         %s - %s" % (
        self.availability[0][0], self.availability[0][1], self.availability[1][0], self.availability[1][1]))
        print("-------------------------")

    #function showCourseList
    #
    #prints the calculated course list for the student
    #assumes the algorithm has calculated the course list for the student
    def showCourseList(self):
        for x in self.courseList:
            print(str(x) + " " + x.getCourseTime())

    #function showSchedule
    #
    #prints the calculated course schedule for the student
    #assumes the algorithm has calculated the course list for the student
    def showSchedule(self):
        print("-------------------------")
        #print monday wednesday schedule
        print("       Mon/Wed ")
        for x in self.courseList:
            if x.day == "M":
                print("%s     %s - %s" % (
                    str(x), x.time[0],  x.time[1]))

        print()

        #print tuesday thursday schedule
        print("       Tues/Thurs ")
        for x in self.courseList:
            if x.day == "T":
                print("%s     %s - %s" % (
                    str(x), x.time[0], x.time[1]))
        print("-------------------------")

