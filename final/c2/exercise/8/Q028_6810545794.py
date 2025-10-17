# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path
import csv

regions = {}

path_ = Path.cwd() / "sales.tsv"
fp = open(path_, mode="r", encoding="utf-8", newline="")
contents_ = csv.reader(fp)
header = next(contents_)

# print(header)

for i in contents_:
    this_ = i[0].split()
    
    if this_[0] not in regions:
        regions[this_[0]] = float(this_[2])
    else:
        regions[this_[0]] += float(this_[2])
    
print("--- Regional Sales Summary ---")
for key, value in regions.items():
    print(f"{key}: {value:.2f}")