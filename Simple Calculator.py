#Simple Calculator
from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.config(background="gray")
e=Entry(root,width=35,borderwidth=7,font=("Helvetica",10))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    get_the_entry= e.get()
    e.delete(0,END)
    e.insert(0,str(get_the_entry) + str(number))

def button_clear():
    e.delete(0,END)
def button_adds():
    num1= e.get()
    global number1
    number1= int(num1)
    e.delete(0,END)
def button_equals():
    num2=e.get()
    e.delete(0,END)
    e.insert(0,number1 + int(num2))

def button_sub():
    num3=e.get()
    global number3
    number3=int(num3)
    e.delete(0,END)

    return
#label
marcel=Label(root,text="Marcel",padx=20,pady=20,relief=RAISED)
marcel.grid(row=0,column=3)
#button
button_1= Button(root,text="1",padx=40,pady=20,bg="black",fg="white",command=lambda: button_click(1))
button_2= Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3= Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4= Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5= Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6= Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7= Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8= Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9= Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0= Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add=Button(root,text="+",padx=39,pady=20,command=button_adds)
button_equal=Button(root,text="=",padx=39,pady=20,command=button_equals)
buttons=Button(root,text="C",padx=39,pady=20,command=button_clear)
button_minus=Button(root,text="-",padx=40,pady=20,command=button_sub)
#buttons function
button_minus.grid(row=2,column=3)
buttons.grid(row=1,column=3)
button_equal.grid(row=4,column=3)
button_add.grid(row=3,column=3)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=1)
root.mainloop()
