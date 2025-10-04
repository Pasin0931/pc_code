# Name: Pasin Makcharoen # Student ID: 6810545794

nm_stu = int(input("How many students? "))
print()

db = {}
count = 1

for i in range(nm_stu):
    name = input(f"Enter name for student {count}: ")
    score = input(f"Enter scores for Alice {name}: ").split()

    mapped_sc = list(map(int, score))

    db[name] = mapped_sc
    count += 1
    print()

print("Student Averages:")

for key, value in db.items():
    avg = sum(value) / len(value)
    val = f"{avg:.2f}"
    
    print(f"{key}: {val}")