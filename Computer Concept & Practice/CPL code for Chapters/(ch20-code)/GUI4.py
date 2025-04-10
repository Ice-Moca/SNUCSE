from tkinter import *

root=Tk( )

w = Label(root, text = "이름을 입력하세요", height = 7)
w.grid(row=1, column=1)

tBox = Entry(root)
tBox.grid(row=1, column=2, padx = 10)
root.mainloop( )         




