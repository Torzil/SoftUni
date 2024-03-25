words_list = input().split()
words_dict = {}

for word in words_list:
    word = word.lower()
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1

for word, occurrences in words_dict.items():
    if occurrences % 2 != 0:
        print(word, end=" ")
