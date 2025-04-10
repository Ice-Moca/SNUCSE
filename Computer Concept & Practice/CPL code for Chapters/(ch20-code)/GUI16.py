from tkinter import *
root = Tk( )

var = StringVar()
mylabel = Label( root, textvariable = var, relief=RAISED )
var.set("Hey!? How are you doing?")
mylabel.pack( )

root.mainloop( )

top.mainloop( )
