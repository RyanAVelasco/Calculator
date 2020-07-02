from tkinter import *

# === Draw the window
calculator = Tk()
calculator.title("Calculator")


# === Actions
def button_input(number):
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + str(number))


def button_add(f1):
    global first_number

    f1 = output.get()
    first_number = int(f1)
    output.delete(0, END)


def button_equal():
    second_number = output.get()
    output.delete(0, END)
    output.insert(0, first_number + int(second_number))


def button_clr():
    output.delete(0, END)


# === Buttons
value = Label(calculator, text="", padx=20, pady=20)
num1 = Button(calculator, text=1, padx=20, pady=20, command=lambda: button_input(1))
num2 = Button(calculator, text=2, padx=20, pady=20, command=lambda: button_input(2))
num3 = Button(calculator, text=3, padx=20, pady=20, command=lambda: button_input(3))
num4 = Button(calculator, text=4, padx=20, pady=20, command=lambda: button_input(4))
num5 = Button(calculator, text=5, padx=20, pady=20, command=lambda: button_input(5))
num6 = Button(calculator, text=6, padx=20, pady=20, command=lambda: button_input(6))
num7 = Button(calculator, text=7, padx=20, pady=20, command=lambda: button_input(7))
num8 = Button(calculator, text=8, padx=20, pady=20, command=lambda: button_input(8))
num9 = Button(calculator, text=9, padx=20, pady=20, command=lambda: button_input(9))
num0 = Button(calculator, text=0, padx=20, pady=20, command=lambda: button_input(0))
equal = Button(calculator, text="=", padx=20, pady=20, command=lambda: button_equal())
dec = Button(calculator, text=".", padx=20, pady=20, command=lambda: button_input())
div = Button(calculator, text="/", padx=20, pady=20, command=lambda: button_input())
mult = Button(calculator, text="*", padx=20, pady=20, command=lambda: button_input())
sub = Button(calculator, text="-", padx=20, pady=20, command=lambda: button_input())
add = Button(calculator, text="+", padx=20, pady=20, command=lambda: button_add(output.get()))
delete = Button(calculator, text="C", padx=20, pady=20, command=lambda: button_clr())

# === Grid
num1.grid(row=3, column=0)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)
num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)
num7.grid(row=1, column=0)
num8.grid(row=1, column=1)
num9.grid(row=1, column=2)
num0.grid(row=4, column=0)
dec.grid(row=4, column=1)
equal.grid(row=2, column=4)
div.grid(row=1, column=3)
mult.grid(row=2, column=3)
sub.grid(row=3, column=3)
add.grid(row=4, column=3)
delete.grid(row=1, column=4)

# === Output
output = Entry(calculator, width=45, borderwidth=5)
output.grid(row=0, column=0, columnspan=5)

# === Initiate the program
calculator.mainloop()
