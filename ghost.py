"""
GHOST
"""

import random

word_pool = []
my_guess = ""
guess_count = 0

# open the word pool text file
f = open("word_pool.txt", "r")

# add each word from the text file to the word pool list
for word in f:
  word_pool.append(word)

# shuffle the words in the word pool to avoid easy repitition
random.shuffle(word_pool)

# pick a random word from the word pool
word = random.choice(word_pool)

##### TEST WORD POOL FILE #####
"""
print(word_pool)
print("List length =",len(word_pool))
print("Mystery word =",word)
print("word length =",len(word))
"""

##### FUNCTIONS #####

def add_word(w):
  with open('word_pool.txt', 'a') as adding_new_word:
    adding_new_word.write(w)
    adding_new_word.write("\n")
    adding_new_word.close()

def check_word(g):
  deduped = []

  # open the word pool file as read only (default)
  f = open("word_pool.txt")
  
  # add words from the text file to the list ONLY if unique
  for word in f:
    deduped.append(word)
  if g+"\n" in deduped:
    pass
  else:
    add_word(g)

def validate(g):
  # break the guess string into a set
  letters = set(g)

  # ensure the set is exactly 5 letters long
  if len(letters) == 5:
    for char in letters:
      if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return 0
    return 1
  else:
    return 0


def guess():
  return input("Please enter your guess: ").upper()


def count(g, w):
  counter = 0
  for char in g:
    if char in w:
      counter += 1
  return counter

##### GAME PLAY #####

print("Welcome to GHOST\n")
print("OBJECTIVE & RULES:")
print("The game's objective is to guess the mystery word")
print("To guess, enter a 5 letter word with no repeating letters")
print("Good luck\n")

while my_guess != word:

  my_guess = guess()

  # validate an allowed word
  valid = validate(my_guess)

  # continue game if valid word was guessed
  if valid == 1:

    # increment the number of guesses by 1
    guess_count += 1

    # add each guess to the word pool
    check_word(my_guess)

    # Determine how many letters in the guess were in the word
    score = count(my_guess, word)

    if my_guess+"\n" == word:
      print("You Win! The word was",my_guess,"and it only took you",guess_count,"guesses")
      my_guess = word
    else:
      print("Your guess has",score,"letters in common with the secret word\n")

  else:
    print("Invalid guess.")
    print("Remember, each letter in the word must be unique")
    print("Use only letters (no numbers or special characters) and the word must be five letters long.\n")




