from tkinter import *
top = Tk( )
CheckVar1 = IntVar( )
CheckVar2 = IntVar( )

def choice( ):
    if CheckVar1.get( ) == 1 and CheckVar2.get( ) == 0:
       msg1 = "You like Music!"
       mylabel.config( text = msg1 )       
    if CheckVar1.get( ) == 0 and CheckVar2.get( ) == 1:
       msg2 = "You like Video!"
       mylabel.config( text = msg2 )
    if CheckVar1.get( ) == 1 and CheckVar2.get( ) == 1:
       msg3 = "You like both Music and Video!"
       mylabel.config( text = msg3 )
    if CheckVar1.get( ) == 0 and CheckVar2.get( ) == 0:
       msg4 = "Oh Come on!"
       mylabel.config( text = msg4 )
       
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, 
                         height=5, width = 20, command = choice)     
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, 
                         height=5, width = 20, command = choice)
C1.pack( )
C2.pack( )

mylabel = Label(top)
mylabel.pack( )


top.mainloop( )
