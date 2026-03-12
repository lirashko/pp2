import re

s = input()

print(re.sub(r"([a-z])([A-Z])", r"\1 \2", s))