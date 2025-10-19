# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

file_ = open("scores.txt", "r", encoding="utf-8")
content = file_.read()

this_ = content.split("\n")
for i in range(len(this_)):
    this_[i] = this_[i].split(",")

students = {}
file_.close()

for i in this_:
    students[i[0]] = i[1]

name_max = ""
score_max = 0

total_stu = 0
score_stu = 0

for key, value in students.items():
    score_stu += float(value)
    total_stu += 1
    
    if float(value) > float(score_max):
        score_max = value
        name_max = key
        
avg = score_stu / total_stu
        
print("--- Score Analysis ---")
print(f"Class Average: {avg:.2f}")
print(f"Highest Score: {name_max} with {score_max} points.")