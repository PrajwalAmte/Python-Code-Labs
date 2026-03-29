import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "win"
    return "lose"

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors ---")
    print(f"Your Score: {user_score} | Computer Score: {computer_score}")
    
    user_choice = input("Enter choice (rock/paper/scissors) or 'quit' to exit: ").lower()
    
    if user_choice == 'quit':
        break
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == "win":
        print("You win this round!")
        user_score += 1
    elif result == "lose":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
