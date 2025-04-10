from tkinter import * 

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def draw(canvas, width, height) : 
    pistachio = rgbString(147, 197, 144)
    maroon    = rgbString(176, 48, 96)
    canvas.create_rectangle(0, 0, width/2, height/2, fill = pistachio)
    canvas.create_rectangle(width/2, height/2, width, height, fill=maroon)



def runDrawing(width=300, height=300) : 
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print( "bye!" )

runDrawing(400, 200)
