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

to_path = Path.cwd() / "contacts.csv"
fp = open(to_path, mode="w", encoding="utf-8", newline="")
writer = csv.writer(fp)

writer.writerow(["Name", "Email", "Phone"])
for i in contacts_:
    writer.writerow(i)

fp.close()

print("\nContact list saved to contacts.csv.")