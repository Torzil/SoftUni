full_string = input()
filtered_string = [x for x in full_string if x.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(filtered_string))
