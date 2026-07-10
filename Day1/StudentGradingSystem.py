StudentName=input("enter student name: ")
StudentClass=input("enter student class: ")
Numofsubjects=int(input("enter number of subjects: "))
totalMarks=0
for i in range(Numofsubjects):
    studentSubject=input("enter subject name: ")
    studentMarks=int(input("enter marks: "))
    if studentMarks < 0 or studentMarks > 100:
        print("Invalid Marks")
        exit()
    totalMarks+=studentMarks

averageMarks=totalMarks/Numofsubjects


print("\n")

print("Student Name:", StudentName)
print("Student Class:", StudentClass)
print("Total Marks:", totalMarks)
print("Average Marks:", averageMarks)

if averageMarks>=90:
    print("Grade: A")
elif averageMarks<90 and averageMarks>=70:
    print("Grade: B")
elif averageMarks>=60 and averageMarks<70:
    print("Grade: C")
elif averageMarks<60 and averageMarks>=50:
    print("Grade: D")
else:
    print("Grade: F")

