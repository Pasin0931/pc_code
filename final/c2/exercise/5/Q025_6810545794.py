# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

state = True

file_name = "story.txt"
content_ = open(file_name, mode="r", encoding="utf-8")
content_ = content_.read()
# print(content_)

words_content = content_.split()
# print(words_content)

fulstop_loc = []

for i in range(len(words_content)):
    if "." in words_content[i]:
        fulstop_loc.append(i)

for word_here in range(len(words_content)):
    word = ""
    for letter in words_content[word_here]:
        if letter != ".":
            word += letter
    words_content[word_here] = word
    
# print(words_content)

in_1 = input("Enter the input filename: ")
if in_1 == file_name:
    in_2 = input("Enter the word to find: ")
    if in_2 in words_content:
        in_3 = input("Enter the replacement word: ")
        in_4 = input("Enter the output filename: ")
    else:
        state = False
        print(f"Error: Input word \'{in_2}\' not found.")
else:
    state = False
    print(f"Error: Input file \'{in_1}\' not found.")

if state == True:
    index = 0
    for i in range(len(words_content)):
        if words_content[i] == in_2:
            words_content[i] = in_3
            
    for i in fulstop_loc:
        words_content[i] = words_content[i] + "."
            
    joined_word = " ".join(words_content)
    # print(joined_word)
    
    this_path = Path.cwd() / f"{in_4}"
    fp = open(this_path, mode="w", encoding="utf-8")
    fp.write(joined_word)
    fp.close()

    print(f"\nReplacement complete. Content saved to {in_4}.")