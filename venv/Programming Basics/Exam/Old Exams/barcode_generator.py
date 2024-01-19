barcode_range_start = input()
barcode_range_end = input()


# for barcode in range(barcode_range_start, barcode_range_end + 1):
#     barcode_is_odd = True
#     for index, digit in enumerate(str(barcode)):
#         digit = int(digit)
#         if digit % 2 == 0:
#             barcode_is_odd = False
#             break
#     if barcode_is_odd:
#         print(barcode, end=" ")

start_1 = int(barcode_range_start[0])
start_2 = int(barcode_range_start[1])
start_3 = int(barcode_range_start[2])
start_4 = int(barcode_range_start[3])

end_1 = int(barcode_range_end[0])
end_2 = int(barcode_range_end[1])
end_3 = int(barcode_range_end[2])
end_4 = int(barcode_range_end[3])

for number_1 in range(start_1, end_1 + 1):
    for number_2 in range(start_2, end_2 + 1):
        for number_3 in range(start_3, end_3 + 1):
            for number_4 in range(start_4, end_4 + 1):
                if number_1 % 2 != 0 and number_2 % 2 != 0 and number_3 % 2 != 0 and number_4 % 2 != 0:
                    print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
