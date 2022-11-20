from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("500x250")

labelContent = "Hello GitHub!"

myLabel = Label(root, text=labelContent)


def change_text():
    myLabel.config(text="Updated Text!")
    myButton.config(state=DISABLED)


myButton = Button(root, text="Click", command=change_text)
myLabel.pack(pady=30)
myButton.pack(pady=30)


root.mainloop()
