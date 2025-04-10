from tkinter import *
from tkinter.colorchooser import *                  

def callback( ) :
    result = askcolor( color="#6A9662", title = "Colour Chooser" ) 
    print(result)
    
root = Tk( )

B1 = Button(root, text='Choose Color', fg="darkgreen", command=callback )
B1.pack(side=LEFT, padx=10)
B2 = Button(text='Quit', command=root.quit, fg="red")
B2.pack(side=LEFT, padx=10)

root.mainloop( )









