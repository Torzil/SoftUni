# year = int(input())
#
# while True:
#     year += 1
#     year_is_happy = True
#     year_as_string = str(year)
#     digits_collection = ""
#     for digit in year_as_string:
#         if digit in digits_collection:
#             year_is_happy = False
#             break
#         digits_collection += digit
#     if year_is_happy:
#         print(year)
#         break

year = int(input())

while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        print(year)
        break
