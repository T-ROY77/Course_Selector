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
    Course("166","CS",  "M",[13,14.15],  3.0),
    Course("123A", "CS", "T", [15, 16.15], 3.0),
    Course("152", "CS", "T", [10.3, 11.45], 3.0),
    Course("156", "CS", "T", [12, 13.15], 3.0),
    Course("160", "CS", "M", [16.3, 17.45], 3.0),
    Course("168", "CS", "M", [13.3, 14.45], 3.0),
    Course("175", "CS", "T", [13.3, 14.45], 3.0),
    Course("100W", "CS", "M", [9.3, 10.45], 2.5),
    Course("134", "CS", "M", [13, 14.15], 3.0),

    Course("20", "COMM", "M", [10.3, 11.45], 2.5),
    Course("40", "COMM", "T", [9, 10.15], 2.5),
    Course("41", "COMM", "T", [13.3, 14.45], 2.5),
    Course("45", "COMM", "M", [9, 10.15], 2.5),
    Course("91", "COMM", "T", [10, 11.15], 2.5),
    Course("100", "COMM", "M", [10, 11.15], 2.5),
    Course("101", "COMM", "T", [9.3, 10.45], 2.5),
    Course("121", "COMM", "M", [12, 13.15], 2.5),
    Course("130", "COMM", "T", [15, 16.15], 2.5),
    Course("131", "COMM", "M", [9, 10.15], 2.5),
    Course("145", "COMM", "T", [10, 11.15], 2.5),

    Course("1A", "ENGL", "M", [16.3, 17.45], 2.5),
    Course("1B", "ENGL", "T", [15.3, 16.45], 2.5),
    Course("2", "ENGL", "T", [7.3, 8.45], 2.5),
    Course("22", "ENGL", "M", [8.3, 9.45], 2.5),
    Course("30", "ENGL", "T", [13.3, 14.45], 2.5),
    Course("50", "ENGL", "T", [13.3, 14.45], 2.5),
    Course("60", "ENGL", "M", [7.3, 8.45], 2.5),
    Course("70", "ENGL", "M", [9, 10.15], 2.5),
    Course("71", "ENGL", "T", [13.3, 14.45], 2.5),
    Course("100", "ENGL", "T", [7.3, 8.45], 2.5),

    Course("1", "GEOL", "T", [12.3, 13.45], 2.5),
    Course("2", "GEOL", "M", [9, 10.15], 2.5),
    Course("8", "GEOL", "M", [8.3, 9.45], 2.5),
    Course("4", "GEOL", "T", [13.3, 14.45], 2.5),
    Course("6", "GEOL", "M", [15.3, 16.45], 2.5),
    Course("7", "GEOL", "T", [8.3, 11.15], 2.5),
    Course("9", "GEOL", "T", [13.3, 14.45], 2.5),
    Course("28", "GEOL", "M", [8.3, 9.45], 2.5),
    Course("111", "GEOL", "M", [8.3, 9.45], 2.5),
    Course("112", "GEOL", "M", [13.3, 14.45], 2.5),

    Course("19", "MATH", "T", [7.3, 8.45], 2.5),
    Course("30", "MATH", "M", [9, 10.15], 2.5),
    Course("31", "MATH", "T", [9.3, 10.45], 2.5),
    Course("161", "MATH", "M", [8.3, 9.45], 2.5),
    Course("42", "MATH", "T", [16, 17.15], 2.5),
    Course("39", "MATH", "T", [10.3, 11.45], 2.5),
    Course("1", "MATH", "M", [9, 10.15], 2.5),
    Course("10", "MATH", "M", [11.3, 12.45], 2.5),
    Course("12", "MATH", "T", [10.3, 11.45], 2.5),
    Course("15", "MATH", "M", [12.3, 13.45], 2.5),

    Course("1A", "AMS", "T", [10.3, 11.45], 2.5),
    Course("1B", "AMS", "T", [11.3, 12.45], 2.5),
    Course("10", "AMS", "T", [15.3, 16.45], 2.5),
    Course("100", "AMS", "M", [12, 13.15], 2.5),
    Course("139", "AMS", "T", [13.3, 14.45], 2.5),
    Course("159", "AMS", "M", [13.3, 14.45], 2.5),
    Course("160", "AMS", "T", [16, 17.15], 2.5),
    Course("169", "AMS", "M", [11.3, 12.45], 2.5),
    Course("180", "AMS", "T", [16.3, 17.45], 2.5),
    Course("190", "AMS", "T", [11.3, 12.45], 2.5),

    Course("140", "BIOL", "M", [10.3, 11.45], 2.5),
    Course("10", "BIOL", "M", [13.3, 14.45], 2.5),
    Course("20", "BIOL", "M", [9.3, 10.45], 2.5),
    Course("21", "BIOL", "M", [10.3, 11.45], 2.5),
    Course("30", "BIOL", "M", [7.3, 10.45], 2.5),
    Course("31", "BIOL", "M", [9, 10.15], 2.5),
    Course("54", "BIOL", "M", [10.3, 11.45], 2.5),
    Course("55", "BIOL", "M", [10.3, 11.45], 2.5),
    Course("65", "BIOL", "M", [13, 4.15], 2.5),
    Course("66", "BIOL", "M", [13.3, 14.45], 2.5),

    Course("58A", "KIN", "M", [14.3, 15.45], 2.5),
    Course("58B", "KIN", "T", [14.3, 15.45], 2.5),
    Course("35A", "KIN", "M", [8.3, 9.45], 2.5),
    Course("35B", "KIN", "M", [8.3, 9.45], 2.5),
    Course("2A", "KIN", "T", [8, 9.15], 2.5),
    Course("2B", "KIN", "M", [9.3, 10.45], 2.5),
    Course("3", "KIN", "M", [11, 12.15], 2.5),
    Course("7", "KIN", "T", [6.3, 7.45], 2.5),
    Course("8", "KIN", "M", [12, 13.15], 2.5),
    Course("11", "KIN", "M", [6, 7.15], 2.5),

    Course("172A", "BUS", "M", [11.3, 13.45], 2.5),
    Course("172B", "BUS", "T", [12.3, 11.45], 2.5),
    Course("172C", "BUS", "M", [6.3, 8.45], 2.5),
    Course("172D", "BUS", "M", [8.3, 9.45], 2.5),
    Course("150A", "BUS", "T", [9.3, 10.15], 2.5),
    Course("150B", "BUS", "M", [10, 11.3], 2.5),
    Course("150C", "BUS", "M", [11, 12.15], 2.5),
    Course("12D", "BUS", "T", [14.3, 15.45], 2.5),
    Course("11A", "BUS", "M", [12, 13.15], 2.5),

    Course("140D", "ART", "W", [10.00, 11.15], 2.5),
    Course("140E", "ART", "T", [9.00, 10.15], 2.5),
    Course("141A", "ART", "M", [13.30, 14.45], 3.0),
    Course("141B", "ART", "T", [15.00, 16.15], 3.0),
    Course("142C", "ART", "W", [11.30, 12.45], 2.5),
    Course("143A", "ART", "M", [9.30, 10.45], 2.5),

    Course("120A", "HIST", "M", [12.30, 14.00], 3.5),
    Course("120B", "HIST", "T", [9.00, 10.30], 3.0),
    Course("120C", "HIST", "M", [14.30, 16.00], 3.5),
    Course("120D", "HIST", "W", [10.00, 11.30], 2.5),
    Course("120E", "HIST", "T", [15.00, 16.30], 2.5),
    Course("120F", "HIST", "M", [11.00, 12.30], 3.0),

]