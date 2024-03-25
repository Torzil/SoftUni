number_of_words = int(input())
synonym_dict = {}

for word in range(number_of_words):
    current_word = input()
    synonym = input()

    if current_word not in synonym_dict.keys():
        synonym_dict[current_word] = []
    synonym_dict[current_word].append(synonym)

for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")
