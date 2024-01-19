student_tickets = 0
standard_tickets = 0
kids_tickets = 0

movie_name = input()
while movie_name != "Finish":
    movie_seats = int(input())
    ticket_type = input()
    taken_seats = 0
    while ticket_type != "End":
        taken_seats += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        if taken_seats == movie_seats:
            break
        ticket_type = input()
    percent_taken_seats_current_movie = taken_seats / movie_seats * 100
    print(f"{movie_name} - {percent_taken_seats_current_movie:.2f}% full.")

    movie_name = input()

total_tickets = student_tickets + standard_tickets + kids_tickets
percent_student_tickets = student_tickets / total_tickets * 100
percent_standard_tickets = standard_tickets / total_tickets * 100
percent_kids_tickets = kids_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kids_tickets:.2f}% kids tickets.")
