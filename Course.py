class Course:
    def __init__(self, courseNumber, major, time, requiredGPA, prereqs=[]):
        self.courseNumber = courseNumber
        self.requiredGPA = requiredGPA
        self.time = time
        self.major = major
        self.prereqs = prereqs

    def getmajor(self):
        return self.major

    def getCourseNumber(self):
        return self.courseNumber

    def getTime(self):
        return self.time

    def getRequiredGPA(self):
        return self.requiredGPA

    def getCourseName(self):
        return "%s%s" % (self.major, self.courseNumber)

    def showCourseInfo(self):
        self.getCourseName()
        print("%s - %s" %(self.time[0], self.time[1]))
        print("GPA requirement: %s" %self.requiredGPA)
        print("Prerequisites: ")
        for x in self.prereqs:
            print("%s" %x.getCourseName())
        print("----------")