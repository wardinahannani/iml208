import tkinter
from tkinter import ttk
from tkinter import messagebox

user_data = {}
info_window = None

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        #User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            faculty = faculty_combobox.get()
            matric = matric_no_entry.get()

            #Course info
            registration_status = reg_status_var.get()
            current_cgpa = cgpa_entry.get()
            numsemesters = numsemesters_spinbox.get()

            #Update dictionary with user data
            user_data['firstname'] = firstname
            user_data['lastname'] = lastname
            user_data['title'] = title
            user_data['age'] = age
            user_data['faculty'] = faculty
            user_data['matric'] = matric
            user_data['cgpa'] = current_cgpa
            user_data['numsemesters'] = numsemesters
            user_data['registration_status'] = registration_status

            if registration_status == "Not Registered":
                # Display error message if registration status is not selected
                messagebox.showerror('Error', 'Registration Status is required.')

            else:
                print("First name:", firstname, "Lastname:", lastname)
                print("Title:", title, "Age:", age, "Faculty:", faculty, "Matric:", matric)
                print("Current CGPA:", current_cgpa, "Current Semesters:", numsemesters)
                print("Registration status:", registration_status)
                print("------------------------------------------")
                
                #Display success message box
                messagebox.showinfo('Message', 'Registration Successful!')
                display_registration_info(firstname, lastname, title, age, faculty, matric, current_cgpa, numsemesters, registration_status)
        else:
            #Display error message box if first name or last name is empty
            messagebox.showerror('Error', 'First name and Last name are required.')
    else:
        # Display error message box if terms are not accepted
        messagebox.showerror('Error', 'Registration Not Successful! Terms and conditions not accepted.')

def display_registration_info(firstname, lastname, title, age, faculty, matric_no, current_cgpa, numsemesters, registration_status):
    info_window = tkinter.Toplevel(window)
    info_window.title("Registration Information")

    info_label = tkinter.Label(info_window, text="Registration Information", font=("Helvetica", 16, "bold"))
    info_label.pack(pady=10)

    info_text = f"Name: {title} {firstname} {lastname}\n"
    info_text += f"Age: {age}\n"
    info_text += f"Faculty: {faculty}\n"
    info_text += f"Matric No: {matric_no}\n"
    info_text += f"Current CGPA: {current_cgpa}\n"
    info_text += f"Current Semesters: {numsemesters}\n"
    info_text += f"Registration Status: {registration_status}\n"

    info_display = tkinter.Label(info_window, text=info_text)
    info_display.pack(pady=10)

def edit_data():
    edit_window = tkinter.Toplevel(window)
    edit_window.title("Edit Data")

    entry_widgets = {}
    for key, value in user_data.items():
        label = tkinter.Label(edit_window, text=key.capitalize())
        label.grid(row=len(entry_widgets), column=0)

        entry = tkinter.Entry(edit_window)
        entry.insert(0, value)
        entry.grid(row=len(entry_widgets), column=1)

        entry_widgets[key] = entry
    
    save_button = tkinter.Button(edit_window, text="Save Changes", command=lambda: save_changes(entry_widgets, edit_window))
    save_button.grid(row=len(entry_widgets) + 1, column=0, columnspan=2)

def save_changes(entry_widgets, edit_window):
    for key, entry in entry_widgets.items():
        user_data[key] = entry.get()
    
    edit_window.destroy()

window = tkinter.Tk()
window.title("Volunteeer Registration Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column= 0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Titles")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=26)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

faculty_label = tkinter.Label(user_info_frame, text="Faculty")
faculty_combobox = ttk.Combobox(user_info_frame, values=["Administration and Policies", "Business and Management", "Accountacy", "Information Management", "Comp Science and Maths"])
faculty_label.grid(row=2, column=1)
faculty_combobox.grid(row=3, column=1)

matric_no = tkinter.Label(user_info_frame, text="Matric No")
matric_no.grid(row=2, column=2)
matric_no_entry = tkinter.Entry(user_info_frame)
matric_no_entry.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                        variable=reg_status_var, onvalue="Registered" , offvalue="Not Registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

cgpa_label = tkinter.Label(courses_frame, text= "Current CGPA")
cgpa_entry = tkinter.Entry(courses_frame)
cgpa_label.grid(row=0, column=1)
cgpa_entry.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text= "Current Semester")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=8)
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Button
button = tkinter.Button(frame, text="Submit Form", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

#Button to edit data
edit_button = tkinter.Button(info_window, text="Edit Data",command=edit_data)
edit_button.pack(pady=10)

window.mainloop()