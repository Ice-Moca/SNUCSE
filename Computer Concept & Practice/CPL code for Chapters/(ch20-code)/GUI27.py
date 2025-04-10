from tkinter import *
from tkinter.messagebox import *

def answer( ) :
       showerror( "Answer", "Sorry, no answer available")

def callback( ) :
    if askyesno( 'Really quit?') :
        showwarning( 'Yes',  'Not yet implemented' )
    else :
        showinfo( 'No', 'Quit has been cancelled' )

B1 = Button( text='Quit',      command=callback )
B1.pack( fill = X )
B2 = Button( text='Answer',  command=answer )
B2.pack( fill = X )
mainloop( )







