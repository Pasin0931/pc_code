# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

file_ = open("journal.log", "a")

while True:
    in_ = input("Enter journal entry (or 'DONE' to exit): ")
    
    if in_ == "DONE":
        print("Journal closed.")
        break
    
    file_.write(in_)
    file_.write("\n")
    
    print("Entry saved.")

file_.close()
