# def check_palindrome(msg):
#     msg = msg.lower()
#     message_list = []
#     reverse_msg = []

#     for i in msg:
#         message_list.append(i)
#         reverse_msg.append(i)

#     reverse_msg.reverse()

#     for i in range(0, len(message_list)):
#         if message_list[i] != reverse_msg[i]:
#             return False
#         elif message_list[i] == reverse_msg[i]:
#             continue
    
#     return True

# def display(msg, state):
#     if state == True:
#         print(f"{msg} is palindrome")
#     else:
#         print(f"{msg} is not palindrome")


# msg = input("Enter word: ")
# state = check_palindrome(msg)
# display(msg, state)




def decode(msg):
    list_msg = []

    for i in msg:
        list_msg.append(i)
    
    list_msg.pop(-1)
    list_msg.pop(-1)
    list_msg.reverse()

    print("The decoded message is:")

    for i in range(0, len(list_msg)):
        if list_msg[i] == "z":
            list_msg[i] = "s"
            print(list_msg[i], end ="")

        elif list_msg[i] == "e":
            list_msg[i] = "a"
            print(list_msg[i], end ="")

        elif list_msg[i] == "o":
            list_msg[i] = "e"
            print(list_msg[i], end ="")
        
        else:
            print(list_msg[i], end ="")


msg = input("Enter a decoded message: ").lower()
decode(msg)