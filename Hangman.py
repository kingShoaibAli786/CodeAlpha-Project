import random

def hangman():
    words = ['python', 'programming', 'hangman', 'challenge', 'developer']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_'
        print('Word:', display_word)

        if display_word == word:
            print("Congratulations! You've guessed the word!")
            break

        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print('Correct!')
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f'Wrong! Attempts left: {attempts}')

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()