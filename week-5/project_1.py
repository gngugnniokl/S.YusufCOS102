import tkinter as tk
from tkinter import messagebox
import csv
def welcomeMessage(firstname, surname, department):
    validation_message = validation(firstname, surname, department)
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {firstname} {surname}\n")
    label_1.pack()
    label_2 = tk.Label(window, text=validation_message)
    label_2.pack()
def validation(firstname, surname, department):
    file_path = "C:/Users/ipinu/OneDrive/Documents/S.YusufCOS102/week-5/GIG-logistics.csv"
    all_employees = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for line in csv_reader:
            # Collect all employee credentials
            all_employees.append(line)
            # Check if the current line matches the input credentials
            if line[2] == firstname and line[1] == surname and line[3] == department:
                # Flag that the user's credentials are valid
                user_valid = True
                break
        else:
            # If no match was found, return invalid credentials message
            return "Invalid credentials."

    if user_valid:
        # Filter out the current user's credentials and prepare the string
        other_employees = "Other employees' credentials:\n"
        for employee in all_employees:
            if employee[2] != firstname or employee[1] != surname or employee[3] != department:
                other_employees += f"Serial Number: {employee[0]}, Surname: {employee[1]}, Firstname: {employee[2]}, Department: {employee[3]}\n"
        return other_employees

    
def submit():
    firstname = firstname_entry.get()
    surname = surname_entry.get()
    department = department_entry.get()
    if firstname and surname and department:
        welcomeMessage(firstname, surname, department)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")
        
root = tk.Tk()
root.title("GIG logistics login")
root.geometry("600x600")

#first name entry field
firstname_label = tk.Label(root, text="Firstname:")
firstname_label.pack()
firstname_entry = tk.Entry(root)
firstname_entry.pack()

#Surname entry field
surname_label = tk.Label(root, text="Surname:")
surname_label.pack()
surname_entry = tk.Entry(root)
surname_entry.pack()

#Department entry field
department_label = tk.Label(root, text="Department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()