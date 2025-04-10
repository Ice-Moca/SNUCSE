from tkinter import *
top = Tk( )
def onselect(event):
    w = event.widget
    idx = int( w.curselection( )[0] )
    value = w.get(idx)
    msg.set( '{0}이(가) 선택되었습니다'.format(value) )

msg = StringVar()
msg.set( "선택된 아이템이 없습니다. " )

Lb1 = Listbox(top)
Lb1.bind( '<<ListboxSelect>>'  ,  onselect)
Lb1.insert(1, "Python") ;  
Lb1.insert(2, "Perl") ; 
Lb1.insert(3, "C")
Lb1.insert(4, "PHP") ; 
Lb1.insert(5, "JSP") ; 
Lb1.insert(6, "Ruby")

Lb1.pack( )
L = Label(top, textvariable = msg)
L.pack()
top.mainloop( )


