from tkinter import *

root = Tk()

root.geometry("300x250")

counter = 0
textContent = 'state' + " " + str(counter)


def update_text():
    global counter
    global textContent
    counter = counter + 1
    textContent = "updated state" + " " + str(counter)
    myLabel.config(text=textContent)


myLabel = Label(root, text=textContent)
myButton = Button(root, text="click", command=update_text)

myLabel.pack(pady=20)
myButton.pack(pady=20)

root.mainloop()