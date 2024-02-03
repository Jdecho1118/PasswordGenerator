import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    character_sets = get_character_sets(use_lowercase, use_uppercase, use_digits, use_special)
    validate_password_length(length, character_sets)

    # Generate password with at least one character from each selected set
    password = generate_initial_chars(character_sets)

    # Fill the remaining length with random characters
    password += generate_random_chars(length, character_sets)

    # Shuffle the password to make it more random
    shuffled_password = shuffle_password(password)

    return shuffled_password

def get_character_sets(use_lowercase, use_uppercase, use_digits, use_special):
    character_sets = []

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_digits:
        character_sets.append(string.digits)

    if use_special:
        character_sets.append(string.punctuation)

    return character_sets

def validate_password_length(length, character_sets):
    if length < len(character_sets):
        raise ValueError("Password length must be at least the number of selected character sets")

def generate_initial_chars(character_sets):
    return ''.join(random.choice(char_set) for char_set in character_sets)

def generate_random_chars(length, character_sets):
    return ''.join(random.choice(''.join(character_sets)) for _ in range(length - len(character_sets)))

def shuffle_password(password):
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

# Improved user interface using f-strings
print("Welcome to the Password Generator!")
try:
    password_length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Invalid input. Using default password length of 12.")
    password_length = 12

# Simplified user input handling
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Example: Generate a password based on user input
generated_password = generate_password(password_length, use_lowercase, use_uppercase, use_digits, use_special)
print(f"Generated Password: {generated_password}")
