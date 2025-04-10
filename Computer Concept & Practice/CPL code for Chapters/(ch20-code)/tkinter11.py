from tkinter import Tk, Canvas

def runDrawing(width=300, height=300) : 
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack( )
    draw(canvas, width, height)
    root.mainloop()

def draw(canvas, width, height):
    canvas.create_text(200,100, text= 'Aerial 18 bold underline' ,  fill= 'purple',  font = 'Aerial 18 bold underline' )
    canvas.create_text(200,150, text= '"Aerial CE" 18 bold underline' ,  fill= 'purple',  font = '"Aerial CE" 18 bold underline' )
    canvas.create_text(200,200, text= 'Helvetica 20 bold underline', fill= 'purple',  font = 'Helvetica 20 bold underline' )
    canvas.create_text(200,300, text= '명조 18 bold italic' , fill= 'darkBlue', font = ' 명조 18 bold italic'  )
    canvas.create_text(200,400, text= '궁서 18 bold italic' , fill= 'darkBlue', font = ' 궁서 18 bold italic'  )
    canvas.create_text(200,500, text= 'Times 28 bold italic' , fill= 'darkBlue', font = 'Times 28 bold italic'  )

runDrawing(500, 600)

