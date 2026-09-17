import random


def play_game():
    print("\n🎯 Number Guessing Game")
    print("I have selected a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number.")
            print(f"Number: {secret_number}")
            print(f"Attempts used: {attempts}")
            return

    print("\n😔 Game Over!")
    print(f"The correct number was: {secret_number}")
    print(f"Attempts used: {attempts}")


def main():
    while True:
        play_game()

        choice = input("\nDo you want to play another round? (y/n): ").lower()

        if choice != "y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
