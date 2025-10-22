import random

# Predefined list of words
word_list = ['white', 'yellow', 'green', 'black', 'blue', 'grey']
chosen_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display setup
display = ['_' for _ in chosen_word]

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while incorrect_guesses < max_incorrect and '_' in display:
    print("Word: " + ' '.join(display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_incorrect - incorrect_guesses} tries left.\n")

# Game result
if '_' not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)