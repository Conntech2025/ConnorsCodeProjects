import tkinter as tk 
from tkinter import ttk 

# list of events
# pythontutorial.net/tkinter/tkinter-event-binding

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

# Center the window on the screen
def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

# window
window = tk.Tk()
center_window(window, 600, 500)
window.title('Event Binding')


# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# events
button.bind('<Alt-KeyPress-a>', lambda event: print(event))
window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

window.bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))

# exercise :
# print 'Mousewheel' when the user holds down shift and use the mousewheel while the text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# run
window.mainloop()