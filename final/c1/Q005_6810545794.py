# Name: Pasin Makcharoen # Student ID: 6810545794

in_ = list(input("Enter a string: ").lower())

no_spc = [i for i in in_ if i != " "]

db = {}

for i in no_spc:
    if i not in db:
        db[i] = 1
    else:
        db[i] += 1

for key, value in db.items():
    print(f"{key}: {value}")