import tkinter
from tkinter import ttk
from tkinter import messagebox
import openpyxl
import os

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            street_address = Street_Address_entry.get()
            city = city_entry.get()
            state = state_combobox.get()
            zip_code = zip_code_entry.get()

            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

 
            selected_education = [level for level, var in education_vars.items() if var.get() == 1]
            education_str = ", ".join(selected_education) if selected_education else "None"


            filepath = "data.xlsx"
            
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                sheet.append(["First Name", "Last Name", "Street Address", "City", "State", "Zip Code", "Registration Status", "# Courses", "# Semesters", "Education levels"])
                workbook.save(filepath)
            
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, street_address, city, state, zip_code, registration_status, numcourses, numsemesters, education_str])
            workbook.save(filepath)
            messagebox.showinfo("Success", "Data entered successfully!")

            reset_fields()

        else:
            messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms")

def reset_fields():
    """Clears all input fields and resets the cursor to 'First Name'."""
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    Street_Address_entry.delete(0, tkinter.END)
    city_entry.delete(0, tkinter.END)
    zip_code_entry.delete(0, tkinter.END)

    state_combobox.set("Select One") 

    reg_status_var.set("Not Registered")
    numcourses_spinbox.delete(0, tkinter.END)
    numcourses_spinbox.insert(0, "0")
    numsemesters_spinbox.delete(0, tkinter.END)
    numsemesters_spinbox.insert(0, "0")

    for var in education_vars.values():
        var.set(0) 

    accept_var.set("Not Accepted")

    first_name_entry.focus()  

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0, sticky="w")
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1, sticky="w")

first_name_entry = tkinter.Entry(user_info_frame, width=18)
last_name_entry = tkinter.Entry(user_info_frame, width=35)
first_name_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")
last_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

Street_Address_label = tkinter.Label(user_info_frame, text="Street Address")
Street_Address_label.grid(row=2, column=0, columnspan=2, sticky="w")

Street_Address_entry = ttk.Entry(user_info_frame, width=60)  
Street_Address_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")  

city_label = tkinter.Label(user_info_frame, text="City")
city_label.grid(row=4, column=0, sticky="w")

state_label = tkinter.Label(user_info_frame, text="State")
state_label.grid(row=4, column=1, sticky="w")

zip_code_label = tkinter.Label(user_info_frame, text="Zip Code")
zip_code_label.grid(row=4, column=2, sticky="w")

city_entry = tkinter.Entry(user_info_frame, width=25)
city_entry.grid(row=5, column=0, padx=5, pady=5, sticky="w")

state_combobox = ttk.Combobox(user_info_frame, width=25, values=[
    "Alaska", "Alabama", "Arakansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa",
    "Idaho", "Ilinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachussets", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri",
    "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin",
    "West Virgina", "Wyoming"])
state_combobox.grid(row=5, column=1, padx=5, pady=5, sticky="w")
state_combobox.set("Select One")

zip_code_entry = tkinter.Entry(user_info_frame, width=10)
zip_code_entry.grid(row=5, column=2, padx=5, pady=5)

#Saving Course Info
courses_frame = tkinter.LabelFrame(frame, text="Courses Information")
courses_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

#Education Level Checkboxes
education_label = tkinter.Label(courses_frame, text="Education Level")
education_label.grid(row=0, column=0, sticky="w")

education_levels = ["HS", "AAS", "BS", "MS", "PhD"]
education_vars = {}
education_frame = tkinter.Frame(courses_frame)
education_frame.grid(row=0, column=1, columnspan=5, sticky="w")


for level in education_levels:
    education_vars[level] = tkinter.IntVar()  # Create an IntVar for each checkbox
    chk = tkinter.Checkbutton(education_frame, text=level, variable=education_vars[level])
    chk.pack(side="left", padx=5)  # Use pack to arrange the checkboxes

#Registration Status
registration_frame = ttk.LabelFrame(frame, text="Registration Status")
registration_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(registration_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_check.grid(row=0, column=0, sticky="w")

#Completed Courses and Semesters
numcourses_label = tkinter.Label(registration_frame, text="# Completed Courses")
numcourses_label.grid(row=0, column=1, padx=5)
numcourses_spinbox = tkinter.Spinbox(registration_frame, from_=0, to=100, width=5)
numcourses_spinbox.grid(row=0, column=2, padx=5)

numsemesters_label = tkinter.Label(registration_frame, text="# Semesters")
numsemesters_label.grid(row=0, column=3, padx=5)
numsemesters_spinbox = tkinter.Spinbox(registration_frame, from_=0, to=20, width=5)
numsemesters_spinbox.grid(row=0, column=4, padx=5)

#Terms and Conditions
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", padx=5, pady=2)
terms_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.pack(anchor="w")

#Submit Button
button_frame = tkinter.Frame(frame) 
button_frame.grid(row=4, column=0, padx=10, pady=5, sticky="w")

button = tkinter.Button(button_frame, text="Enter Data", command=enter_data, width=8, height=1)
button.pack()

window.mainloop()