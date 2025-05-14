import tkinter
from tkinter import ttk
from tkinter import messagebox

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

            print("First name:", firstname, "Last name:", lastname)
            print("Street Address:", street_address, "City:", city, "State:", state, "Zip Code:", zip_code)
            print("# Courses:", numcourses, "# Semesters:", numsemesters)
            print("Registration status:", registration_status)
            print("------------------------------------------")
        else:
            messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# User Information Section
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

# First Name & Last Name
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0, sticky="w")
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1, sticky="w")

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0, padx=5, pady=5)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

# Street Address (Single Row)

Street_Address_label = tkinter.Label(user_info_frame, text="Street Address")
Street_Address_label.grid(row=2, column=0, columnspan=2, sticky="w")

Street_Address_entry = ttk.Entry(user_info_frame, width=40)  # Decreased width
Street_Address_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")  # No column spanning



# City, State, and Zip Code in One Row
city_label = tkinter.Label(user_info_frame, text="City")
city_label.grid(row=4, column=0, sticky="w")

state_label = tkinter.Label(user_info_frame, text="State")
state_label.grid(row=4, column=1, sticky="w")

zip_code_label = tkinter.Label(user_info_frame, text="Zip Code")
zip_code_label.grid(row=4, column=2, sticky="w")

city_entry = tkinter.Entry(user_info_frame)
city_entry.grid(row=5, column=0, padx=5, pady=5)

state_combobox = ttk.Combobox(user_info_frame, values=[
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY"])
state_combobox.grid(row=5, column=1, padx=5, pady=5)

zip_code_entry = tkinter.Entry(user_info_frame)
zip_code_entry.grid(row=5, column=2, padx=5, pady=5)

# Courses Information Section
courses_frame = tkinter.LabelFrame(frame, text="Courses Information")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Education Level Section (Checkboxes in One Row)
education_label = tkinter.Label(courses_frame, text="Education Level")
education_label.grid(row=0, column=0, sticky="w", columnspan=5, pady=(0, 5))

education_levels = ["HS", "AAS", "BS", "MS", "PhD"]
education_vars = []
education_frame = tkinter.Frame(courses_frame)
education_frame.grid(row=1, column=0, columnspan=5, sticky="w")

for i, level in enumerate(education_levels):
    var = tkinter.BooleanVar()
    chk = tkinter.Checkbutton(education_frame, text=level, variable=var)
    chk.grid(row=0, column=i, padx=5, sticky="w")
    education_vars.append(var)

# Registration Status
registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_label.grid(row=2, column=0, sticky="w")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_check.grid(row=3, column=0, sticky="w")

# Completed Courses and Semesters
numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_label.grid(row=2, column=1)
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=100)
numcourses_spinbox.grid(row=3, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_label.grid(row=2, column=2)
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=20)
numsemesters_spinbox.grid(row=3, column=2)

# Terms and Conditions
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", padx=5, pady=2)
terms_frame.grid(row=2, column=0, sticky="w", padx=10, pady=5)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.pack(anchor="w")


# Submit Button
button_frame = tkinter.Frame(frame) 
button_frame.grid(row=3, column=0, padx=18, pady=10, sticky="w")

button = tkinter.Button(button_frame, text="Enter Data", command=enter_data, width=8, height=1)
button.pack()

window.mainloop()
