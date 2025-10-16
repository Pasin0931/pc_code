# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

file_ = open("scores.txt", "r", encoding="utf-8")
content = file_.read()

this_ = content.split("\n")
for i in range(len(this_)):
    this_[i] = this_[i].split(",")

students = {}

for i in this_:
    students[i[0]] = i[1]

name_max = ""
score_max = 0

total_stu = 0
score_stu = 0

for key, value in students.items():
    score_stu += int(value)
    total_stu += 1
    
    if int(value) >= score_max:
        score_max = int(value)
        name_max = key
        
avg = score_stu / total_stu
avg = f"{avg:.2f}"
        
print("--- Score Analysis ---")
print(f"Class Average: {avg}")
print(f"Highest Score: {name_max} with {score_max} points.")