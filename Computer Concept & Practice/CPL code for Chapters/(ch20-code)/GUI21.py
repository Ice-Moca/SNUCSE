from tkinter import *
from tkinter import *

colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

for c in colours:
    lab = Label( text = c,  relief=RIDGE,     width=15)
    lab.pack( )
    ent = Entry( bg = c,   relief=SUNKEN,  width=10)
    ent.pack( )

mainloop( )




