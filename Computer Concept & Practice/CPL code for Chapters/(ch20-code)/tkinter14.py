from tkinter import Tk, Canvas

def runDrawing(width=300, height=300) : 
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack( )
    draw(canvas, width, height)
    root.mainloop()
    
def drawBelgianFlag(canvas, x0, y0, x1, y1) : 
    width = (x1 - x0)
    canvas.create_rectangle(x0, y0, x0+width/3, y1, fill= 'black', width=0)
    canvas.create_rectangle(x0+width/3, y0, x0+width*2/3, y1, fill='yellow', width=0)
    canvas.create_rectangle(x0+width*2/3, y0, x1, y1, fill= 'red', width=0)

import math
def draw(canvas, width, height) :
    (cx, cy, r) = (width/2, height/2, min(width, height)/3)
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill= 'yellow')
    r = r * 0.85
    for hour in range(12) : 
        hourAngle = math.pi/2 - (2*math.pi)*(hour/12)
        hourX = cx + r * math.cos(hourAngle)
        hourY = cy - r * math.sin(hourAngle)
        label = str(hour if (hour > 0) else 12)
        canvas.create_text(hourX, hourY, text=label, font = 'Arial 16 bold')


runDrawing(400, 200)

