students = {}
while True:
    name = input("Enter name: ")
    if name == "Q":
        break
    scores = float(input("Enter scores: "))
    students[name] = scores
print(students)

below_60 = 0
count = 0

for key, value in students.items():
    print(f"{key} got {value:.2f}")
    if value < 60:
        count += 1
        below_60 += value

if below_60 == 0 and count == 0:
    print("No one got below 60.")
else:
    avg = below_60 / count
    print(f"Average scores of students who got below 60 = {avg:.2f}")