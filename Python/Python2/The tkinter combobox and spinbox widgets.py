import tkinter as tk 
from tkinter import ttk 

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin') 

# combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
#  combo.configure(values = items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, from_ = 3, to = 20, increment = 3, command = lambda: print(spin_int.get()), textvariable = spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1,2,3,4,5)
spin.pack()

# run
window.mainloop()