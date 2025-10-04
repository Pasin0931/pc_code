# Name: Pasin Makcharoen # Student ID: 6810545794

import math

db = {}

while True:
    in_ = input("Enter group name and coordinates (x y z) or 'done' to finish: ").split()
    if in_[0].lower() == "done":
        break

    if len(in_) != 4:
        print("Invalid input")
        continue

    name = in_[0]
    x = float(in_[1])
    y = float(in_[2])
    z = float(in_[3])

    db[name] = (x, y, z)

pairs = []
group_names = list(db.keys())

for i in range(len(group_names)):
    for j in range(i + 1, len(group_names)):
        g1 = group_names[i]
        g2 = group_names[j]
        x1, y1, z1 = db[g1]
        x2, y2, z2 = db[g2]
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        if g1 < g2:
            pair_name = f"{g1} to {g2}"
        else:
            pair_name = f"{g2} to {g1}"
        pairs.append([pair_name, distance])

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[j][1] < pairs[i][1]:
            pairs[i], pairs[j] = pairs[j], pairs[i]
        elif pairs[j][1] == pairs[i][1] and pairs[j][0] < pairs[i][0]:
            pairs[i], pairs[j] = pairs[j], pairs[i]

print("\nTop minimum distance pairs (show only top-5):")

limit = 5
if len(pairs) < 5:
    limit = len(pairs)

for i in range(limit):
    pair_name = pairs[i][0]
    distance = pairs[i][1]
    print(f"{i + 1}. {pair_name}: {distance:.2f}")