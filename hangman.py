import random

def hangman():
    words = ["python", "computer", "program", "developer", "coding"]

    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("================================")
    print("       WELCOME TO HANGMAN")
    print("================================")
    print("Guess the hidden word one letter at a time!")
    print("You have", max_attempts, "incorrect guesses allowed.")

    while incorrect_guesses < max_attempts:
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Incorrect guesses remaining:",
              max_attempts - incorrect_guesses)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            print("You won!")
            break

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    else:
        print("\nGame over! You have used all your attempts.")
        print("The correct word was:", word)


if __name__ == "__main__":
    hangman()