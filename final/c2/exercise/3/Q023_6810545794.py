from pathlib import Path

file_ = open("journal.log", "a")

while True:
    in_ = input("Enter journal entry (or \'DONE\' to exit): ")
    
    if in_ == "DONE":
        file_ = open("journal.log", "r")
        file_.readlines()
        print("Journal closed.")
        break
    
    file_.write(in_)
    file_.write("\n")
    
    print("Entry saved.")