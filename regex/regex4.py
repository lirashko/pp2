import re

s = input()
pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, s))