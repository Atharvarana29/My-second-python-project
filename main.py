import random

RandomNumber = random.randint(1, 99)
print(f"[DEBUG] Random number is: {RandomNumber}")  # For testing

attempts = 0
history = []

print("🎯 Guess the number between 1 and 99:")

while True:
    try:
        UserInput = int(input("Enter your guess number: "))

        # Check if input is in the valid range
        if not 1 <= UserInput <= 99:
            print("⚠️ Please enter a number between 1 and 99.")
            continue

        # Valid input; process the guess
        attempts += 1
        history.append(UserInput)

        if UserInput > RandomNumber:
            print("🔻 Enter a lower number please.")
        elif UserInput < RandomNumber:
            print("🔺 Enter a higher number please.")
        else:
            print(f"🎉 Congrats! You have successfully guessed the correct number in {attempts} attempts.")
            print("🧠 Your guesses were:", history)
            break

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
