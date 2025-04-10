from tkinter import *
root = Tk( )

def hello(event) : 
    print("Single Click, Button-1") 

def quit(event) : 
    print("Double Click, so let's stop!") 
    import sys; 
    sys.exit() 

wbutton = Button(root, text='Mouse Clicks') 
wbutton.pack( ) 

wbutton.bind('<Button-1>', hello) 
wbutton.bind('<Double-Button-1>', quit) 

root.mainloop( )




