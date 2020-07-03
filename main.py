from tkinter import *
from PIL import ImageTk, Image
import math

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
    global math

    math = "add"
    f1 = output.get()
    first_number = float(f1)
    output.delete(0, END)


def button_sub(f1):
    global first_number
    global math

    math = "sub"
    f1 = output.get()
    first_number = float(f1)
    output.delete(0, END)


def button_mult(f1):
    global first_number
    global math

    math = "mult"
    f1 = output.get()
    first_number = float(f1)
    output.delete(0, END)


def button_div(f1):
    global first_number
    global math

    math = "div"
    f1 = output.get()
    first_number = float(f1)
    output.delete(0, END)



def button_sq(f1):
    global first_number

    first_number = float(output.get())
    output.delete(0, END)
    output.insert(0,(first_number ** 2))


def button_cube(f1):
    global first_number

    first_number = float(output.get())
    output.delete(0, END)
    output.insert(0,(first_number ** 3))


def button_quad(f1):
    global first_number

    first_number = float(output.get())
    output.delete(0, END)
    output.insert(0,(first_number ** 4))


def button_sqrt(f1):
    global first_number

    first_number = float(output.get())
    output.delete(0, END)
    output.insert(0, math.sqrt(first_number))



def button_equal():
    second_number = output.get()
    output.delete(0, END)

    if math == "add":
        output.insert(0, first_number + float(second_number))
    elif math == "sub":
        output.insert(0, first_number - float(second_number))
    elif math == "mult":
        output.insert(0, first_number * float(second_number))
    elif math == "div":
        output.insert(0, first_number / float(second_number))



def button_clr():
    output.delete(0, END)


def buttonRightReveal():
    sqrt.grid(row=1, column=6)
    sq.grid(row=2, column=6)
    cube.grid(row=3, column=6)
    quad.grid(row=4, column=6)


# === Centre Reveal
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
dec = Button(calculator, text=".", padx=21, pady=20, command=lambda: button_input("."))
div = Button(calculator, text="÷", padx=20, pady=20, command=lambda: button_div(output.get()))
mult = Button(calculator, text="×", padx=20, pady=20, command=lambda: button_mult(output.get()))
sub = Button(calculator, text="−", padx=20, pady=20, command=lambda: button_sub(output.get()))
add = Button(calculator, text="+", padx=20, pady=20, command=lambda: button_add(output.get()))
equal = Button(calculator, text="=", padx=19, pady=20, command=lambda: button_equal())
clear = Button(calculator, text="C", padx=21, pady=116, command=lambda: button_clr())
# === Right Reveal
reveal_r = Button(calculator, text="ᐅ", pady=116, bg="lightblue", command=lambda: buttonRightReveal())
sqrt = Button(calculator, text="√", padx=12, pady=20, command=lambda: button_sqrt(output.get()))
sq = Button(calculator, text="²", padx=14, pady=20, command=lambda: button_sq(output.get()))
cube = Button(calculator, text="³", padx=14, pady=20, command=lambda: button_cube(output.get()))
quad = Button(calculator, text="⁴", padx=14, pady=20, command=lambda: button_quad(output.get()))
# === Bottom Reveal
reveal_b = Button(calculator, text="ᐁ", padx=148)  # improving this at a later date to include a graph

# === Centre Grid
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
equal.grid(row=4, column=2)
clear.grid(row=1, column=4, rowspan=4)
div.grid(row=1, column=3)
mult.grid(row=2, column=3)
sub.grid(row=3, column=3)
add.grid(row=4, column=3)
# === Right Grid
reveal_r.grid(row=1, column=5, rowspan=4)
# === Bottom Grid
reveal_b.grid(row=5, column=0, columnspan=6)

# === Output
output = Entry(calculator, width=34, borderwidth=5, font=12)
output.grid(row=0, column=0, columnspan=6)

# === Initiate the program
calculator.mainloop()
