import re

pattern = r"@#+(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

n = int(input())

for _ in range(n):
    text = input()
    match = re.match(pattern, text)
    if not match:
        print("Invalid barcode")
    else:
        matches = re.finditer(pattern, text)
        for obj in matches:
            barcode = obj.group('barcode')
            prod_group = ""
            for char in barcode:
                if char.isdigit():
                    prod_group += char
            if prod_group:
                print(f"Product group: {prod_group}")
            else:
                print(f"Product group: 00")
