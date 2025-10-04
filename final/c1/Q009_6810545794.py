# Name: Pasin Makcharoen # Student ID: 6810545794

num_item = int(input("How many items in inventory? "))
print()

count = 1

db = {}
items = []

for i in range(num_item):
    print(f"Item {count}")
    while True:
        name = input("Enter name: ")
        if name.lower() not in items:
            break
        else:
            print("Invalid name, enter a different name")
    price = float(input("Enter price: "))
    quan = int(input("Enter quantity: "))

    db[f"item{count}"] = [name, price, quan]
    items.append(name.lower())

    count += 1
    print()

sub_t_all = []

print("Inventory Details:")
for key, value in db.items():
    sub_t = value[1] * value[2]
    sub_t_all.append(sub_t)

    print(f"{value[0]} - Price: {value[1]:.2f}, Quantity: {value[2]}, Subtotal: {sub_t:.2f}")

print()
print(f"Total inventory value: {sum(sub_t_all):.2f}")