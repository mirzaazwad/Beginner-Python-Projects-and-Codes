#!/usr/bin/env python3
from tkinter import *

root = Tk()
root.title("EEE announcement")
T=Text(root,height=10,width=150)
T.grid(row=7,column=1)
def myclick():
    string="""The EEE final viva for the group with student ID 2000421{0} to 2000421{1} would be held today, {2}th Nov 2021, {3} from {4} onwards,
the link is given below:
{5}
Join in due time as per the instructions given earlier\n""".format(SIDi.get(),SIDf.get(),day.get(),wday.get(),time.get(),link.get())
    T.insert(END,string)


s1label=Label(root,text="First Student ID: ").grid(row=0,column=0)
SIDi=Entry(root,width=50)
SIDi.grid(row=0,column=1)
s2label=Label(root,text="Last Student ID:").grid(row=1,column=0)
SIDf=Entry(root,width=50)
SIDf.grid(row=1,column=1)
dlabel=Label(root,text="Enter Date Day:").grid(row=2,column=0)
day=Entry(root,width=50)
day.grid(row=2,column=1)
wlabel=Label(root,text="Enter Week Day:").grid(row=3,column=0)
wday=Entry(root,width=50)
wday.grid(row=3,column=1)
tlabel=Label(root,text="Enter Time:").grid(row=4,column=0)
time=Entry(root,width=50)
time.grid(row=4,column=1)
llabel=Label(root,text="Enter Link:").grid(row=5,column=0)
link=Entry(root,width=50)
link.grid(row=5,column=1)
output=Label(root,text="Output: ").grid(row=7,column=0)
mybutton=Button(root,text="Announcement",command=myclick).grid(row=6,column=1)
root.mainloop()
