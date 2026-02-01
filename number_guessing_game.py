import random

print("Welcome to the Number Guessing Game")

print("\nChoose Difficulty Level:")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")

while True:
    try:
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            max_number = 10
            max_attempts = 5
            break
        elif choice == 2:
            max_number = 50
            max_attempts = 7
            break
        elif choice == 3:
            max_number = 100
            max_attempts = 10
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    except ValueError:
        print("Please enter a valid number.")

# Generate random number
random_number = random.randint(1, max_number)
attempts = 0

print(f"\nI have selected a number between 1 and {max_number}.")
print(f"You have {max_attempts} attempts. Good luck!\n")

# Game loop
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > max_number:
            print(f"⚠️ Please enter a number between 1 and {max_number}.")
            continue

        if guess < random_number:
            print("Too Low!")
        elif guess > random_number:
            print("Too High!")
        else:
            print("Congratulations! You guessed the correct number!")
            print(f"Total attempts used: {attempts}")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")

# If attempts are over
if attempts == max_attempts and guess != random_number:
    print("\nGame Over!")
    print(f"The correct number was: {random_number}")
