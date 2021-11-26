import turtle as t
import tkinter as tk
count = -1
window = tk.Tk()
entryvar = tk.StringVar(window)
word = "word"
guess = ""
guesslist = []
listlength = 0
guesscount = 0

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

    wrong = tk.Label(
        text = "You are wrong",
    )

    correct = tk.Label(
        text = "Correct",
    )
    
    window.update_idletasks()
    window.update()
    
    if listlength != len(guesslist):
        count+=1
        listlength +=1

        if count != -1:
            if len(guesslist[count-1]) == len(word):
                if guesslist[count-1] == word:
                    print("You win!")
                    correct.pack() 

                else:
                    print("Wrong guess")
                    guesscount += 1
                    wrong.pack() 

            elif guesslist[count-1] in word:
                print("Your guess is correct")
                correct.pack()
                window.update_idletasks()

            else:
                print("Wrong guess")
                guesscount += 1
                wrong.pack()
