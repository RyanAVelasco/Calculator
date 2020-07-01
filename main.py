from tkinter import *



calculator = Tk()



emptyspace = Label(calculator, text="")
num1 = Button(calculator, text=1, padx=10, pady=10)
num2 = Button(calculator, text=2, padx=10, pady=10)
num3 = Button(calculator, text=3, padx=10, pady=10)
num4 = Button(calculator, text=4, padx=10, pady=10)
num5 = Button(calculator, text=5, padx=10, pady=10)
num6 = Button(calculator, text=6, padx=10, pady=10)
num7 = Button(calculator, text=7, padx=10, pady=10)
num8 = Button(calculator, text=8, padx=10, pady=10)
num9 = Button(calculator, text=9, padx=10, pady=10)
num0 = Button(calculator, text=0, padx=10, pady=10)
equal = Button(calculator, text="=", padx=10, pady=10)
dec = Button(calculator, text=".", padx=10, pady=10)
div = Button(calculator, text="/", padx=10, pady=10)
mult = Button(calculator, text="*", padx=10, pady=10)
sub = Button(calculator, text="-", padx=10, pady=10)
add = Button(calculator, text="+", padx=10, pady=10)
delete = Button(calculator, text="<", padx=10, pady=10)



emptyspace.grid(row=1)
num1.grid(row=4, column=0, padx=5, pady=5)
num2.grid(row=4, column=1, padx=5, pady=5)
num3.grid(row=4, column=2, padx=5, pady=5)
num4.grid(row=3, column=0, padx=5, pady=5)
num5.grid(row=3, column=1, padx=5, pady=5)
num6.grid(row=3, column=2, padx=5, pady=5)
num7.grid(row=2, column=0, padx=5, pady=5)
num8.grid(row=2, column=1, padx=5, pady=5)
num9.grid(row=2, column=2, padx=5, pady=5)
num0.grid(row=5, column=0, padx=5, pady=5)
dec.grid(row=5, column=1, padx=5, pady=5)
equal.grid(row=5, column=2, padx=5, pady=5)
div.grid(row=2, column=3, padx=5, pady=5)
mult.grid(row=3, column=3, padx=5, pady=5)
sub.grid(row=4, column=3, padx=5, pady=5)
add.grid(row=5, column=3, padx=5, pady=5)
delete.grid(row=2, column=4, padx=5, pady=5)



calculator.mainloop()