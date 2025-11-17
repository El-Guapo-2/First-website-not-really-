def main():
    secret_word = "messerrocks"
    guessed_letters = []
    current_progress = ["_"] * len(secret_word)
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!\n")

    while incorrect_guesses < max_incorrect_guesses and "_" in current_progress:
        print("Your word: " + " ".join(current_progress))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    current_progress[index] = guess
        else:
            incorrect_guesses += 1
            print("Wrong guess!")
            print(f"Remaining guesses: {max_incorrect_guesses - incorrect_guesses}")

    if "_" not in current_progress:
        print("\nCongratulations! You guessed the word: " + secret_word)
    else:
        print("\nGame over! The word was: " + secret_word)

if __name__ == "__main__":
    main()