import random

def number_guesser():
    number_to_guess = random.randint(1, 10)
    tries = 3

    print("🎯 Welcome to Number Guesser!")
    print("Guess the number between 1 and 10.")

    while tries > 0:
        guess = int(input("Your guess: "))
        if guess == number_to_guess:
            print("🎉 Correct! You win!")
            return
        else:
            tries -= 1
            print("❌ Wrong! Tries left:", tries)

    print("😢 Out of tries. The number was:", number_to_guess)

number_guesser()
