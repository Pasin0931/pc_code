# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path
import csv

contacts_ = []

c_contact = 1

while True:
    print(f"--- Enter Contact {c_contact} ---")
    
    this_contact = []
    
    n_ = input("Name: ")
    this_contact.append(n_)
    
    e_ = input("Email: ")
    this_contact.append(e_)
    
    p_ = input("Phone: ")
    this_contact.append(p_)
    
    contacts_.append(this_contact)
    
    add_c = input("Add another contact? (yes/no): ")
    if add_c == "no":
        break
    c_contact += 1
    print()
    
# print(contacts_)
dt = "Name,Email,Phone"
for i in contacts_:
    dt += f"\n{i[0]},{i[1]},{i[2]}"
    
# print()
# print(dt)
# print()

to_path = Path.cwd() / "contacts.csv"
fp = open(to_path, mode="a", encoding="utf-8")
writer = csv.writer(fp)
writer.writerow(dt)
fp.close()

print("\nContact list saved to contacts.csv.")