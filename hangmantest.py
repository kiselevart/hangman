from hangmancmd import hangman
import tkinter as tk
guesslist = []

word = "word"
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entryvar = tk.StringVar(root)
entry1 = tk.Entry(root, textvariable = entryvar)
entry1.pack()

canvas1.create_window(200, 140, window=entry1)
canvas1.pack()

def getguess():
    guess = entryvar.get()
    entryvar.set("")
    guesslist.append(guess)


    guessstring = ""
    for x in range(len(guesslist)):
        guessstring += guesslist[x]


    gamestore = hangman(word,guessstring)
    guesstype = gamestore[0]
    wordtype = gamestore[1]
    print(guesstype)

    if guesstype != "Win":
        label1 = tk.Label(root, text= guesstype)
        label2 = tk.Label(root, text= wordtype)
        canvas1.create_window(200, 230, window=label1)
        canvas1.create_window(200, 250, window=label2)   

    else:
        label1 = tk.Label(root, text= "You win")
        canvas1.create_window(200, 230, window=label1)
    

button1 = tk.Button(text='Guess', command=getguess)
button1.pack()
canvas1.create_window(200, 180, window=button1)
canvas1.pack()
canvas1.delete(all)

root.mainloop()