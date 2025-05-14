import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    entry_text = entry.get()
    
    # update the label
    label['text'] = entry_text
    entry['state'] = 'disabled'


def reset_func():
    # reset label text and enable entry
    label['text'] = 'Some text'
    entry['state'] = 'normal'


# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets 
label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

exercise_label = ttk.Label(master = window, text = "my label")
exercise_label.pack()

button = ttk.Button(master=window, text='The button', command=button_func)
button.pack()

exercise_button = ttk.Button(master=window, text='Reset', command=reset_func)
exercise_button.pack()

# run
window.mainloop()