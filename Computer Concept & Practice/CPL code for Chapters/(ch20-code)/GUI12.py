from tkinter import *
root=Tk( )
def enter():
    msg.set( "오!  당신의 이름은 {0} 이군요!".format( name.get( ) ) )

name = StringVar( )
msg = StringVar()

left = Label(root, text = "이름을 입력하세요", height = 7)
left.grid(row=1, column=1)
right = Entry(root, textvariable = name, width=30)
right.grid(row=1, column=2, padx = 10)

bottom = Label(root, textvariable = msg)
bottom.grid(row=2, column=1, columnspan=3)

but = Button(root, text="입력", width=10, command = enter)
but.grid(row=1, column=3)

root.mainloop( )






