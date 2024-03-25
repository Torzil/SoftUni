chars_list = input().split(", ")
chars_dict = {key: ord(key) for key in chars_list}

print(chars_dict)
