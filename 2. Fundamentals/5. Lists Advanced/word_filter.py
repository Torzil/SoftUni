original_words = input().split()
filtered_words = [word for word in original_words if len(word) % 2 == 0]
print("\n".join(filtered_words))
