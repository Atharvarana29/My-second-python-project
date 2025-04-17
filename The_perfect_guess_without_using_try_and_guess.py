import random

def play_game():
    random_number = random.randint(1, 99)
    print(f"[DEBUG] Random number is: {random_number}")  # For testing
    
    attempts = 0
    history = []
    
    print("🎯 Guess the number between 1 and 99:")
    
    while True:
        user_input = input("Enter your guess number: ").strip()

        # Check if input is an integer using isdigit (and allow negative check)
        if not user_input.isdigit():
            print("❌ Invalid input. Please enter a valid number.")
            continue

        user_guess = int(user_input)

        # Check if number is in valid range
        if not 1 <= user_guess <= 99:
            print("⚠️ Please enter a number between 1 and 99.")
            continue

        # Valid guess
        attempts += 1
        history.append(user_guess)

        if user_guess > random_number:
            print("🔻 Enter a lower number please.")
        elif user_guess < random_number:
            print("🔺 Enter a higher number please.")
        else:
            print(f"🎉 Congrats! You have successfully guessed the correct number in {attempts} attempts.")
            print("🧠 Your guesses were:", history)
            break

if __name__ == "__main__":
    play_game()
