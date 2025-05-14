import tkinter as tk

def save_data():
    pass  # Function to handle form submission

root = tk.Tk()
root.title("Acme Home Mortgage Application")

# Title Label
tk.Label(root, text="Acme Home Mortgage Loan Application", font=("Arial", 14, "bold")).pack(pady=10)

# First Name and Last Name
tk.Label(root, text="First Name:").pack()
entry_first_name = tk.Entry(root, width=25)
entry_first_name.pack()

tk.Label(root, text="Last Name:").pack()
entry_last_name = tk.Entry(root, width=25)
entry_last_name.pack()

# Email and Phone
tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

# Loan Amount
tk.Label(root, text="Loan Amount:").pack()
entry_loan_amount = tk.Entry(root, width=40)
entry_loan_amount.pack()

# Loan Term (Dropdown)
tk.Label(root, text="Loan Term:").pack()
loan_term_var = tk.StringVar(value="30-year")
loan_term_options = ["10-year", "15-year", "30-year"]
loan_term_menu = tk.OptionMenu(root, loan_term_var, *loan_term_options)
loan_term_menu.pack()

# Employment Status (Dropdown)
tk.Label(root, text="Employment Status:").pack()
employment_var = tk.StringVar(value="Employed")
employment_options = ["Employed", "Self-Employed", "Unemployed", "Student", "Retired"]
employment_menu = tk.OptionMenu(root, employment_var, *employment_options)
employment_menu.pack()

# Annual Income
tk.Label(root, text="Annual Income:").pack()
entry_income = tk.Entry(root, width=40)
entry_income.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit Application", command=save_data, bg="green", fg="white")
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
