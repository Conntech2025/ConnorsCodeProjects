import tkinter as tk 
from tkinter import ttk 
import subprocess

# Function to execute the contents of assignments
def run_assignment_1():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/Understanding the tkinter window and how to use widgets.py", "r") as file:
        exec(file.read())

def run_assignment_2():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2\Setting and getting widget data in tkinter.py", "r") as file:
        exec(file.read())

def run_assignment_3():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/Understanding Tkinter Variables.py", "r") as file:
        exec(file.read())

def run_assignment_4():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/An overview of the tkinter buttons (+using them with vraibles).py", "r") as file:
        exec(file.read())

def run_assignment_5():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/Using button functions with arguments in tkinter.py", "r") as file:
        exec(file.read())

def run_assignment_6():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/Understanding tkinter events.py", "r") as file:
        exec(file.read())

def run_assignment_7():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/The tkinter combobox and spinbox widgets.py", "r") as file:
        exec(file.read())

def run_assignment_8():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/creating tables in tkinter with the treeview widget.py", "r") as file:
        exec(file.read())

def run_assignment_9():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/Understanding parenting and frames in tkinter.py", "r") as file:
        exec(file.read())

def run_assignment_10():
    with open(r"C:/Users/stoic/OneDrive/Desktop/Python2/Tabs in Tkinter.py", "r") as file:
        exec(file.read())

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

# menu
menu = tk.Menu(window)

# sub menu
Set_of_Assignments_menu = tk.Menu(menu, tearoff=False)
Set_of_Assignments_menu.add_command(label="Understanding the tkinter window and how to use widgets", command=run_assignment_1)
Set_of_Assignments_menu.add_command(label="Setting and getting widget data in tkinter", command=run_assignment_2)
Set_of_Assignments_menu.add_command(label="Understanding tkinter variables", command=run_assignment_3)
menu.add_cascade(label="1st Set of Assignments", menu=Set_of_Assignments_menu)

# another sub menu
Assignments_menu = tk.Menu(menu, tearoff = False)
Assignments_menu.add_command(label="An overview of tkinter buttons (+using them with tkinter variables)", command=run_assignment_4)
Assignments_menu.add_command(label="Using button functions with arguments in tkinter", command=run_assignment_5)
Assignments_menu.add_command(label="Understanding tkinter events", command=run_assignment_6)
Assignments_menu.add_separator()
menu.add_cascade(label = '2nd Set of Assignments', menu = Assignments_menu)

# another sub menu
More_Assignments_menu = tk.Menu(menu, tearoff = False)
More_Assignments_menu.add_command(label="The tkinter combobox and spinbox widgets", command=run_assignment_7)
More_Assignments_menu.add_command(label="Creating tables in tkinter with the treeview widget", command=run_assignment_8)
More_Assignments_menu.add_command(label="Understanding parenting and frames in tkinter", command=run_assignment_9)
More_Assignments_menu.add_command(label="Tabs in tkinter", command=run_assignment_10)
More_Assignments_menu.add_separator()
menu.add_cascade(label = '3rd Set of Assignments', menu = More_Assignments_menu)


window.configure(menu = menu)

# run
window.mainloop()