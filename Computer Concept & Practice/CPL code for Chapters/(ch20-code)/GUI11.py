from tkinter import Tk, Button
from time import strftime, localtime

def clicked( ):     # not a event handler
     time = strftime("Day: %d %b %Y  \n  Time: %H : %M : %S %p  \n", localtime( ) )
     print(time)

root =Tk( )

mybutton = Button( root, text= "click it", command=clicked) 
mybutton.pack( ) 
root.mainloop( )





