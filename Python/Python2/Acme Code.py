import tkinter as tk
from tkinter import messagebox
import openpyxl
import os

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

# Function to save data to Excel
def save_data():
    try:
        wb = openpyxl.load_workbook(file_name)
        ws = wb.active
        ws.append([
            entry_first_name.get(), entry_last_name.get(), entry_email.get(), entry_phone.get(),
            entry_loan_amount.get(), loan_term_var.get(),
            employment_var.get(), entry_income.get()
        ])
        wb.save(file_name)
        wb.close()
        messagebox.showinfo("Success", "Application Submitted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

    # Clear input fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_loan_amount.delete(0, tk.END)
    entry_income.delete(0, tk.END)

# Create main application window
root = tk.Tk()
root.title("Acme Home Mortgage Loan Application")
root.geometry("850x400")  

# Create a frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0, anchor="n")  

# Labels and Entry Fields
title_label = tk.Label(frame, text="Acme Home Mortgage Loan Application", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=(5, 5))  

tk.Label(frame, text="First Name:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
entry_first_name = tk.Entry(frame, width=25)
entry_first_name.grid(row=1, column=1, sticky="w")

tk.Label(frame, text="Last Name:").grid(row=1, column=2, sticky="e", padx=5, pady=2)
entry_last_name = tk.Entry(frame, width=25)
entry_last_name.grid(row=1, column=3, sticky="w")

tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
entry_email = tk.Entry(frame, width=25)
entry_email.grid(row=2, column=1, sticky="w")

tk.Label(frame, text="Phone:").grid(row=2, column=2, sticky="e", padx=5, pady=2)
entry_phone = tk.Entry(frame, width=25)
entry_phone.grid(row=2, column=3, sticky="w")

tk.Label(frame, text="Loan Amount:").grid(row=3, column=0, sticky="e", padx=5, pady=2)
entry_loan_amount = tk.Entry(frame, width=25)
entry_loan_amount.grid(row=3, column=1, sticky="w")

tk.Label(frame, text="Loan Term:").grid(row=3, column=2, sticky="e", padx=5, pady=2)
loan_term_var = tk.StringVar(value="30-year")
loan_term_options = ["10-year", "15-year", "30-year"]
loan_term_menu = tk.OptionMenu(frame, loan_term_var, *loan_term_options)
loan_term_menu.grid(row=3, column=3, sticky="w")

tk.Label(frame, text="Employment Status:").grid(row=4, column=0, sticky="e", padx=5, pady=2)
employment_var = tk.StringVar(value="Employed")
employment_options = ["Employed", "Self-Employed", "Unemployed", "Student", "Retired"]
employment_menu = tk.OptionMenu(frame, employment_var, *employment_options)
employment_menu.grid(row=4, column=1, sticky="w")

tk.Label(frame, text="Annual Income:").grid(row=5, column=0, sticky="e", padx=5, pady=2)
entry_income = tk.Entry(frame, width=25)
entry_income.grid(row=5, column=1, sticky="w")

# Submit Button
submit_button = tk.Button(frame, text="Submit Application", command=save_data, bg="green", fg="white", font=("Arial", 12, "bold"))
submit_button.grid(row=6, column=0, columnspan=4, pady=(10, 5))  

# Run the Tkinter event loop
root.mainloop()
