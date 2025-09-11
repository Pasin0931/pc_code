import math

def read_in():
    scores = []
    while True:
        in_score = input("Enter score (or just ENTER to end): ")
        if in_score == "":
            break
        scores.append(int(in_score))
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores)

def calculate_sd(scores, mean):
    n = len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / (n - 1)
    return math.sqrt(variance)

def get_grade(score, mean, sd):
    if score >= mean + 1.5 * sd:
        return "A"
    elif score >= mean + 1.0 * sd:
        return "B+"
    elif score >= mean + 0.5 * sd:
        return "B"
    elif score >= mean:
        return "C+"
    elif score >= mean - 0.5 * sd:
        return "C"
    elif score >= mean - 1.0 * sd:
        return "D+"
    elif score >= mean - 1.5 * sd:
        return "D"
    else:
        return "F"

def display(scores, mean, sd):
    print(f"Average score is {mean:.2f}")
    print(f"Standard deviation is {sd:.2f}")
    for i, score in enumerate(scores):
        grade = get_grade(score, mean, sd)
        print(f"Score #{i+1}: {score} grade: {grade}")

scores = read_in()
if len(scores) >= 2:
    mean = calculate_average(scores)
    sd = calculate_sd(scores, mean)
    display(scores, mean, sd)
