import re

s = input()
pattern = r"[ ,.]"

print(re.sub(pattern, ":", s))