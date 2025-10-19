# Name: Pasin Makcharoen # Student ID: 6810545794

import csv
from pathlib import Path

path_ = Path.cwd() / "inventory.csv"
fp = open(path_, mode="r", encoding="utf-8")
reader = csv.reader(fp)

all_headers = next(reader)

id_ = []
name_ = []
cata = []
stock = []
    
for each_ in reader:
    # print(each_)
    id_.append(each_[0])
    name_.append(each_[1])
    cata.append(each_[2])
    stock.append(each_[3])

in_ = input("Enter category to filter by: ")
if in_.title() not in cata:
    print(f"No items found in category \'{in_}\'.")
else:
    print(f"Items in category \'{in_}\': ")
    in_ = in_.title()
    for i in range(len(id_)):
        if cata[i] == in_:
            print(f"Item: {name_[i]}, Stock: {stock[i]}")

fp.close()