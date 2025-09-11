floor3_rooms = {'4/4': 1, '4/5': 2, '5/1': 3, '5/2': 4, '5/3': 5}

classroom_floors = {key:value for key, value in floor3_rooms.items()}
print(classroom_floors)

class4_year_rooms = {key:"year4" for key, value in floor3_rooms.items() if key == "4/4" or key == "4/5"}
print(class4_year_rooms)

class4_year_rooms = {key:"year5" for key, value in floor3_rooms.items() if key == "5/1" or key == "5/2" or key == "5/3"}
print(class4_year_rooms)

left_wings = {value:key for key, value in floor3_rooms.items() if key == "4/4" or key == "4/5" or key == "5/1"}
print(left_wings)

right_wings = {value:key for key, value in floor3_rooms.items() if key == "5/2" or key == "5/3"}
print(right_wings)



# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# scores['Pat'] = 89

# scores2 = scores.copy()
# scores3 = scores.copy()

# scores2['Beth'] = 65
# scores3['Zoe'] = 63

# print(scores2)
# print(scores3)



