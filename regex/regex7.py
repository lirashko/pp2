import re

s = input()

result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)

print(result)