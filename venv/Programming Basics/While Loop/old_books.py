needed_book = input()
checked_books = 0
book_is_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == needed_book:
        book_is_found = True
        break
    checked_books += 1
    current_book = input()

if book_is_found:
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")
