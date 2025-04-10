from tkinter import *

import os
os.chdir("C:\\Users\\hjkim\\Desktop" )

root =Tk( )

#image
suzi_photo  = PhotoImage( file = "suzi.png")
pic_label     = Label( root, image = suzi_photo, width=0, height=150)
name_label = Label( root, text = "This is Suzi", width =0, height=0)
pic_label.pack( )
name_label.pack( )

root.mainloop( )
