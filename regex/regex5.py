import re

s = input()
pattern = r"a.*b"

if re.fullmatch(pattern, s):
    print("Match")
else:
    print("No match")