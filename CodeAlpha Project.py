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


class Stock:
    def __init__(self, symbol, shares, purchase_price):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price

    def __str__(self):
        return f"{self.symbol} - {self.shares} shares at ${self.purchase_price:.2f} each"

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, symbol, shares, purchase_price):
        stock = Stock(symbol.upper(), shares, purchase_price)
        self.stocks.append(stock)
        print(f"Added {shares} shares of {symbol.upper()} at ${purchase_price:.2f} each.")

    def show_portfolio(self):
        print("\nYour Portfolio:")
        if not self.stocks:
            print("No stocks in portfolio.")
            return
        for stock in self.stocks:
            print(stock)

if __name__ == "__main__":
    portfolio = Portfolio()

    while True:
        print("\n1. Add Stock")
        print("2. Show Portfolio")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price per share: "))
            portfolio.add_stock(symbol, shares, purchase_price)

        elif choice == '2':
            portfolio.show_portfolio()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


def chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great!")
        elif "name" in user_input:
            print("Chatbot: I'm a simple chatbot made with Python.")
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()

