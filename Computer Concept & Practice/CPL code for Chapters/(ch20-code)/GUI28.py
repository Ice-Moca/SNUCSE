from tkinter import *
from tkinter.filedialog import *     

def callback( ) :
    name= askopenfilename( ) 
    print(name)
    
errmsg = 'Error!'
Bbb = Button(text='File Open', command=callback )
Bbb.pack( fill=X )

mainloop( )








