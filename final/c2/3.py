from pathlib import Path

tmp = Path.cwd() / "A" / "001.txt"

# print(tmp)

fp = open(tmp, "w")
fp.write("DUWGUDVWAUDVUWAGYU")
# fp.write("NIGGA 2")
fp.close()

# for i in range()