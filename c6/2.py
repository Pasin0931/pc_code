# in_ = input("Input: ")

# print("Output:")

# in_ = list(in_)
# if in_[0] == in_[-1]:
#     print(True)
# else:
#     print(False)



in_ = input("Input: ")

res = 1
print("Output:")

while True:
    for i in range(len(in_)):
        res = res * int(in_[i])

    if len(str(res)) == 1:
        print(res)
        break
    else:
        in_ = str(res)
        res = 1