from tkinter import *
root=Tk()
root.title('Simple Calculator')
num1=Entry(root,width=30, borderwidth=5, fg='white',bg='red')
num1.grid(row=0,column=0)
num1.insert(0,'Enter First Number:')
num2=Entry(root,width=30, borderwidth=5, fg='white',bg='blue')
num2.grid(row=0,column=1)
num2.insert(1,'Enter Second Number:')
def add():
    a=num1.get()
    a=int(a[19:])
    b=num2.get()
    b=int(b[20:])
    ans=a+b
    label=Label(root,text="Ans: "+str(ans),width=30,fg='green',bg='black').grid(row=0,column=2)
def mul():
    a=num1.get()
    a=int(a[19:])
    b=num2.get()
    b=int(b[20:])
    ans=a*b
    label=Label(root,text="Ans: "+str(ans),width=30,fg='green',bg='black').grid(row=0,column=2)
def sub():
    a=num1.get()
    a=int(a[19:])
    b=num2.get()
    b=int(b[20:])
    ans=a-b
    label=Label(root,text="Ans: "+str(ans),width=30,fg='green',bg='black').grid(row=0,column=2)
def div():
    a=num1.get()
    a=int(a[19:])
    b=num2.get()
    b=int(b[20:])
    ans=a/b
    label=Label(root,text="Ans: "+str(ans),width=30,fg='green',bg='black').grid(row=0,column=2)
    
add_button=Button(root,text="+",width=30,fg='white',bg='green',command=add).grid(row=3,column=0)
sub_button=Button(root,text="-",width=30,fg='white',bg='orange',command=sub).grid(row=3,column=1)
mul_button=Button(root,text="x",width=30,fg='white',bg='yellow',command=mul).grid(row=3,column=2)
div_button=Button(root,text="/",width=30,fg='white',bg='cyan',command=div).grid(row=3,column=3)

root.mainloop()
    
