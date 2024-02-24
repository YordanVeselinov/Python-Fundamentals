import re
number_of_barcodes = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for current_barcode in range(number_of_barcodes):
    barcode = input()
    matches = re.findall(pattern, barcode)
    if not matches:
        print("Invalid barcode")
    else:
        number = "".join(re.findall("\d", barcode))
        if not number:
            number = "00"
        print(f"Product group: {number}")