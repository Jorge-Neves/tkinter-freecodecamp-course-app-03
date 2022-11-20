from tkinter import *

root = Tk()

root.geometry("500x250")

my_text = "Updated Text!"


# function define for
# updating the my_label
# widget content
def update_text():
    # use global variable
    global my_text

    # configure
    myLabel.config(text=my_text)


# create a button widget and attached
# with counter function
myButton = Button(root, text="Click", command=update_text)

# create a Label widget
# Initial Label widget content
myLabel = Label(root, text="Hello GitHub")


myLabel.pack(pady=20)
myButton.pack(pady=20)

root.mainloop()
