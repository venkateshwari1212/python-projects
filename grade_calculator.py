"""
Create a Python program that takes the marks for 5 subjects as
input from the user, calculates the total marks, the average
score, and assigns a grade based on the average. The grade can
be determined based on typical thresholds, such as:
A: Average >= 90
B: Average >= 75
C: Average >= 60
D: Average >= 50
F: Average < 50
The program should display the total marks, average, and
corresponding grade to the user. 
"""
marks = []
for i in range(1, 6):
    mark = input(f"Enter marks for subject {i}: ")
    if not mark.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter numeric values.")
        exit()
    marks.append(float(mark))

total_marks = sum(marks)
average_marks = total_marks / 5

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 75:
    grade = 'B'
elif average_marks >= 60:
    grade = 'C'
elif average_marks >= 50:
    grade = 'D'
else:
    grade = 'F'

print("\nResults:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
