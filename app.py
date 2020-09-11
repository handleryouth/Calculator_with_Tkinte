import tkinter as tk
import tkinter.font as font
import math
import re
from DPI import setting_dpi


expression = ""

def press(num):
    global expression
    if num == 'log':
        finding = re.split(r'[\W]', expression)
        if finding:
            last_one = finding[-1]
            log = str(math.log10(int(last_one)))
            after = expression.replace(last_one, log)
            equation.set(after)
    else:
        expression = expression + str(num)
        equation.set(expression)

def cancel():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        showing.set(total)
    except:
        equation.set("Error. Try Again ! ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")
    showing.set("")

def pressed_key(event):
    key = event.char
    if key == '+':
        press("+")
    elif key =='-':
        press("-")
    elif key == "*":
        press('*')
    elif key == "/":
        press('/')
    elif key == "=":
        equalpress()
    elif key == ".":
        press(".")
    elif key == '1':
        key = int(key)
        press(key)
    elif key == '2':
        key = int(key)
        press(key)
    elif key == '3':
        key = int(key)
        press(key)
    elif key == '4':
        key = int(key)
        press(key)
    elif key == '5':
        key = int(key)
        press(key)
    elif key == '6':
        key = int(key)
        press(key)
    elif key == '7':
        key = int(key)
        press(key)
    elif key == '8':
        key = int(key)
        press(key)
    elif key == '9':
        key = int(key)
        press(key)
    elif key == '0':
        key = int(key)
        press(key)
    elif key == '(':
        press(key)
    elif key == ')':
        press(key)
    elif key =='\r':
        equalpress()



if __name__ == "__main__":
    setting_dpi()
    root = tk.Tk()
    root.configure(background="gainsboro")
    root.title("Calculator")
    root.resizable(True, False)

    font.nametofont("TkDefaultFont").configure(size=12)

    equation = tk.StringVar()
    showing = tk.StringVar()

    expression_field = tk.Entry(root, textvariable=equation, justify='right', font=("Segoe UI",15))
    expression_field['state'] = 'disabled'

    expression_field.grid(columnspan=4, ipadx=100, ipady=20, padx = 15, pady = 15, sticky = "W")

    equation.set('Your Number Here ....')

    end_count = tk.Entry(root, justify = 'right', state = 'disabled', textvariable=showing, font=("Segoe UI",15))
    end_count.grid(columnspan=4, ipadx=30, ipady=10, row=2, sticky = 'E', padx= 15, pady = 15)

    showing.set('Shown Here !')
    root.bind('<Key>', pressed_key)

    button1 = tk.Button(root, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=3, column=0, padx= 10, pady = 10)

    button2 = tk.Button(root, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=3, column=1, padx= 10, pady = 10)

    button3 = tk.Button(root, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=3, column=2, padx= 10, pady = 10)

    button4 = tk.Button(root, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=4, column=0, padx= 10, pady = 10)

    button5 = tk.Button(root, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=4, column=1, padx= 10, pady = 10)

    button6 = tk.Button(root, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=4, column=2, padx= 10, pady = 10)

    button7 = tk.Button(root, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=5, column=0, padx= 10, pady = 10)

    button8 = tk.Button(root, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=5, column=1, padx= 10, pady = 10)

    button9 = tk.Button(root, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=5, column=2, padx= 10, pady = 10)

    button0 = tk.Button(root, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=6, column=0, padx= 10, pady = 10)

    plus = tk.Button(root, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=3, column=3, padx= 10, pady = 10)

    minus = tk.Button(root, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=4, column=3, padx= 10, pady = 10)

    multiply = tk.Button(root, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=5, column=3, padx= 10, pady = 10)

    divide = tk.Button(root, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=6, column=3, padx= 10, pady = 10)

    equal = tk.Button(root, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=6, column=2, padx= 10, pady = 10)

    clear = tk.Button(root, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=6, column=1, padx= 10, pady = 10)

    Decimal = tk.Button(root, text='comma', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=7, column=0, padx= 10, pady = 10)

    square_root = tk.Button(root, text='√', fg='black', bg='red',
                     command=lambda: press('**0.5'), height=1, width=7)
    square_root.grid(row=7, column=2, padx= 10, pady = 10)

    logarithm = tk.Button(root, text='Log', fg='black', bg='red',
                            command=lambda: press('log'), height=1, width=7)
    logarithm.grid(row=7, column=1, padx= 10, pady = 10)

    square = tk.Button(root, text='^2', fg='black', bg='red',
                     command=lambda: press('**2'), height=1, width=7)
    square.grid(row=7, column=3, padx= 10, pady = 10)

    pi = tk.Button(root, text='π', fg='black', bg='red',
                     command=lambda: press('3.14159265359'), height=1, width=7)
    pi.grid(row=8, column=0, padx= 10, pady = 10)

    deleting = tk.Button(root, text='Del', fg='black', bg='red',
                     command=lambda: cancel(), height=1, width=7)
    deleting.grid(row=8, column=1, padx= 10, pady = 10)

    open_bracket = tk.Button(root, text='(', fg='black', bg='red',
                         command=lambda: press('('), height=1, width=7)
    open_bracket.grid(row=8, column=2, padx=10, pady=10)

    close_bracket = tk.Button(root, text=')', fg='black', bg='red',
                             command=lambda: press(')'), height=1, width=7)
    close_bracket.grid(row=8, column=3, padx=10, pady=10)


    root.mainloop()
