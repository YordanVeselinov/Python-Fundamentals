# year = int(input())
# year_is_special = True
#
# while year_is_special:
#     year += 1
#     year_as_string = str(year)
#     year_is_special = False
#     for digit in year_as_string:
#         if year_as_string.count(digit) != 1:
#             year_is_special = True
#             break
# print(year)

year = int(input())
year += 1
while True:
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        break
    year += 1