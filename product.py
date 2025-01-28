from tkinter import*
from datetime import date
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
num1 = Entry()
num1.place(x=80,y=40)
num2 = Entry()
num2.place(x=80,y=80)
def display():
    p = int(num1.get())
    q = int(num2.get())
    r=p*q
    text_box.insert(END,r)
text_box = Text(height=3)
btn = Button(text="Begin",command = display,height=1,bg="#1261A0",fg="white")
btn.place(x=80,y=110)
text_box.place(x=80,y=130)
root.mainloop()