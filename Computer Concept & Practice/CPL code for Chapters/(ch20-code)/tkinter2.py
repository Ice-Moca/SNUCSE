from tkinter import *

root = Tk()

mycanvas = Canvas(root)
mycanvas.pack( )

mycanvas.create_line( (10,10,10,100) )
mycanvas.create_line( (10,10,100,10) )
mycanvas.create_rectangle( 100,100,150,150 )
mycanvas.create_oval( 200,100,250,150 )


root.mainloop()
