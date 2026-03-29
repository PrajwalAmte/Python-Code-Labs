import random

while True:
    print("\n--- Dice Roller ---")
    print("1. Roll the dice")
    print("2. Exit")
    
    choice = int(input("Choose an option (1-2): "))
    
    if choice == 1:
        roll = random.randint(1, 6)
        print(f"Dice rolled: {roll}")
    elif choice == 2:
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please try again.")