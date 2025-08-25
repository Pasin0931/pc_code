# TV_PRICE = 3000
# AUDIO_PRICE = 1500

# def read_amounts():
#     numTv = int(input("Number of TVs: "))
#     numAud = int(input("Number of audio systems: "))
#     return numTv, numAud

# def compute_total(totalTv = 0, totalAud = 0):
#     total_tv_price = totalTv * TV_PRICE
#     total_aud_price = totalAud * AUDIO_PRICE
#     total_price = total_tv_price + total_aud_price
#     return total_price

# def get_output_str(price = 0):
#     return f'Your total amount is {price:.2f} Baht.'


# tvs, auds = read_amounts()
# total = compute_total(tvs, auds)
# output_str = get_output_str(total)
# print(output_str)

# --------------------------------------

# def read_weight_height():
#     wei = float(input("Please enter your weight (kg): "))
#     hei = float(input("Please enter your height (cm): "))
#     return wei, hei

# def get_bmi(weight,height):
#     return weight/((height*0.01)**2)

# yourWeight, yourHeight = read_weight_height()
# bmi = get_bmi(height=yourHeight, weight=yourWeight)
# print(f"Your BMI: {bmi:.2f}")

# --------------------------------------

FIVEHUNDRED = 500
HUNDRED = 100
TWENTY = 20

def read_all_inputs():
    name = str(input("Input your name: "))
    charge = float(input("Input your charge: "))
    payment = float(input("Input your payment: "))
    return name, charge, payment

def calculate_change(charge, payment):
    return payment - charge

def find_change_in_bills(value):
    remain = value
    b500 = 0
    b100 = 0
    b20 = 0
    coins = 0
    while True:
        if remain >= FIVEHUNDRED:
            b500 = remain // FIVEHUNDRED
            remain = remain - (FIVEHUNDRED * b500)
        elif FIVEHUNDRED > remain >= HUNDRED:
            b100 = remain // HUNDRED
            remain = remain - (HUNDRED * b100)
        elif HUNDRED > remain >= TWENTY:
            b20 = remain // TWENTY
            remain = remain - (TWENTY * b20)
        elif TWENTY > remain:
            coins = remain
            break
    return b500, b100, b20, coins

def show_change(name, change, b500, b100, b20, coins):
    print(f"Thank you, {name}, for your payment.")
    print(f"As for change, you receive {change} Baht.")
    print(f"You receive {int(b500)} 500-Baht bills, {int(b100)} 100-Baht bills, {int(b20)} 20-Baht bills, and {coins:.2f} Baht change in coins.")

name, charge, payment = read_all_inputs()
totalCharge = calculate_change(charge, payment)
b500, b100, b20, coins = find_change_in_bills(totalCharge)
show_change(name, charge, b500, b100, b20, coins)