# a = "0g2e4t"
# print(a[-1])
# print(a[-3])
# print(a[-5])




# msg = input("Enter a message: ")
# for i in range(0, len(msg)):
#     print(f"Character {i+1} is {msg[i]}")




# msg = input("Enter a message: ")

# out = ""
# for i in range(0, len(msg), 2):
#     out = out+msg[i]
# print(out)

# out = ""
# for i in range(1, len(msg), 2):
#     out = out+msg[i]
# print(out)




# def display(msg):
#     space = ""
#     for i in msg:
#         print(space + i)
#         space+=" "

# msg = input("Enter a message: ")
# display(msg)




def vowel_nonVowel_counter(msg):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    non_vowel = 0

    for ch in msg:
        if ch == "a":
            a+=1

        elif ch == "e":
            e+=1

        elif ch == "i":
            i+=1

        elif ch == "o":
            o+=1

        elif ch == "u":
            u+=1

        else:
            non_vowel+=1

    return a, e, i, o, u, non_vowel

def display(a, e, i, o, u, non_vol):
    print(f"There are {a} a's.")
    print(f"There are {e} e's.")
    print(f"There are {i} i's.")
    print(f"There are {o} o's.")
    print(f"There are {u} u's.")
    print(f"There are {non_vol} non-vowels characters.")

msg = input("Enter a message: ").lower()
a, e, i, o, u, count = vowel_nonVowel_counter(msg)
display(a, e, i, o, u, count)