#This is an Hangman game
import random

#Below are some hangman text... To make it fun...lol
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Words that would be used in the game...You can add yours if you like, as many as posible
word_list = ["python", "market", "footbal", "monkey"]

#Randomly choosing a word from the word_list and assign it to a variable called "chosen_word".
chosen_word = random.choice(word_list)

#Initializing our display variable and puting some empty lines in it
display = []
for index in range(len(chosen_word)):
  display += "_"


#Some initaizations to make the game run smoothly
game_complete = False
lives = 7

#some greatings
print("Welcome to the Hangman game\n You have 7 trials to guess each letter in the word\n Have a fun experience!!!")

#Now the game implementation
while game_complete == False:
  print()
  print(display)

  #Getting a word from the user
  guess = input("Guess a letter in the word\n").lower()

  #Checking if the guessed letter is part of the chosen_word
  if guess in chosen_word:
    #Now we need to get the index of that word, so we first loop through the choosen_word
    for index in range(len(chosen_word)):
      #Now we get the particular position(index)
      if guess == chosen_word[index]:
        #Now we put the word in the right postion in the display list
        display[index] = chosen_word[index]

  #When the guessed letter is not in the choosen word
  else:
    #First remove a life
    lives -= 1
    #Tell the user the word is incorrect
    print(f"{guess} is a wrong letter")
    #Get it some hangman
    print(stages[lives])

  #This is to check if all spaces are filled up in the display list and end the game
  if "_" not in display:
    game_complete = True

  #Also a condition to end the game, out of lives
  if lives == 0:
    game_complete = True


#Now we are out of the while loop, now we need to know what ended the loop
if lives == 0:
  print("Ouch.....You ran out of trials\nGame over!")
else:
  print(f"Congratulations.....You have guessed the word correctly: {chosen_word.upper()}")
  print("You WIN!!!")