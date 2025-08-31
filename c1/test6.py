def ask_user():
    ticket = int(input("How many tickets?: "))
    zone = str(input("Which zone? (A/B/C/D): ")).upper()
    promotion = str(input("Do you have promotional code? ")).upper()
    if promotion == "N":
        return ticket, zone, None
    elif promotion == "Y":
        promo_code = str(input("Enter promo code: "))
        return ticket, zone, promo_code


def ticket_price(num, zone):
    if zone == "A":
        return num * 5800
    elif zone == "B":
        return num * 4500
    elif zone == "C":
        return num * 3500
    elif zone == "D":
        return num * 2000


def discount_tic(price, code):
    
    if code == "HAVEFUN45":
        dis_price = price - (price * (45 / 100))
        return dis_price
    elif code == "HAVEFUN20":
        dis_price = price - (price * (20 / 100))
        return dis_price
    elif code == "HAVEFUN15":
        dis_price = price - (price * (15 / 100))
        return dis_price
    else:
        return price

tic, zon, code = ask_user()
tic_price = ticket_price(tic, zon)
discount = discount_tic(tic_price, code)
print(f"Total price is {discount:.2f} Baht.")
