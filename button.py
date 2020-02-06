#Importing all functions of Tkinter
from tkinter import *
root = Tk()
#Defining function for callback
def callback():
    print("Click!")
button1 = Button(root, text="ONE", command=callback, bg="Red", fg="Green")
button2 = Button(root, text="TWO", command=callback, bg="Green", fg="Red")
#Placing buttons
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
