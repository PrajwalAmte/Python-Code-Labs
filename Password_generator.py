import random

try:
    length = int(input("Enter the password length: "))
    
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_"
        
        if length > len(characters):
            print(f"Maximum password length is {len(characters)} characters.")
        else:
            password = "".join(random.sample(characters, length))
            print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")