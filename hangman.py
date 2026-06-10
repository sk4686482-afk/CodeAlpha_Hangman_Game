import random

# List of 5 predefined words as required
word_list = ["python", "coding", "laptop", "screen", "player"]

# Selecting a random word from the list
secret_word = random.choice(word_list)

# Initializing game variables
guessed_letters = []
attempts = 6

print("--- Welcome to the Hangman Game! ---")

# Main game loop
while attempts > 0:
    
    # Displaying the current state of the secret word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    print("\nWord to guess: ", display_word)
    print(f"Attempts left: {attempts}")
    
    # Check if the player has guessed all the letters
    if "_" not in display_word:
        print("\n🎉 Congratulations! You won! The correct word was:", secret_word)
        break

    # Taking input from the user
    guess = input("Guess a letter: ").lower()

    # Validating the user input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter!")
        continue

    # Checking if the letter is correct or incorrect
    if guess in guessed_letters:
        print("You have already guessed that letter!")
    elif guess in secret_word:
        print("Good job! Correct guess.")
        guessed_letters.append(guess)
    else:
        print("Wrong guess! You lost an attempt.")
        attempts -= 1

# Game over condition
if attempts == 0:
    print("\n😢 Game Over! You ran out of attempts.")
    print("The correct word was:", secret_word)