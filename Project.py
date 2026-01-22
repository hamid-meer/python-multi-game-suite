import random

# -------- WORD SCRABBLE --------
def scrabble():
    print("\nWord Scrabble Game")

    word = "python"
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print("Scrambled word:", scrambled)
    answer = input("Guess the word: ")

    if answer == word:
        print("Correct!")
    else:
        print("Wrong! The word was:", word)

# -------- WORD GUESSER --------
def guesser():
    print("\nWord Guesser Game")

    word = "apple"
    guess = input("Guess the word: ")

    if guess == word:
        print("You guessed it right!")
    else:
        print("Wrong guess. The word was:", word)

# -------- PASSWORD FINDER --------
def password():
    print("\nPassword Finder")

    secret = "1234"
    guess = input("Enter the password: ")

    if guess == secret:
        print("Access granted")
    else:
        print("Access denied")

# -------- MAIN MENU --------
while True:
    print("\n--- Game Menu ---")
    print("1. Word Scrabble")
    print("2. Word Guesser")
    print("3. Password Finder")
    print("4. Exit")

    choice = input("Choose a game: ")

    if choice == "1":
        scrabble()
    elif choice == "2":
        guesser()
    elif choice == "3":
        password()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
