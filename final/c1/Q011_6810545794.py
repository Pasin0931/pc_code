# Name: Pasin Makcharoen # Student ID: 6810545794

db = {}

while True:
    transaction = input("Enter transaction description (or 'done' to finish): ")

    if transaction.lower() == "done":
        break

    amount = float(input(f"Enter amount for {transaction}: "))

    if amount == 0:
        continue
    elif amount < 0:
        state= "-"
    else:
        state = "+"
    
    db[transaction] = [amount, state]

t_in = []
t_expense = []

print()
print("--- FINANCIAL REPORT ---")
print("Transactions:")

for key, value in db.items():
    if value[1] == "+":

        t_in.append(value[0])

        s1 = f"{value[1]} {key}"
        s2 = f"{value[0]:.2f}"
        print(f"{s1:<17}${s2:>8}")
    else:

        t_expense.append(value[0])

        s1 = f"{value[1]} {key}"
        s2 = f"{value[0]:.2f}"
        print(f"{s1:<17}${s2:>8}")

print("------------------------")

sum_in = f"{sum(t_in):.2f}"
sum_exp = f"{sum(t_expense):.2f}"

net_b = float(sum_in) + float(sum_exp)
net_b = f"{net_b:.2f}"

w1 = "Total Income:"
w2 = "Total Expenses:"
w3 = "Net Balance:"

print(f"{w1:<17}${sum_in:>8}")
print(f"{w2:<17}${sum_exp:>8}")
print(f"{w3:<17}${net_b:>8}")

print("------------------------")