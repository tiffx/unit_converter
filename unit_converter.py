from tkinter import *

window = Tk()

def km_to_miles():
    g = float(e1_value.get())*1000
    lb = float(e1_value.get())*2.20462
    oz = float(e1_value.get())*35.274
    t_g.delete("1.0",END)
    t_g.insert(END,g)
    t_lb.delete("1.0",END)
    t_lb.insert(END,lb)
    t_oz.delete("1.0",END)
    t_oz.insert(END,oz)

label = Label(window,text="kg")
label.grid(row=0,column=1)

g_label = Label(window,text="g")
g_label.grid(row=1,column=0)

lb_label = Label(window,text="lb")
lb_label.grid(row=1,column=1)

oz_label = Label(window,text="oz")
oz_label.grid(row=1,column=2)

b1 = Button(window,text="Convert",command=km_to_miles)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=0)

t_g = Text(window,height=1,width=20)
t_g.grid(row=2,column=0)

t_lb = Text(window,height=1,width=20)
t_lb.grid(row=2,column=1)

t_oz = Text(window,height=1,width=20)
t_oz.grid(row=2,column=2)

window.mainloop()