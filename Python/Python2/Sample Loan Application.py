import tkinter as tk
from tkinter import messagebox
import openpyxl
import os
 
# Ensure the directory exists
folder_path = r"c:\apps"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)  # Create folder if it doesn't exist
 
# Excel file path
file_name = os.path.join(folder_path, "loan_applications.xlsx")
 
# Create the Excel file if it doesn't exist
if not os.path.exists(file_name):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Full Name", "Email", "Phone", "Loan Amount", "Loan Term (Years)", "Employment Status", "Annual Income"])
    wb.save(file_name)
    wb.close()  # Ensure file is closed
 
# Function to save data to Excel
def save_data():
    try:
        wb = openpyxl.load_workbook(file_name)
        ws = wb.active
        ws.append([
            entry_name.get(), entry_email.get(), entry_phone.get(),
            entry_loan_amount.get(), entry_loan_term.get(),
            employment_var.get(), entry_income.get()
        ])
        wb.save(file_name)
        wb.close()  # Ensure workbook is closed properly
        messagebox.showinfo("Success", "Application Submitted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")
 
    # Clear input fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_loan_amount.delete(0, tk.END)
    entry_loan_term.delete(0, tk.END)
    entry_income.delete(0, tk.END)
 
# Create main application window
root = tk.Tk()
root.title("Loan Application Form")
root.geometry("400x500")
 
# Labels and Entry Fields
tk.Label(root, text="Full Name:").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()
 
tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()
 
tk.Label(root, text="Phone:").pack(pady=5)
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()
 
tk.Label(root, text="Loan Amount:").pack(pady=5)
entry_loan_amount = tk.Entry(root, width=40)
entry_loan_amount.pack()
 
tk.Label(root, text="Loan Term (Years):").pack(pady=5)
entry_loan_term = tk.Entry(root, width=40)
entry_loan_term.pack()
 
tk.Label(root, text="Employment Status:").pack(pady=5)
employment_var = tk.StringVar(value="Employed")
employment_options = ["Employed", "Self-Employed", "Unemployed", "Student", "Retired"]
employment_menu = tk.OptionMenu(root, employment_var, *employment_options)
employment_menu.pack()
 
tk.Label(root, text="Annual Income:").pack(pady=5)
entry_income = tk.Entry(root, width=40)
entry_income.pack()
 
# Submit Button
submit_button = tk.Button(root, text="Submit Application", command=save_data, bg="green", fg="white")
submit_button.pack(pady=20)
 
# Run the Tkinter event loop
root.mainloop()