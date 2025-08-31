# Enter student score (or ENTER to end): 87↵
# Enter student score (or ENTER to end): 56↵
# Enter student score (or ENTER to end): 73↵
# Enter student score (or ENTER to end): 59↵
# Enter student score (or ENTER to end): 90↵
# Enter student score (or ENTER to end): 72↵
# Enter student score (or ENTER to end): ↵
# Score #1: 87
# Score #2: 56
# Score #3: 73
# Score #4: 59
# Score #5: 90
# Score #6: 72
# Average score is 72.83
# Minimum score is 56
# Maximum score is 90

def read_input():
    students = int(input("How many students? "))

    temp = []
    for i in range(0, students):
        read = str(input("Enter student score: "))
        temp.append(read)

    return temp

def calculate(temp):
    sum = 0
    for i in temp:
        sum += int(i)
    average_val = sum / len(temp)

    min_val = min(temp)

    max_val = max(temp)

    return average_val, min_val, max_val

def display_values(avg, mi, mx, temp):
    for i in range(1, len(temp) + 1):
        print(f"Score #{i}: {temp[i - 1]}")

    print(f"Average score is {avg:.2f}")
    print(f"Minimum score is {mi}")
    print(f"Maximum score is {mx}")


vals = read_input()
avg, mi, mx = calculate(vals)
display_values(avg, mi, mx, vals)