import string
import random

def get_valid_length():
    """Prompts the user for a valid password length."""
    while True:
        try:
            length = int(input("Enter password length: "))
            if length > 0:
                return length
            else:
                print("Password length must be greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_character_set():
    """Prompts the user to select character categories for the password."""
    character_list = ""
    selected_sets = []

    print("\nChoose character set(s) for your password:")
    print("1. Digits (0-9)")
    print("2. Letters (A-Z, a-z)")
    print("3. Special characters (!@#$%^&*)")
    print("4. Exit & Generate Password")

    while True:
        try:
            choice = int(input("Pick a number (1-4): "))
            if choice == 1:
                character_list += string.digits
                selected_sets.append(string.digits)
                print("Digits added.")
            elif choice == 2:
                character_list += string.ascii_letters
                selected_sets.append(string.ascii_letters)
                print("Letters added.")
            elif choice == 3:
                character_list += string.punctuation
                selected_sets.append(string.punctuation)
                print("Special characters added.")
            elif choice == 4:
                if character_list:
                    return character_list, selected_sets
                else:
                    print("You must select at least one character set!")
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def generate_password(length, character_list, selected_sets):
    """Generates a secure password ensuring inclusion of all selected character types."""
    password = [random.choice(char_set) for char_set in selected_sets]
    remaining_chars = [random.choice(character_list) for _ in range(length - len(password))]
    
    password.extend(remaining_chars)
    random.shuffle(password)  # Ensures randomness of characters
    return "".join(password)

def main():
    print("\n===== Secure Password Generator =====")
    
    length = get_valid_length()
    character_list, selected_sets = get_character_set()
    password = generate_password(length, character_list, selected_sets)

    print("\nGenerated Secure Password:", password)
    print("=====================================")

if __name__ == "__main__":
    main()
