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




# print("Please enter the following information:")
# print("----------------------------------------")
# name = input("  Name: ")
# age = input("  Age: ")
# major = input("  Major: ")
# gpa = input("  GPA: ")
# school_year = input("  School Year: ")
# availability = input("  Availability: ")
# prevCourses = input(" previous courses: ")
# courseList = input("Course list: ")
