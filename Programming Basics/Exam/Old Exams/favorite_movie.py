number_of_movies = 0
best_score = 0
best_movie = ""
movie_limit_is_reached = False

movie_name = input()
while movie_name != "STOP":
    movie_score = 0
    for letter in movie_name:
        letter_score = ord(letter)
        if letter.isupper():
            letter_score -= len(movie_name)
        elif letter.islower():
            letter_score -= 2 * len(movie_name)
        movie_score += letter_score
    if movie_score > best_score:
        best_movie = movie_name
        best_score = movie_score
    number_of_movies += 1
    if number_of_movies == 7:
        movie_limit_is_reached = True
        break
    movie_name = input()

if movie_limit_is_reached:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")
