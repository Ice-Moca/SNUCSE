from tkinter import * 

def draw(canvas, width, height) : 
    canvas.create_oval(100,50,300, 150, fill = "yellow")
    canvas.create_polygon(100,30,200,50,300,30,200,10, fill = "green")
    canvas.create_line(100,50,300,150, fill ="red", width=5)
    canvas.create_text(200,100, text = "Amazing!", fill = "purple", 
                               font = "Helvetica 26 bold underline" )
    canvas.create_text(200,100, text = "Carpe Diem!", anchor="sw", fill ="darkBlue",
                               font = "Times 28 bold italic")




def runDrawing(width=300, height=300) : 
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print( "bye!" )

runDrawing(400, 200)
