# Create student_grades dictionary
student_grades = {
    "Ema": [90, 85, 95],
    "Aria": [75, 80, 70],
    "Tia": [88, 92, 85],
    "Dan": [100, 98, 96],
    "Albert": [60, 65, 70]
}

# Function for average grade
def avg_grade(scores):
    # 3. Print each student’s name and their average grade
    for student, grades in student_grades.items():
        average = avg_grade(grades)
        print(f"{student}: {average:.2f}")

    # Return the average scores
    return sum(scores) / len(scores)

highest_average = -1 

# Find the top student
for student in student_grades:
    average = avg_grade(student_grades[student])
    if average > highest_average:
        highest_average = average
        top_student = student

print(top_student)