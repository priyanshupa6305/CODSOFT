import random

def display_rules():
    print("\n--- Game Rules ---")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock\n")

def play_game():
    user_score = 0
    computer_score = 0

    display_rules()

    while True:
        # Prompt user input
        print("\nYour options: rock, paper, scissors, reset, or exit")
        user_choice = input("Choose your move: ").lower()
        if user_choice == "exit":
            print("\nThanks for playing!")
            break
        elif user_choice == "reset":
            user_score, computer_score = 0, 0
            print("\nScores have been reset!")
            continue

        if user_choice not in ["rock", "paper", "scissors"]:
            print("\nInvalid choice. Please try again.")
            continue

        # Computer selection
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Game logic
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            user_score += 1
        else:
            result = "Computer wins!"
            computer_score += 1

        # Display result
        print(result)
        print(f"Current Score: You {user_score} - Computer {computer_score}")

        # Play again prompt
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

play_game()
