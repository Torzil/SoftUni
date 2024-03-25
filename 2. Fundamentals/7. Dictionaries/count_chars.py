given_string = input().split()
chars_dict = {}

for word in given_string:
    for char in word:
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1

for key, value in chars_dict.items():
    print(f"{key} -> {value}")
