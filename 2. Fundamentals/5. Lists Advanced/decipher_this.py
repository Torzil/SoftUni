def message_decipher(message):
    decrypted_message = []
    for word in message:
        word = list(word)
        character = ""
        for char in word:
            if char.isdigit():
                character += char
        word = [char for char in word if not char.isnumeric()]
        word.insert(0, chr(int(character)))
        word[1], word[-1] = word[-1], word[1]
        word = "".join(word)
        decrypted_message.append(word)
    return decrypted_message


encrypted_message = input().split()
print(" ".join(message_decipher(encrypted_message)))
