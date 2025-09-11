# def update(x,y,z,w):
#     x = 5
#     y[1] = 3
#     z = "hi"
#     w = [i**2 for i in range(1,5)]  # List comprehension
#     print(x)
#     print(y)
#     print(z)
#     print(w)
#     return 5, [1, 4, 9, 16]

# a = 2
# b = [1, 2, 4, 8]
# c = 'hello'
# d = [100, 200, 300]
# e, f = update(a, b, c, d)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)



def update(x, y, z, v, w):
    v = 200
    x[2] = 20
    y.append(1000)
    z = [101, 201]
    w = 'bye'

_list1 = [1, 2, 3, 4, 5]
_list2 = [11, 12, 13, 14, 15]
_list3 = [21, 22, 23, 24, 25]
value = 100
text = 'hi'
update(_list1, _list2, _list3, value, text)
print(_list1)
print(_list2)
print(_list3)
print(value)
print(text)