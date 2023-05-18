class Course:
    def __init__(self, number, major, day, time, requiredGPA, prereqs=[]):
        self.number = number
        self.day = day
        self.requiredGPA = requiredGPA
        self.time = time
        self.major = major
        self.prereqs = prereqs

    def getCourseName(self):
        return "%s%s" % (self.major, self.number)

    def getCourseTime(self):
        return "%s - %s" % (self.time[0], self.time[1])

    def showCourseInfo(self):
        self.getCourseName()
        print("%s - %s" %(self.time[0], self.time[1]))
        print("GPA requirement: %s" %self.requiredGPA)
        print("Prerequisites: ")
        for x in self.prereqs:
            print("%s" %x.getCourseName())
        print("----------")


    def __str__(self):
        return self.getCourseName()

# Creating an array of course objects
course_array = [
    Course("46A", "CS",  "M", [9,10.15], 3.0),
    Course("46B", "CS", "T", [11,12.15], 2.8),
    Course("47", "CS", "T", [13,14.15], 3.5),
    Course("146","CS",  "T",[17.3,18.45],  3.0),
    Course("147","CS",  "M", [16,17.15], 2.5),
    Course("149","CS",  "T",[14.3,15.45],  3.0),
    Course("151","CS",  "T",[12,13.15],2.8),
    Course("152", "CS", "M", [17,18.15], 3.5),
    Course("154","CS",  "M",[14,15.15],  2.5),
    Course("157A","CS",  "T",[13.3,14.45],  3.0),
    Course("160","CS",  "T", [15,16.15], 2.8),
    Course("166","CS",  "M",[13,14.15],  3.0)
]