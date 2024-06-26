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
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header or use next(csv_reader, None) if your CSV has a header
        next(csv_reader)  # Skip the header row
        for line in csv_reader:
            # Check if the current line matches the input credentials
            if line[2] == firstname and line[1] == surname and line[3] == department:
                # Collect the credentials of other employees
                other_employees = "Other employees' credentials:\n"
                for other_line in csv_reader:
                    # Ensure not to print the credentials of the current user
                    if other_line[2] != firstname or other_line[1] != surname or other_line[3] != department:
                        other_employees += f"Serial Number: {other_line[0]}, Surname: {other_line[1]}, Firstname: {other_line[2]}, Department: {other_line[3]}\n"
                return other_employees
        return "Invalid credentials."
    
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