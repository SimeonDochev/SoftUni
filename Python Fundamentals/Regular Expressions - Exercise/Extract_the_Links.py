import re

text = input()
pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
valid_sites_list = []

while text:
    valid_sites = [obj.group() for obj in re.finditer(pattern, text)]
    if valid_sites:
        valid_sites_list.extend(valid_sites)
    text = input()

print(*valid_sites_list, sep='\n')
