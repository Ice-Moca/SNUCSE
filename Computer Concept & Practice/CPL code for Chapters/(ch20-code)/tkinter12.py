from tkinter import Tk, Canvas

def runDrawing(width=300, height=300) : 
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack( )
    draw(canvas, width, height)
    root.mainloop()
    
def draw(canvas, width, height) : 
    canvas.create_oval( (50,50), (250,150), fill = 'yellow')
    canvas.create_polygon([(50,30),(150,50),(250,30),(150,10)] , fill= 'green')


runDrawing(400, 200)

