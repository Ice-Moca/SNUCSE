from tkinter import * 


def draw(canvas, width, height) : 
    margin = 10
    canvas.create_rectangle(margin, margin, 
                            width - margin, height - margin, fill = "darkGreen")

    (cx,cy) = (width/2, height/2)
    (rect_width, rect_height) = (width/4, height/4)

    canvas.create_rectangle( cx - rect_width/2, cy - rect_height/2,
		            cx + rect_width/2, cy + rect_height/2,
		            fill = "orange")


def runDrawing(width=300, height=300) : 
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print( "bye!" )

runDrawing(400, 200)
