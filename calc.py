import tkinter as tk
from tkinter import  messagebox

mainWindow = tk.Tk()
mainWindow.title("Sample Window")


heading_label = tk.Label(mainWindow, text="Enter 1st number")
heading_label.pack()

first_no = tk.Entry(mainWindow)
first_no.pack()

heading_label1 = tk.Label(mainWindow, text="Enter 2nd number")
heading_label1.pack()

second_no = tk.Entry(mainWindow)
second_no.pack()


def addition():
    first, second = takeInput()
    result = first + second
    result_label.config(text="Operations result is: " +
                             str(result))

def subtraction():
    first, second = takeInput()
    result = first - second
    result_label.config(text="Operations result is: " +
                             str(result))

def multiplication():
    first, second = takeInput()
    result = first * second
    result_label.config(text="Operations result is: " +
                             str(result))


def division():
    first, second = takeInput()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))

def takeInput():
    first = first_no.get()
    second = second_no.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_no.get()) == 0) or (len(second_no.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


add_button = tk.Button(mainWindow, text="+",
                            command=lambda : addition())
add_button.pack()

subtract_button = tk.Button(mainWindow, text="-",
                         command=lambda : subtraction())
subtract_button.pack()

multiply_button = tk.Button(mainWindow, text="*",
                            command=lambda : multiplication())
multiply_button.pack()

divide_button = tk.Button(mainWindow, text="/",
                            command=lambda : division())
divide_button.pack()

result_label = tk.Label(mainWindow, text="Operations result is:")
result_label.pack()


mainWindow.mainloop()
