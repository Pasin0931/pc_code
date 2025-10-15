from pathlib import Path

in_ = input("Enter your name: ")

sel_path = Path.cwd() / "greeting.txt"
fp = open(sel_path, "w")
fp.write(f"Hello, {in_}! Welcome to file handling.")
fp.close()

print("Greeting saved to greeting.txt")