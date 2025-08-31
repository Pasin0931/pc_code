# def usd_to_thb(usd):
#   return EXCHANGE_RATE * usd


# EXCHANGE_RATE = 34.09
# print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
# print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")

# EXCHANGE_RATE = 33.15
# print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
# print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")

# EXCHANGE_RATE = 35.26
# print(f"The current exchange rate is {EXCHANGE_RATE} THB per USD")
# print(f"You get {usd_to_thb(100):.2f} Thai Baht for 100 USD")

# -----------------

# def function3():
#     y = 20
#     # global x
#     print('function3-1', x, id(x))
#     x = 50
#     print('function3-2', x, id(x))

# #main
# x = 20
# print('main-1', x, id(x))
# function3()
# print('main-2', x, id(x))

# ------------------

# KILOMETERS_PER_MILE = 1.609

# def convert_miles_to_kms(value):
#   return KILOMETERS_PER_MILE * value

# mile = float(input("Input distance in miles: "))
# print(f"The converted distance is {convert_miles_to_kms(mile):.2f} kilometers.")

# ------------------

# def get_bmi(weight,height):
#     return weight/(height**2)

# print(get_bmi(63, 1.71))

# ------------------

def calculate_distance(v, a, t):
    return v*t + 0.5 * a * t **2

dist, velo, acc, duration = 0, 2, 0.5, 60
print(calculate_distance(t=duration, v=velo, a=acc))