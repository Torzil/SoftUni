word = input()
capitals_list = []

for index, letter in enumerate(word):
    if letter.isupper():
        capitals_list.append(index)

print(capitals_list)
