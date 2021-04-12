"""
This is the scoring criteria:
    Scores 91 - 100: Grade = "Outstanding"
    Scores 81 - 90: Grade = "Exceeds Expectations"
    Scores 71 - 80: Grade = "Acceptable"
    Scores 70 or lower: Grade = "Fail"
"""

if __name__ == "__main__":
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }
    print(student_scores)

    student_grades = {}
    for name, score in student_scores.items():
        grade = None
        if 91 <= score <= 100:
            grade = 'Outstanding'
        elif 81 <= score <= 90:
            grade = 'Exceeds Expectations'
        elif 71 <= score <= 80:
            grade = 'Acceptable'
        elif score <= 70:
            grade = 'Fail'
        else:
            grade = 'Invalid Score'
        student_grades[name] = grade
    print(student_grades)
