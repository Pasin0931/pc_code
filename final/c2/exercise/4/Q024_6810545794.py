from pathlib import Path

file_ = open("scores.txt", "r", encoding="utf-8")
content = file_.read()

this_ = content.split("\n")
for i in range(len(this_)):
    this_[i] = this_[i].split(",")

students = {}

for i in this_:
    students[i[0]] = i[1]
    
for key, value in students.items():
    print(key)