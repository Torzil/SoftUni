import random

print("Welcome to the SoftUni Number Guessing Game!")
print("I have randomly selected a number between 1 and 100, try to guess it! You have 5 attempts.")

random_number = random.randint(1, 100)

for attempt in range(1, 6):
    guess = int(input("Enter your guess: "))

    if guess == random_number:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
        break

    elif guess < random_number:
        print("Too low. Try again!")

    elif guess > random_number:
        print("Too high. Try again!")

else:
    print(f"You've run out of attempts! The correct number was {random_number}.")
