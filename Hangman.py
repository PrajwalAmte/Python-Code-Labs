import random

words = ["python", "hangman", "developer", "programming", "computer", "challenge"]
word = random.choice(words)
guessed = set()
attempts = 6
won = False

while attempts > 0:
    display = ''.join([letter if letter in guessed else '_' for letter in word])
    print(f"\nWord: {display}")
    print(f"Guessed letters: {', '.join(sorted(guessed)) if guessed else 'None'}")
    print(f"Attempts left: {attempts}")
    
    letter = input("Guess a letter: ").lower().strip()
    
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue
    
    if letter in guessed:
        print("You already guessed that letter!")
        continue
    
    guessed.add(letter)
    
    if letter in word:
        print("Correct!")
        if all(char in guessed for char in word):
            print(f"\nYou won! The word was: {word}")
            won = True
            break
    else:
        print("Wrong!")
        attempts -= 1

if not won:
    print(f"\nGame over! The word was: {word}")