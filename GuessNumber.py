import random

number = random.randint(1, 10)
guessed = False

for attempt in range(1, 4):
    try:
        guess = int(input(f"Attempt {attempt}/3 - Guess the number (1-10): "))
        if guess == number:
            print("Hurray!!")
            print(f"You guessed correctly! The number was {number}")
            guessed = True
            break
        elif guess < number:
            print("Too low, try again!")
        else:
            print("Too high, try again!")
    except ValueError:
        print("Please enter a valid number.")

if not guessed:
    print(f"Game over! The number was {number}")