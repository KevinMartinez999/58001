from tkinter import *

window = Tk()

window.geometry("500x400+10+10")
window.title("My First Graphical User Interface")

txt = Entry(window, border=10)
txt.place(x=170, y=150)
btn = Button(text="Click me", fg="blue", bg="pink")
btn.place(x=210, y=200)

lbl = Label(window,text="My first Demo", font ="Tahoma")
lbl.place(x=185,y=110)

window.mainloop()