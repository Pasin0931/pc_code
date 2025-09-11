def average(score):
    return sum(score) / len(score)

def convert_to_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def read_one_student(index):
    print(f"Please input score of student{index}.")
    test1 = int(input("Test1 : "))
    test2 = int(input("Test2 : "))
    test3 = int(input("Test3 : "))
    print()
    avg = test1 * 0.3 + test2 * 0.3 + test3 * 0.4
    return avg

def read_multiple_students(num_students):
    averages = []
    for i in range(1, num_students + 1):
        avg = read_one_student(i)
        averages.append(avg)
    return averages

num_students = int(input('Numbers of students : '))
student_averages = read_multiple_students(num_students)

for i, avg in enumerate(student_averages):
    grade = convert_to_grade(avg)
    print(f"Average score of Student{i+1} is {avg:.1f}, Grade {grade}.")
