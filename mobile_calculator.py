import tkinter as tk
import math

# Global expression
expression = ""

# Function to update expression
def press(key):
    global expression
    if key == "^":   # agar user ^ press kare to backend mein ** daalo
        expression += "**"
    else:
        expression += str(key)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    equation.set("")

# Function for sqrt
def squareroot():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function for log base 10
def logbase10():
    global expression
    try:
        result = str(math.log10(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Create GUI window
root = tk.Tk()
root.title("Mobile Style Calculator")
root.geometry("350x500")
root.resizable(False, False)

equation = tk.StringVar()

# Input field
expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief='sunken', justify="right")
expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

# Button layout (like mobile calculator)
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("^",4,2), ("+",4,3),
]

# Create buttons
for (text, row, col) in buttons:
    b = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2,
                  command=lambda t=text: press(t))
    b.grid(row=row, column=col, padx=5, pady=5)

# Special buttons
tk.Button(root, text="C", font=('Arial', 18), width=5, height=2, command=clear).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="√", font=('Arial', 18), width=5, height=2, command=squareroot).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="log", font=('Arial', 18), width=5, height=2, command=logbase10).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="=", font=('Arial', 18), width=5, height=2, command=equalpress).grid(row=5, column=3, padx=5, pady=5)

root.mainloop()