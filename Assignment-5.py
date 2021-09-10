import tkinter

from tkinter import messagebox

def add():
    a = int(e1.get())
    b = int(e2.get())
    result = 'Addition:\n\t' + str(a) + ' + ' + str(b) + ' = ' + str(a+b)
    messagebox.showinfo('Result', result)

def subtract():
    a = int(e1.get())
    b = int(e2.get())
    result = 'Subtraction:\n\t' + str(a) + ' - ' + str(b) + ' = ' + str(a-b)
    messagebox.showinfo('Result', result)
    
def multiply():
    a = int(e1.get())
    b = int(e2.get())
    result = 'Multiplition:\n\t' + str(a) + ' x ' + str(b) + ' = ' + str(a*b)
    messagebox.showinfo('Result', result)

def divide():
    a = int(e1.get())
    b = int(e2.get())
    result = 'Division:\n\t' + str(a) + ' / ' + str(b) + ' = ' + str(a/b)
    messagebox.showinfo('Result', result)
    
root = tkinter.Tk()

l1 = tkinter.Label(root, text = 'Enter the first number')
l1.grid(row = 0, column = 0)
l2 = tkinter.Label(root, text = 'Enter the second number')
l2.grid(row = 1, column = 0)

e1 = tkinter.Entry(root)
e1.grid(row = 0, column = 1)
e2 = tkinter.Entry(root)
e2.grid(row = 1, column = 1)

l3 = tkinter.Label(root, text = 'Choose the operation:')
l3.grid(row = 3, column = 0)

b1 = tkinter.Button(root, text = 'Add', command = add)
b1.grid(row = 4, column = 0)
b2 = tkinter.Button(root, text = 'Subtract', command = subtract)
b2.grid(row = 5, column = 0)
b3 = tkinter.Button(root, text = 'Multiply', command = multiply)
b3.grid(row = 6, column = 0)
b4 = tkinter.Button(root, text = 'Divide', command = divide)
b4.grid(row = 7, column = 0)

root.mainloop()
