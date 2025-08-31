# def add_article(noun, proper):
#     noun = noun.lower()
#     if proper == "Y":
#         word = noun.title()
#         return f"The {word}"
#     elif proper == "N":
#         word = noun.title()
#         print(word[0])
#         if word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U":
#             return f"An {word}"
#         else:
#             return f"A {word}"

# noun = input('Input a noun: ')
# proper = input('Is this proper noun (Y/N)? ')
# print(add_article(noun, proper))

# --------------------------------------------


# s1 = "sample output"
# s2 = "PREDICTIVE MODEL"
# s3 = "PATTERN RECOGNITION"

# word1 = s1.upper()
# word2 = s2.lower().capitalize()
# word3 = s3.lower().title()

# print(word1)
# print(word2)
# print(word3)

# -----------------------------------------------

# def add_article(noun, proper):
#     noun = noun.lower()
#     if proper == "Y":
#         noun = noun.title()
#         return f"The {noun}"
#     elif proper == "N":
#         if noun[0] == "a" or noun[0] == "e" or noun[0] == "i" or noun[0] == "o" or noun[0] == "u":
#             return f"An {noun}"
#         else:
#             return f"A {noun}"


# noun = input('Input a noun: ')
# proper = input('Is this proper noun (Y/N)? ')
# print(add_article(noun, proper))

# -----------------------------------------------

def check_first_digit(word):
    first_char = word[0]
    
    if first_char.isdigit():
        return False
    else:
        return True


def check_each_char(word):
    for char in word:
       
        if not (char.isalnum() or char == "_"):
            return False

    return True

name = input("Enter a name: ")
if check_first_digit(name) == True and check_each_char(name) == True:
    print('This can be valid variable name.')
else:
    print('This cannot be valid variable name.')