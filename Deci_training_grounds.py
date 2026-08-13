import numpy as np
grades = np.array([
    [85, 90, 78], # Ahmed
    [92, 88, 95], # Fatma
    [78, 82, 80], # Omar
    [88, 91, 87], # Nour
    [95, 89, 93]  # Sara
])#exam1,exam2,exam3
print(f"Minimum grade: {grades.min()}, Maximum grade: {grades.max()}")
average_grades = grades.mean(axis=1)
student_list = ["Ahmed", "Fatma", "Omar", "Nour", "Sara"]
print("Average grades for each student:")
for x,y in zip(average_grades, student_list):
    print(f"{y}: {x}")
    if x == average_grades.max():
        print(f"{y} has the highest average grade.")
average_grades_per_exam = grades.mean(axis=0)
print("Average grade for each exam:")
for i, avg in enumerate(average_grades_per_exam):
    print(f"Exam {i+1}: {avg}")
    if avg == average_grades_per_exam.min():
        print(f"Exam {i+1} is the most difficult exam.")
