# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path
import math

def checking(file_name):
    if not Path(file_name).exists():
        print(f"Error: {file_name} not found.\n")
        return False
    return True

def p_summary(cir_, rec_, squ_, total_shapes_, total_area_, file_name=''):
    title_ = f"Report for {file_name}" if file_name else "Grand Total"
    all_shape_ = "Total shapes:" if not file_name else "Shapes:"
    over_ = "overall " if not file_name else ""
    print(f"--- {title_} ---")
    print(f"{all_shape_}")
    print(f"  circle: {cir_}")
    print(f"  rectangle: {rec_}")
    print(f"  square: {squ_}")
    print(f"Total {over_}shapes: {total_shapes_}")
    print(f"Total {over_}area: {total_area_:.2f}")
    print("-------------------")

grand_totals = {"circle": 0, "rectangle": 0, "square": 0, "amount": 0, "total": 0}

if not checking("index.txt"):
    pass
else:
    with open("index.txt", "r", encoding="utf-8") as f:
        file_list = [line.strip() for line in f.readlines()]

    if all(f == "" for f in file_list):
        print("Error: index.txt not found.")
    else:
        for file_name in file_list:
            if file_name == "":
                continue
            if not checking(file_name):
                continue

            print(f"Processing file: {file_name}")

            with open(file_name, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f.readlines()]

            counts = {"circle": 0, "rectangle": 0, "square": 0}
            file_total_area = 0
            file_total_shapes = 0

            for line in lines:
                line_str = line.strip()
                if line_str == "":
                    continue
                parts = line_str.split()
                try:
                    shape = parts[0]
                    if shape not in counts:
                        raise ValueError
                    if shape == "circle":
                        if len(parts) != 2:
                            raise ValueError
                        radius = float(parts[1])
                        area = math.pi * radius ** 2
                    elif shape == "rectangle":
                        if len(parts) != 3:
                            raise ValueError
                        width = float(parts[1])
                        height = float(parts[2])
                        area = width * height
                    elif shape == "square":
                        if len(parts) != 2:
                            raise ValueError
                        side = float(parts[1])
                        area = side ** 2

                    counts[shape] += 1
                    file_total_shapes += 1
                    file_total_area += area
                    grand_totals[shape] += 1
                    grand_totals["amount"] += 1
                    grand_totals["total"] += area

                except (ValueError, IndexError):
                    print(f"Error on line: {line}")

            p_summary(counts["circle"], counts["rectangle"], counts["square"],
                      file_total_shapes, file_total_area, file_name)
            print()

        p_summary(grand_totals["circle"], grand_totals["rectangle"], grand_totals["square"],
                  grand_totals["amount"], grand_totals["total"])

