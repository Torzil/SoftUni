import re

number_of_barcodes = int(input())

regex1 = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
regex2 = r"\d"

for _ in range(number_of_barcodes):
    barcode = input()
    match = re.findall(regex1, barcode)
    if match:
        match2 = re.findall(regex2, match[0])
        if match2:
            code_group = "".join(match2)
        else:
            code_group = "00"
        print(f"Product group: {code_group}")
    else:
        print("Invalid barcode")
