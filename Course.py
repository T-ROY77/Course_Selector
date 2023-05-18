class Course:
    def __init__(self, number, major, time, requiredGPA, prereqs=[]):
        self.number = number
        self.requiredGPA = requiredGPA
        self.time = time
        self.major = major
        self.prereqs = prereqs

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

# Creating an array of course objects
course_array = [
    Course("CS-46A", "M/W", "9:00 AM", "10:15 AM", 3.0),
    Course("CS-46B", "Tu/Th", "11:00 AM", "12:15 PM", 2.8),
    Course("CS-47", "Tu/Th", "1:00 PM", "2:15 PM", 3.5),
    Course("CS-146", "Fri", "5:30 PM", "6:45 PM", 3.0),
    Course("CS-147", "M/W", "4:00 PM", "5:15 PM", 2.5),
    Course("CS-149", "Tu/Th", "2:30 PM", "3:45 PM", 3.0),
    Course("CS-151", "Fri", "12:00 PM", "1:15 PM", 2.8),
    Course("CS-152", "M/W", "5:00 PM", "6:15 PM", 3.5),
    Course("CS-154", "M/W", "2:00 PM", "3:15 PM", 2.5),
    Course("CS-157A", "Tu/Th", "1:30 PM", "2:45 PM", 3.0),
    Course("CS-160", "Fri", "3:00 PM", "4:15 PM", 2.8),
    Course("CS-166", "M/W", "1:00 PM", "2:15 PM", 3.0)
]


# Accessing the attributes of course objects
for course in course_array:
    print(f"Course Name: {course.number}")
    print(f"Start Time: {course.start_time}")
    print(f"End Time: {course.end_time}")
    print(f"GPA Requirement: {course.gpa_requirement}")
    print()  # Empty print statement for spacing