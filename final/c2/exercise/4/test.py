from pathlib import Path

pth = "scores.txt"
store = []
total = 0
with open(Path(pth),"r", encoding="utf-8") as f:
    for lines in f:
        name,score = lines.strip().split(",")
        store.append([name,score])

    for i in store:
        total += float(i[1])
    average = total / len(store)
    highest = max(store, key=lambda d: d[1])

    print("--- Score Analysis ---")
    print(f"Class Average: {average:.2f}")
    print(f"Highest Score: {highest[0]} with {highest[1]} points.")