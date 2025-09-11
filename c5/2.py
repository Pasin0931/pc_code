# def filter_dict(input_d):
#     return {key:value for key, value in input_d.items() if key % 100 == 0 or key == 0}
# this_dict = {100: 200, 250: 500, 300: 600, 700: 1400, 730: 1460, 850: 1700}
# print(filter_dict(this_dict))



text = input("Enter text: ")

word_list = {}
for letter in text:
    if letter == " ":
        continue
    elif letter not in word_list:
        word_list[letter] = 1
    else:
        word_list[letter] += 1

print(word_list)
for key, value in word_list.items():
    print(f"There are {value} {key}'s")