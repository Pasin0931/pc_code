# Name: Pasin Makcharoen # Student ID: 6810545794

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False


status = True

try:
    owner_n = input("Enter account owner: ")
    balance = float(input("Enter initial balance: "))
    
    print(f"Welcome, {owner_n}.")
except ValueError:
    status = False
    print("Invalid input")
    
commands = ["deposit", "withdraw", "balance", "exit"]
some_command = ["balance", "exit"]

if status == True:
    bank_ = BankAccount(owner_n, balance)
    
    while True:
        com_ = input("Enter command: ").strip().lower().split()
        
        if len(com_) > 2 or com_[0] not in commands or com_[0] == "":
            print("Invalid command")
            continue
        
        elif com_[0] in ("deposit", "withdraw"):
            if len(com_) != 2:
                print("Invalid command")
                continue
            
            elif com_[0] == "deposit":
                state_ = bank_.deposit(com_[1])
                if state_ == True:
                    print(f"Deposit successful. New balance: {bank_.get_balance()}")
                else:
                    print(f"Invalid deposit amount.")
                    
            elif com_[0] == "withdraw":
                state_ = bank_.withdraw(com_[1])
                if state_ == True:
                    print(f"Withdrawal successful. New balance: {bank_.get_balance():.2f}")
                else:
                    print(f"Insufficient funds or invalid amount.")
                    
        elif com_[0] in some_command:
            