# in_ = int(input("Input: "))

# pow_2 = 1
# i = 1
# while pow_2 < in_:
#     pow_2 = 2 ** i
#     i += 1

# print("Output:")
# print(pow_2)



# in_ = input("Input: ")

# in_ = list(in_)
# in_.reverse()
# in_ = "".join(in_)
# in_ = int(in_)

# print("Output:")
# print(in_)



in_ = input("Input: ")

print("Output:")

if int(in_) == 0:
    print(0)

else:
    new_li = []
    in_ = list(in_)
    
    count = 0
    while count < len(in_):
        if in_[count] == "0":
            count += 1
            continue
        else:
            new_li.append(in_[count])
            count += 1
    
    print("".join(new_li))