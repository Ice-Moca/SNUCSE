from tkinter import *

root=Tk( )

def createTextBox(parent):
  tBox = Entry(parent)
  tBox.grid(row=1, column=2, padx = 10)
            
createTextBox(root)

w = Label(root, text = "이름을 입력하세요", height = 7)
w.grid(row=1, column=1)

root.mainloop( )         



