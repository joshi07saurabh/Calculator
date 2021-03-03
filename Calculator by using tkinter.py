 c from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("My Calculator")

def click(event):
    text=event.widget.cget("text")
    
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
            
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        entry.update()
    elif text=="C":
        scvalue.set("")
        entry.update()
    else:
        scvalue.set(scvalue.get()+ text)
        entry.update()

scvalue=StringVar()
scvalue.set("")
entry=Entry(root,textvariable=scvalue,font="lucida,25,bold")
entry.pack(pady=30,padx=30,ipady=20,fill=X)

frame=Frame(root,bg="grey")
frame.pack(padx=20,pady=2)
b=Button(frame,text="1",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="2",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="3",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)

frame=Frame(root,bg="grey")
frame.pack(padx=20,pady=2)
b=Button(frame,text="4",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="5",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="6",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)

frame=Frame(root,bg="grey")
frame.pack(padx=20,pady=2)
b=Button(frame,text="7",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="8",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="9",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)

frame=Frame(root,bg="grey")
frame.pack(padx=20,pady=2)
b=Button(frame,text="=",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="C",font="lucida,30,bold")
b.bind("<Button-1>",click)
b.pack(padx=2,pady=2,side=LEFT)
b=Button(frame,text="*",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)

frame=Frame(root,bg="grey")
frame.pack(padx=20,pady=2)
b=Button(frame,text="+",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="-",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
b=Button(frame,text="/",font="lucida,30,bold")
b.pack(padx=2,pady=2,side=LEFT)
b.bind("<Button-1>",click)
root.mainloop()
