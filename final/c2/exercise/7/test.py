import csv
from pathlib import Path

item_id = []
name = []
category = []
stock = []

path = Path.cwd() / "inventory.csv"
f = open(path, "r", encoding="utf-8")
content = csv.reader(f)
next(content)

for items in content:
    item_id.append(items[0])
    name.append(items[1])
    category.append(items[2])
    stock.append(items[3])

filtering = input("Enter category to filter by: ")
if filtering.title() not in category:
    print(f"No items found in category '{filtering}'.")
else:
    print(f"Items in category '{filtering}': ")
    filering = filtering.title()
    for i in range(len(item_id)):
        if category[i] == filtering:
            print(f"Item: {name[i]}, Stock: {stock[i]}")


f.close()