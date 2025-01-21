from tkinter import *
from datetime import date
root = Tk()
root.title("Welcome")
root.geometry("400x400")
lbl = Label(text= "hey there",fg="blue",bg = "yellow",height=1,width=300)
namelbl = Label(text=" Full Name", bg="yellow")
namee = Entry()
def display ():
   name = namee.get()
   global Message
   message = "welcome to the app"
   greet = "hello" + name +"\n"
   text.insert(END, greet)
   text.insert(END, message)
   text.insert(END, date.today())
text = Text(height=5)
btn = Button(text="submit", fg="blue", bg="yellow", command=display,height=1)

lbl.pack()
namelbl.pack()
namee.pack()
btn.pack()
text.pack()
root.mainloop()