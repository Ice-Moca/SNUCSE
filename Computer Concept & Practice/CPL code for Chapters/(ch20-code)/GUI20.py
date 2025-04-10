from tkinter import *

def donothing( ):
   another_window = Toplevel(root)
   button = Button(another_window, text="Do nothing button")
   button.pack()
   
root = Tk( )
top_menubar = Menu(root)

filemenu = Menu( top_menubar, tearoff=0 )
filemenu.add_command( label="New",        command = donothing)
filemenu.add_command( label="Open",       command = donothing)
filemenu.add_command( label="Save",        command = donothing)
filemenu.add_command( label="Save as...",  command = donothing)
filemenu.add_command( label="Close",       command = donothing)
filemenu.add_separator( )
filemenu.add_command( label="Exit",          command = root.quit )
top_menubar.add_cascade( label="File", menu = filemenu )

editmenu = Menu( top_menubar, tearoff=0 )
editmenu.add_command( label="Undo",      command = donothing )
editmenu.add_separator( )
editmenu.add_command( label="Cut",         command = donothing )
editmenu.add_command( label="Copy",       command = donothing )
editmenu.add_command( label="Paste",       command = donothing )
editmenu.add_command( label="Delete",     command = donothing )
editmenu.add_command( label="Select All", command = donothing )
top_menubar.add_cascade( label="Edit", menu = editmenu )

helpmenu = Menu( top_menubar, tearoff=0 )
helpmenu.add_command( label="Help Index", command = donothing )
helpmenu.add_command( label="About...",     command = donothing )
top_menubar.add_cascade( label="Help", menu = helpmenu )

root.config( menu = top_menubar )

root.mainloop( )



