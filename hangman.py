import turtle as t
import tkinter as tk
from typing import Counter
count = -1
window = tk.Tk()
entryvar = tk.StringVar(window)
word = "word"
guess = ""
guesslist = ['',]
listlength = 0

def submit():
        global guess
        guess = entryvar.get()
        entryvar.set("")
        guesslist.append(guess)

while True:
    entermsg = tk.Label(
        width = 100,
        height = 50,
    )

    entrylabel = tk.Label(
        text = "Enter your guess",
        width = 20,
        height = 5,
    )

    submitbtn = tk.Button(window, text = 'Submit', command = submit)
    entry = tk.Entry(window, textvariable = entryvar)

    entrylabel.pack()
    entry.pack()
    submitbtn.pack()
    entermsg.pack()

    window.update()
    window.update_idletasks()

    wronglabel = tk.Label(
        text = "You are wrong",
        width = 10,
        height = 5,
    )

    congrat = tk.Label(
        text = "You win!",
        width = 10,
        height = 5,
    )
    
    
    if listlength != len(guesslist):
        if len(guesslist[count]) == len(word):
            if guesslist[count] == word:
                print("You win!")
                congrat.pack() #DOESNT WORK WHY

            else:
                print("Wrong guess")
                wronglabel.pack() #DOESNT WORK WHY

        elif guesslist[count] in word:
            print("Your guess is correct")

        else:
            print("Wrong")
            wronglabel.pack()


        count+=1
        listlength +=1
        
        print(count)
        print(guess)
        print(guesslist)
        
    











