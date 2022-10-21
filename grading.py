# Program Name: grading.py
# Purpose of a program:
# Write a program computing an average of three exam scores
# User enters three exam scores.
# Program prints the exam scores, average of three scores, corresponding letter grade,
# and result of Pass or Fail of a course.

# To pass a course, student should get a grade C or above.

# Average Score    Grade
#    90+	        A
#    80-89	        B
#    70-79	        C
#    60-69	        D
#    0-59	        F

# Example of output
# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.
########################################################################################
# Noble Bautista = Editor

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

# (above) exams are defined as variables where the grade is typed by the user as an integer grade.

grades = [exam_one, exam_two, exam_three] #defines grades as a culmination of all three exam scores
sum = 0
for grade in grades:
  sum = sum + grade 

avg = sum / len(grades) #calculates grade average

if avg >= 90:
    letter_grade = "A" #if grade falls between these parameters, it recieves an A.
elif avg >= 80 and avg <= 89: 
    letter_grade = "B" #if grade falls between these parameters, it recieves a B.
elif avg >= 70 and avg <= 79:
    letter_grade = "C" #if grade falls between these parameters, it recieves a C.
elif avg >= 60 and avg <= 69:
    letter_grade = "D" #if grade falls between these parameters, it recieves a D.
elif avg <= 59:
    letter_grade = "F" #if grade falls between these parameters, it recieves an F.

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
    
#program prints the exam scores, average of three scores, corresponding letter grade,
#and result of Pass or Fail of a course.
