from tkinter import *

root = Tk()

root.geometry("500x250")

myLabel = Label(root, text="Hello GitHub!")
myButton = Button(root, text="Click")

myLabel.pack(pady=30)
myButton.pack(pady=30)

root.mainloop()
