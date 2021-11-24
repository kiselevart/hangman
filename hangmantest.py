import tkinter as tk
window = tk.Tk()
entryvar = tk.StringVar(window)
word = "word"
global guess
guess = ""
guesslist = []

def submit():
    global guess
    guess = entryvar.get()
    entryvar.set("")
    guesslist.append(guess)
    

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

window.mainloop()

print(guesslist)