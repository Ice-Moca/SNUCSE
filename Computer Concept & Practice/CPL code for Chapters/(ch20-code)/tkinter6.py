from tkinter import * 

def draw(canvas, width, height) : 
    canvas.create_rectangle( 0,0,150,150, fill = "yellow" )


def runDrawing(width=300, height=300) : 
    root = Tk( )
    canvas = Canvas(root, width=width, height=height)
    canvas.pack( )
    draw(canvas, width, height)
    root.mainloop( )
    print( "bye!" )

runDrawing(400, 200)




