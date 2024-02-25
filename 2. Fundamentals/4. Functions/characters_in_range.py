def ascii_range_interpreter(range_start, range_end):
    chars_list = []
    characters = ""
    for char in range(range_start + 1, range_end):
        chars_list.append(chr(char))
        characters = " ".join(chars_list)
    return characters


start_char = ord(input())
end_char = ord(input())

print(ascii_range_interpreter(start_char, end_char))
