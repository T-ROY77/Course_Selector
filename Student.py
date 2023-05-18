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
            print(str(x) + " " + x.getCourseTime())

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

