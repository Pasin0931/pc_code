# in_ = input("Input: ")

# print("Output:")

# in_ = list(in_)
# if in_[0] == in_[-1]:
#     print(True)
# else:
#     print(False)



# in_ = input("Input: ")

# res = 1
# print("Output:")

# while True:
#     for i in range(len(in_)):
#         res = res * int(in_[i])

#     if len(str(res)) == 1:
#         print(res)
#         break
#     else:
#         in_ = str(res)
#         res = 1



# in_ = input("Input: ")

# count = 0
# for i in range(0, len(in_) - 1):
#     if in_[i] == in_[i + 1]:
#         count += 1
#     else:
#         continue

# print("Output:")
# print(count)



# c = int(input("Input: "))
# r = c

# matrix = []
# for i in range(r):
#     row = input("").split()
#     matrix.append(row)

# print("Output: ", end="")

# result = []
# top, bottom, left, right = 0, r - 1, 0, c - 1

# while top <= bottom and left <= right:

#     for j in range(left, right + 1):
#         result.append(matrix[top][j])
#     top += 1

#     for i in range(top, bottom + 1):
#         result.append(matrix[i][right])
#     right -= 1

#     if top <= bottom:
#         for j in range(right, left - 1, -1):
#             result.append(matrix[bottom][j])
#         bottom -= 1

#     if left <= right:
#         for i in range(bottom, top - 1, -1):
#             result.append(matrix[i][left])
#         left += 1

# print(" ".join(result))



# in_ = input("Input: ").split()
# in_.sort()

# word = {}

# for i in range(len(in_)):
#     if in_[i] not in word:
#         word[in_[i]] = 1
#     else:
#         word[in_[i]] += 1

# print("Output:")
# for key, value in word.items():
#     print(key, value)



# usrs = {}

# while True:
#     in_ = input("").split()

#     if in_[0] == "end":
#         break

#     elif in_[0] == "add":
#         usrs[in_[1]] = in_[2]

#     elif in_[0] == "remove":
#         del usrs[in_[1]]

# usrs = dict(sorted(usrs.items()))

# print("Output:")
# for key, value in usrs.items():
#     print(f"{key}:{value}")



# num_student = int(input(""))

# grade_subjects = {}
# while True:
#     in_ = input("").split()

#     if in_[0] == "popitem":
#         if len(in_) == 2:
#             last_subject = list(list(grade_subjects.values())[-1])[-1]
            
#             del grade_subjects[in_[1]][last_subject]
#             print(grade_subjects)
        
#         elif len(in_) == 1:
#             last_student = list(grade_subjects.keys())[-1]
#             del grade_subjects[last_student]
#             break

#     elif in_[0] == "pop":
#         del grade_subjects[in_[1]][in_[2]]
        
#     else:
#         if len(grade_subjects) <= num_student:
#             student_subject = {}

#             subjects = [in_[i] for i in range(1, len(in_))]

#             for subject in subjects:
#                 this_subject, this_score = subject.split(":")

#                 this_score = int(this_score)

#                 student_subject[this_subject] = this_score

#             grade_subjects[in_[0]] = student_subject

#         else:
#             continue

# print("Output:")
# print(grade_subjects)



# num_student = int(input(""))

# count = 0
# grade_subjects = {}
# while count < num_student:
#     in_ = input("").split()

#     student_subject = {}

#     subjects = [in_[i] for i in range(1, len(in_))]

#     for subject in subjects:
#         this_subject, this_score = subject.split(":")

#         this_score = int(this_score)

#         student_subject[this_subject] = this_score

#     grade_subjects[in_[0]] = student_subject

#     count += 1

# # -------------------------------------------------------

# count_command = int(input(""))
# commands = []
# count = 0
# while count < count_command:
#     in_ = input("").split()

#     if in_[0] == "popitem":
#         if len(in_) == 2:
#             if in_[1] in grade_subjects and grade_subjects[in_[1]]:
#                 last_sub = list(grade_subjects[in_[1]])[-1]
#                 del grade_subjects[in_[1]][last_sub]

#         elif len(in_) == 1:
#             if grade_subjects:
#                 last_student = list(grade_subjects.keys())[-1]
#                 del grade_subjects[last_student]

#     elif in_[0] == "pop":
#         if in_[1] in grade_subjects:
#             if in_[2] in grade_subjects[in_[1]]:
#                 del grade_subjects[in_[1]][in_[2]]

#     elif in_[0] == "sum":
#         if in_[1] not in grade_subjects or not grade_subjects[in_[1]]:
#             commands.append(0)
#         else:
#             sum_ = 0
#             for subject_ in grade_subjects[in_[1]]:
#                 sum_ += grade_subjects[in_[1]][subject_]

#             commands.append(sum_)

#     elif in_[0] == "top":
#         if in_[1] not in grade_subjects or not grade_subjects[in_[1]]:
#             commands.append("None")
#         else:
#             max_score = max(grade_subjects[in_[1]].values())
#             top_subjects = [subj for subj, score in grade_subjects[in_[1]].items() if score == max_score]
#             commands.append(",".join(top_subjects))

#     elif in_[0] == "average":
#         temp = []
#         for name in grade_subjects:
#             if in_[1] in grade_subjects[name]:
#                 temp.append(grade_subjects[name][in_[1]])
        
#         if not temp:
#             avg = "0.00"
#         else:
#             avg = sum(temp) / len(temp)
#             avg = f"{avg:.2f}"

#         commands.append(avg)

#     count += 1

# # print("-------------------------")
# for i in commands:
#     print(i)
# print("Output:")
# print(grade_subjects)



# keys_ = input("Input keys: ").split()
# values_ = input("Input values: ").split()

# print("Output:")

# mapped = dict(zip(keys_, values_))

# for key, value in mapped.items():
#     print(f"{key}: {value}")



# items_ = input("Input items: ").split()
# weights_ = input("Input weights: ").split()
# scores_ = input("Input scores: ").split()

# weights_ = list(map(float, weights_))
# scores_ = list(map(float, scores_))

# temp = []
# for w, s in zip(weights_, scores_):
#     temp.append(w * s)

# avg = sum(temp)

# zipped = dict(zip(items_, list(zip(weights_, scores_))))

# print("Output:")
# print(zipped)
# print(f"Weighted Average: {avg:.2f}")



# keys_ = input("Input keys: ").split()
# values_ = input("Input values: ").split()

# dict_format = dict(zip(keys_, values_))
# reversed_dict = dict(reversed(dict_format.items()))

# print("Output:")
# print(reversed_dict)



keys_ = input("Input keys: ").split()
values_ = input("Input values: ").split()

replace = {}
dict_format = dict(zip(keys_, values_))
for key, value in dict_format.items():
    replace[value] = key

print("Output:")
print(replace)