import tkinter as tk
from tkinter import messagebox
import openpyxl
import os
import re 

# Ensure the directory exists
folder_path = r"c:\apps"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Excel file path
file_name = os.path.join(folder_path, "loan_applications.xlsx")

# Create the Excel file if it doesn't exist
if not os.path.exists(file_name):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["First Name", "Last Name", "Email", "Phone", "Loan Amount", "Loan Term", "Employment Status", "Annual Income"])
    wb.save(file_name)
    wb.close()

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create main application window
root = tk.Tk()
root.title("Acme Home Mortgage Loan Application")
root.geometry("850x400")  

# Create container for frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Frame 1 (Loan Application)
frame1 = tk.Frame(container)
frame1.grid(row=0, column=0, sticky="nsew")

# Labels and Entry Fields for Frame 1
title_label = tk.Label(frame1, text="Acme Home Mortgage Loan Application", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=(5, 5))  

tk.Label(frame1, text="First Name:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
entry_first_name = tk.Entry(frame1, width=25)
entry_first_name.grid(row=1, column=1, sticky="w")

tk.Label(frame1, text="Last Name:").grid(row=1, column=2, sticky="e", padx=5, pady=2)
entry_last_name = tk.Entry(frame1, width=35)
entry_last_name.grid(row=1, column=3, sticky="w")

tk.Label(frame1, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
entry_email = tk.Entry(frame1, width=25)
entry_email.grid(row=2, column=1, sticky="w")

tk.Label(frame1, text="Phone:").grid(row=2, column=2, sticky="e", padx=5, pady=2)
entry_phone = tk.Entry(frame1, width=25)
entry_phone.grid(row=2, column=3, sticky="w")

tk.Label(frame1, text="Loan Amount:").grid(row=3, column=0, sticky="e", padx=5, pady=2)
entry_loan_amount = tk.Entry(frame1, width=25)
entry_loan_amount.grid(row=3, column=1, sticky="w")

tk.Label(frame1, text="Loan Term:").grid(row=3, column=2, sticky="e", padx=5, pady=2)
loan_term_var = tk.StringVar(value="Select One")
loan_term_options = ["Select One", "10-year", "15-year", "30-year"]
loan_term_menu = tk.OptionMenu(frame1, loan_term_var, *loan_term_options)
loan_term_menu.grid(row=3, column=3, sticky="w")

tk.Label(frame1, text="Employment Status:").grid(row=4, column=0, sticky="e", padx=5, pady=2)
employment_var = tk.StringVar(value="Select One")
employment_options = ["Select One", "Employed", "Self-Employed", "Unemployed", "Student", "Retired"]
employment_menu = tk.OptionMenu(frame1, employment_var, *employment_options)
employment_menu.grid(row=4, column=1, sticky="w")

tk.Label(frame1, text="Annual Income:").grid(row=5, column=0, sticky="e", padx=5, pady=2)
entry_income = tk.Entry(frame1, width=25)
entry_income.grid(row=5, column=1, sticky="w")

submit_button = tk.Button(frame1, text="Submit Application", bg="green", fg="white", font=("Arial", 12, "bold"))
submit_button.grid(row=6, column=0, columnspan=4, pady=(10, 5)) 

next_button = tk.Button(frame1, text="Next →", command=lambda: show_frame(frame2))
next_button.grid(row=7, column=3, pady=10, sticky="e")

# Frame 2 (Work History)
frame2 = tk.Frame(container)
frame2.grid(row=0, column=0, sticky="nsew")

tk.Label(frame2, text="Work History", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(frame2, text="Current Employer:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
entry_current_employer = tk.Entry(frame2, width=25)
entry_current_employer.grid(row=1, column=1, sticky="w")
tk.Label(frame2, text="Years at Job:").grid(row=1, column=2, sticky="e", padx=5, pady=2)
entry_years_current = tk.Entry(frame2, width=10)
entry_years_current.grid(row=1, column=3, sticky="w")

for i in range(3):
    tk.Label(frame2, text="Previous Employer:").grid(row=i+2, column=0, sticky="e", padx=5, pady=2)
    tk.Entry(frame2, width=25).grid(row=i+2, column=1, sticky="w")
    tk.Label(frame2, text="Years at Job:").grid(row=i+2, column=2, sticky="e", padx=5, pady=2)
    tk.Entry(frame2, width=10).grid(row=i+2, column=3, sticky="w")

back_button = tk.Button(frame2, text="← Back", command=lambda: show_frame(frame1))
back_button.grid(row=5, column=0, pady=10, sticky="w")

submit_button = tk.Button(frame2, text="Submit Application", bg="green", fg="white", font=("Arial", 12, "bold"))
submit_button.grid(row=5, column=3, pady=10, sticky="e")

# Set the initial frame
show_frame(frame1)

# Run the Tkinter event loop
root.mainloop()
