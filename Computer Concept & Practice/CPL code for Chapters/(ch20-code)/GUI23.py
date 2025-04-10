from tkinter import *

colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

r = 0
for c in colours:
     lab = Label( text=c,  relief=RIDGE,    width=15)
     lab.grid(row=r , column=0)
     ent = Entry( bg=c,    relief=SUNKEN, width=10)
     ent.grid(row=r , column=1)
     r = r + 1

mainloop( )




