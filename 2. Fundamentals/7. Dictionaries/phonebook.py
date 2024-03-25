phonebook = {}
search_count = 0

while True:
    contact = input().split("-")

    if contact[0].isdigit():
        search_count = int(contact[0])
        break

    name = contact[0]
    number = contact[1]

    if name not in phonebook.keys():
        phonebook[name] = ""
    phonebook[name] = number

for search in range(search_count):
    person_to_call = input()
    if person_to_call in phonebook.keys():
        print(f"{person_to_call} -> {phonebook[person_to_call]}")
    else:
        print(f"Contact {person_to_call} does not exist.")
