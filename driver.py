from Student import *
from Course import *


John = Student("John", "Computer Science", 3.2, [[8, 2], [10, 4]], ["46A", "46B", "47"])
introToProg = Course("46A", "CS", [10.30, 11.45], 2.5, [])
introToProg2 = Course("46B", "CS", [10.30, 11.45], 2.5, [introToProg])




print(John.getName())
print(John.getGPA())
John.showAvailablitySchedule()
John.showTranscript()

introToProg.showCourseInfo()
introToProg2.showCourseInfo()

if John.getGPA() >= introToProg.requiredGPA:
    print("John can take %s" %introToProg.getCourseName())
