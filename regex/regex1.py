import re

s = input()
pattern = r"ab*"

if re.fullmatch(pattern, s):
    print("Match")
else:
    print("No match")