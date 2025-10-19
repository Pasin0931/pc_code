# Name: Pasin Makcharoen # Student ID: 6810545794

all_opp = ["+", "-", "*", "/"]

while True:
    try:
        in_ = input("Enter expression: ")

        if in_ == "EXIT":
            break
        
        valid_ = True
        in_ = in_.split(" ")
        
        for i in range(len(in_)):
            if i % 2 == 0:
                if in_[i] in all_opp:
                    valid_ = False
                    print("Error: Invalid expression format.")
                    break
                else:
                    in_[i] = float(in_[i])
            
            elif i % 2 != 0:
                if in_[i] in all_opp:
                    try:
                        trying = in_[i+1]
                        continue
                    except IndexError:
                        valid_ = False
                        print("Error: Invalid expression format.")
                        break        
                else:
                    valid_ = False
                    print("Error: Invalid expression format.")
                    break

        if valid_:
            total_ = in_[0]

            try:

                for i in range(1, len(in_), 2):
                    if in_[i] == "+":
                        total_ += in_[i + 1]

                    elif in_[i] == "-":
                        total_ -= in_[i + 1]

                    elif in_[i] == "*":
                        total_ *= in_[i + 1]

                    elif in_[i] == "/":
                        total_ /= in_[i + 1]

                print(f"Result: {total_}")

            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

    except ValueError as e:
        e = str(e)
        e = e.replace("could not convert string to float: ", "")
        print(f"Error: Invalid number {e} in expression.")

print("Goodbye!")