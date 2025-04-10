# label and button

from tkinter import *
root = Tk( )

mylabel = Label(root, text= "Hello, label widget")
mylabel.pack( )

mybutton = Button(root, text= "Press me! Button widget")
mybutton.pack( )

root.mainloop( )


