from tkinter import *

root = Tk()

mycanvas = Canvas(root)
mycanvas.pack( )

mycanvas.create_line( (10,10,10,100) )
mycanvas.create_line( (10,10,100,10) )
mycanvas.create_rectangle( 100,100,150,150 )
mycanvas.create_oval( 200,100,250,150 )

mycanvas.create_arc( 200,200,300,300 )
mycanvas.create_polygon( 280,150,280,100,350,150,360,100,380,250 )
mycanvas.create_text( 50,200, text="canvas")

root.mainloop()

