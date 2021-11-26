import tkinter as tk
word = "word"
count = 0
wrongcount = 0
length = len(word)
correctstring = "_"*length
rightcount = 0

def hangman(word,guess):

    length = len(word)
    correctstring = "_"*length

    if len(guess) == len(word):
        if guess == word:
            return ["Win", guess]

        else:
            return "Wrong"

    elif guess in word:
        print("correct")
        i = word.index(guess)
        correctstring = correctstring[:i] + guess + correctstring[i+1:]
        return ["Correct", correctstring]

    else:
        return "Wrong"
        

