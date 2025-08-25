def read_vector(tInput):
    print(tInput)
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))
    return x, y

def convert_vector_to_str(x, y):
    res = f"[{x:.2f}, {y:.2f}]"
    return res

def add(ax=0, ay=0, bx=0, by=0):
    x = ax + bx
    y = ay + by
    return x, y

def subtract(ax=0, ay=0, bx=0, by=0):
    x = ax - bx
    y = ay - by
    return x, y

def calculate(ax, ay, bx, by, choice="+"):
    if choice == "+":
       cx,cy = add(ax,ay,bx,by)          # Call function add
    elif choice == "-":
       cx,cy = subtract(ax,ay,bx,by)     # Call function subtract
    return cx, cy

    
ax, ay = read_vector("For vector A")
bx, by = read_vector("For vector B")
choice = str(input("What to do with vectors? "))
cx, cy = calculate(ax, ay, bx, by, choice)
a = convert_vector_to_str(ax, ay)
b = convert_vector_to_str(bx, by)
c = convert_vector_to_str(cx, cy)
print(f"{a} {choice} {b} = {c}")