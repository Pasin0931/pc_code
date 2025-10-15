from pathlib import Path

in_ = input("Enter the filename to read: ")

path_ = Path(in_)

state = path_.exists()

if state == False:
    print(f"Error: The file \'{path_}\' was not found.")
else:
    print("--- File Content ---")
    file_ = open(in_, "r", encoding="utf-8")
    content_ = file_.read()
    print(content_)
    
    print("--- Word Count ---")
    words = content_.split()
    print(f"Total words: {len(words)}")