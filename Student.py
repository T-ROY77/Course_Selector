class Student:
    def __init__(self, name, major, GPA, availability, prevCourses):
        self.name = name
        self.major = major
        self.GPA = GPA
        self.availability = availability
        self.prevCourses = prevCourses
        self.courseList = []

    def showAvailablitySchedule(self):
        print("-------------------------")
        print("   Mon/Wed      Tues/Thurs")
        print("    %s - %s         %s - %s" % (
        self.availability[0][0], self.availability[0][1], self.availability[1][0], self.availability[1][1]))
        print("-------------------------")

    def showTranscript(self):
        print("-------------------------")
        for x in self.prevCourses:
            print("CS%s" % x)
        print("-------------------------")

    def showCourseList(self):
        for x in self.courseList:
            print(str(x))

    def showSchedule(self):
        print("-------------------------")
        print("   Mon/Wed      Tues/Thurs")
        print("    %s - %s         %s - %s" % (
        self.availability[0][0], self.availability[0][1], self.availability[1][0], self.availability[1][1]))
        print("-------------------------")

