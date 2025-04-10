from tkinter import *
root = Tk()
mycanvas = Canvas(root)
mycanvas.pack()

mycanvas.create_rectangle( 100,100, 200, 200 , outline = "black")
mycanvas.create_oval( 100, 100, 200, 200, outline = "red")
mycanvas.create_arc( 100, 100, 200, 200, start= 0, extent = 90, outline = "blue")

root.mainloop( )
