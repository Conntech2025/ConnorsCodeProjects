import tkinter
from tkinter import ttk, messagebox
import openpyxl
import os

def enter_data():
    accepted = accept_var.get()
    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            registration_status = reg_status_var.get()
            num_courses = num_courses_spinbox.get()
            num_semesters = num_semesters_spinbox.get()
            
            print("First Name:", firstname, "Last Name:", lastname)
            print("Title:", title, "Age:", age, "Nationality:", nationality)
            print("Registration Status:", registration_status)
            print("# Courses:", num_courses, "# Semesters:", num_semesters)
            print("------------------------------------------")
            
            filepath = "data.xlsx"
            
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                sheet.append(["First Name", "Last Name", "Title", "Age", "Nationality", "Registration Status", "# Courses", "# Semesters"])
                workbook.save(filepath)
            
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters])
            workbook.save(filepath)
            messagebox.showinfo("Success", "Data entered successfully!")
        else:
            messagebox.showwarning("Error", "First name and last name are required.")
    else:
        messagebox.showwarning("Error", "You have not accepted the terms.")

# Window setup
window = tkinter.Tk()
window.title("Data Entry Form")
frame = tkinter.Frame(window)
frame.pack()

# User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

tkinter.Label(user_info_frame, text="First Name").grid(row=0, column=0)
tkinter.Label(user_info_frame, text="Last Name").grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0, padx=5, pady=5)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

tkinter.Label(user_info_frame, text="Title").grid(row=0, column=2)
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Dr."])
title_combobox.grid(row=1, column=2, padx=5, pady=5)

tkinter.Label(user_info_frame, text="Age").grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0, padx=5, pady=5)

tkinter.Label(user_info_frame, text="Nationality").grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "South America", "Oceania"])
nationality_combobox.grid(row=3, column=1, padx=5, pady=5)

# Course Information
courses_frame = tkinter.LabelFrame(frame, text="Course Information")
courses_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

tkinter.Label(courses_frame, text="Registration Status").grid(row=0, column=0)
reg_status_var = tkinter.StringVar(value="Not Registered")
tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered").grid(row=1, column=0, sticky="w")

tkinter.Label(courses_frame, text="# Completed Courses").grid(row=0, column=1)
num_courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=100)
num_courses_spinbox.grid(row=1, column=1)

tkinter.Label(courses_frame, text="# Semesters").grid(row=0, column=2)
num_semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=20)
num_semesters_spinbox.grid(row=1, column=2)

# Terms & Conditions
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, padx=20, pady=10, sticky="w")

accept_var = tkinter.StringVar(value="Not Accepted")
tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted").grid(row=0, column=0, sticky="w")

# Submit Button
button_frame = tkinter.Frame(frame)
button_frame.grid(row=3, column=0, padx=20, pady=10, sticky="w")

tkinter.Button(button_frame, text="Enter Data", command=enter_data).pack()

window.mainloop()