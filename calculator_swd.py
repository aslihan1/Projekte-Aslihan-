#Bibliotheken
import tkinter as tk
import math

tk_window = tk.Tk()
tk_window.geometry('550x500')
tk_window.configure(bg='pink')
tk_window.title('CALCULATOR')



def calculator():

    first_button.destroy() #destroy the first button when clicked

    def button_click(number):
        current = display.get()
        clear()
        display.insert(0, str(current) + str(number))

    def clear():
        display.delete(0, tk.END)

    def add():
        first_number = display.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        display.delete(0, tk.END)

    def subtract():
        first_number = display.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        display.delete(0, tk.END)

    def multiply():
        first_number = display.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        display.delete(0, tk.END)

    def divide():
        first_number = display.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        display.delete(0, tk.END)

    def cos():
        result = math.cos(math.degrees(float(display.get())))
        display.delete(0, "end")
        display.insert(0, result)

    def sin():
        result = math.sin(float(display.get()))
        display.delete(0, "end")
        display.insert(0, result)

    def tan():
        result = math.tan(float(display.get()))
        display.delete(0, "end")
        display.insert(0, result)

    def equal():
        second_number = display.get()
        display.delete(0, tk.END)

        if math == "addition":
            display.insert(0, f_num + int(second_number))
        elif math == "subtraction":
            display.insert(0, f_num - int(second_number))
        elif math == "multiplication":
            display.insert(0, f_num * int(second_number))
        elif math == "division":
            display.insert(0, f_num / int(second_number))
        elif math == "cosinus":
            display.insert(0, )

    #Frame of the calculator's buttons
    calculator_frame = tk.Frame(tk_window, bg='white')
    calculator_frame.pack()

    #create an entry for the numbers
    display = tk.Entry(calculator_frame, width=40, font=('Helvetica', 17, 'bold'), bg='pink', fg='blue')
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    #Buttons
    button_1 = tk.Button(calculator_frame, text='1', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(1))
    button_2 = tk.Button(calculator_frame, text='2', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(2))
    button_3 = tk.Button(calculator_frame, text='3', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(3))
    button_4 = tk.Button(calculator_frame, text='4', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(4))
    button_5 = tk.Button(calculator_frame, text='5', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(5))
    button_6 = tk.Button(calculator_frame, text='6', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(6))
    button_7 = tk.Button(calculator_frame, text='7', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(7))
    button_8 = tk.Button(calculator_frame, text='8', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(8))
    button_9 = tk.Button(calculator_frame, text='9', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(9))
    button_0 = tk.Button(calculator_frame, text='0', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: button_click(0))
    button_clr = tk.Button(calculator_frame, text='CLR', width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: clear())
    button_add = tk.Button(calculator_frame, text="+", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: add())
    button_subtract = tk.Button(calculator_frame, text="-", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: subtract())
    button_multiply = tk.Button(calculator_frame, text="*", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: multiply())
    button_divide = tk.Button(calculator_frame, text="/", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: divide())
    button_equal = tk.Button(calculator_frame, text="=", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: equal())
    button_cos = tk.Button(calculator_frame, text="cos", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: cos())
    button_sin = tk.Button(calculator_frame, text="sin", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: sin())
    button_tan = tk.Button(calculator_frame, text="tan", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue',command=lambda: tan())
    button_dot = tk.Button(calculator_frame, text=".", width=9, height=2, font=('Helvetica', 15, 'bold'), fg='blue')

    #places the buttons on the grid
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)
    button_7.grid(row=5, column=0)
    button_8.grid(row=5, column=1)
    button_9.grid(row=5, column=2)
    button_0.grid(row=6, column=1)
    button_clr.grid(row=6, column=0)
    button_add.grid(row=3, column=3)
    button_subtract.grid(row=4, column=3)
    button_multiply.grid(row=5, column=3)
    button_divide.grid(row=6, column=3)
    button_equal.grid(row=6, column=2)
    button_cos.grid(row=7, column=0)
    button_sin.grid(row=7, column=1)
    button_tan.grid(row=7, column=2)
    button_dot.grid(row=7, column=3)
# First button of the window
first_button = tk.Button(tk_window, text='Rechne mit mir!', font=('Helvetica', 15, 'bold'), fg='blue',
                         highlightbackground='darkblue', border=5, width=15, height=3, command=calculator)
first_button.pack()

tk_window.mainloop()
