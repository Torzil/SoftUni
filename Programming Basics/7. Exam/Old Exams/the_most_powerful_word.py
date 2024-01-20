most_powerful_word = ""
most_powerful_word_points = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

current_word = input()
while current_word != "End of words":
    current_word_points = 0
    word_starts_with_vowel = False
    for letter in current_word:
        letter_value = ord(letter)
        current_word_points += letter_value
    first_letter = current_word[0]
    if first_letter.lower() in vowels:
        word_starts_with_vowel = True
    if word_starts_with_vowel:
        current_word_points *= len(current_word)
    else:
        current_word_points //= len(current_word)
    if current_word_points > most_powerful_word_points:
        most_powerful_word = current_word
        most_powerful_word_points = current_word_points
    current_word = input()

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_points}")
