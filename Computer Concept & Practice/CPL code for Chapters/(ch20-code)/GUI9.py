from tkinter import *

lastx, lasty = 0, 0

def xy(event) :
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event) :
    global lastx, lasty
    canvas.create_line( (lastx, lasty, event.x, event.y) )
    lastx, lasty = event.x, event.y

root = Tk( )
canvas = Canvas(root)
canvas.pack( )

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

root.mainloop( )




