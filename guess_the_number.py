import random

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess > secret_number:
            print("Your guess is too high. Guess again.")
        elif guess < secret_number:
            print("Your guess is too low. Guess again.")
        else:
            print("Congratulations! You guessed the number correctly!")

    except ValueError:
        print("Invalid input! Please enter a number only.")
