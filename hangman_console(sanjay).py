import random

# 5 predefined words as specified
WORDS = ["apple", "table", "robot", "music", "plant"]
MAX_GUESSES = 6

def display_word(word, guessed_letters):
    """Display word with underscores for unguessed letters"""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main():
    print("=" * 50)
    print("🎯 WELCOME TO HANGMAN GAME")
    print("=" * 50)
    
    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    while True:
        print("\n" + "=" * 30)
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {' '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {MAX_GUESSES - incorrect_guesses}")
        print("=" * 30)
        
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabetic character (A-Z).")
            continue
            
        if guess in guessed_letters:
            print("❌ You already guessed that letter.")
            continue

        # Process the guess
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "🎉" * 20)
            print(f"🎉 CONGRATULATIONS! You guessed the word: {word}")
            print("🎉" * 20)
            break
            
        # Check lose condition
        if incorrect_guesses >= MAX_GUESSES:
            print("\n" + "💀" * 20)
            print(f"💀 GAME OVER! The word was: {word}")
            print("💀" * 20)
            break

    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again == 'y':
        print("\n" + "🔄" * 20)
        print("🔄 Starting new game...")
        print("🔄" * 20)
        main()
    else:
        print("\n👋 Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main() 