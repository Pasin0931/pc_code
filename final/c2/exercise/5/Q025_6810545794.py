# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

state = True

in_1 = input("Enter the input filename: ")
to_path = Path.cwd() / f"{in_1}"

if to_path.exists():
    content_ = open(to_path, mode="r", encoding="utf-8")
    content_ = content_.read()

    in_2 = input("Enter the word to find: ")
    in_3 = input("Enter the replacement word: ")
    in_4 = input("Enter the output filename: ")
else:
    state = False
    print(f"Error: Input file \'{in_1}\' not found.")

if state == True:
    content_ = content_.replace(in_2, in_3)
    
    this_path = Path.cwd() / f"{in_4}"
    fp = open(this_path, mode="w", encoding="utf-8")
    fp.write(content_)
    fp.close()

    print(f"\nReplacement complete. Content saved to {in_4}.")