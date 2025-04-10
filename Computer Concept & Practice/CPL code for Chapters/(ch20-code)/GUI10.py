from tkinter import *
tk = Tk( )

canvas = Canvas(tk, width=400, height=400)
canvas.pack( )
Arrow = 0

def printarrow(event) :
    global Arrow
    canvas.delete(Arrow)
    if   event.keysym == 'Up' :  
        Arrow = canvas.create_polygon( 210, 200, 190, 200, 190, 180, 180,
          180, 200, 160, 220, 180, 210, 180, fill='yellow', outline='black')
    elif event.keysym == 'Down' :
        Arrow = canvas.create_polygon( 210, 200, 190, 200, 190, 220, 180,
          220, 200, 240, 220, 220, 210, 220, fill='pink', outline='black')
    elif event.keysym == 'Left' :
        Arrow = canvas.create_polygon( 200, 190, 200, 210, 180, 210, 180,
          220, 160, 200, 180, 180, 180, 190, fill='lightblue', outline='black')
    else :       # if event.keysym == ‘Right' 
        Arrow = canvas.create_polygon( 200, 190, 200, 210, 220, 210, 220,
          220, 240, 200, 220, 180, 220, 190, fill='white', outline='black')
        
canvas.bind_all( '<KeyPress-Up>',     printarrow )
canvas.bind_all( '<KeyPress-Down>', printarrow )
canvas.bind_all( '<KeyPress-Left>',    printarrow )
canvas.bind_all( '<KeyPress-Right>',  printarrow )





