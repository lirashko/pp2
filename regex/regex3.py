import re

s = input()
pattern = r"[a-z]+_[a-z]+"

print(re.findall(pattern, s))