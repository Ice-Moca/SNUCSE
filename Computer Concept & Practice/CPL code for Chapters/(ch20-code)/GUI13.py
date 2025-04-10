from tkinter import *
root = Tk( )

def callback(m):
    msg.set('오! 당신의 이름은 {0} 이군요!'.format( m.get() ))

name= StringVar( )
name.trace( "w", lambda *args: callback(name) )
msg = StringVar()
msg.set( '당신의 이름은 ooo 입니다' )

left = Label(root, text = '이름을 입력하세요',  height = 7)
left.grid(row=1, column=1)
right = Entry(root, textvariable = name, width=30)
right.grid(row=1, column=2, padx = 10)

buttom = Label(root, textvariable = msg)
buttom.grid(row=2, column=1, columnspan=3)

root.mainloop( )
