import tkinter as tk
from tkinter import messagebox

# Function to check admission criteria
def check_admission(jamb_score, credits, department, interview_passed):
    if department == "Computer Science" and jamb_score >= 250 and credits >= 5 and interview_passed:
        return True
    elif department == "Mass Communication" and jamb_score >= 230 and credits >= 5 and interview_passed:
        return True
    return False

# Function to submit the form
def submit_form():
    name = name_entry.get()
    jamb_score = int(jamb_score_entry.get())
    credits = int(credits_entry.get())
    department = department_var.get()
    interview_passed = interview_var.get() == 1

    if check_admission(jamb_score, credits, department, interview_passed):
        admitted.append(name)
        messagebox.showinfo("Admission Status", f"{name} has been admitted into {department} Department.")
    else:
        not_admitted.append(name)
        messagebox.showerror("Admission Status", f"{name} has not been admitted.")

# Main window
root = tk.Tk()
root.title("Admission Automation")
root.geometry("400x300")

# Variables
admitted = []
not_admitted = []
department_var = tk.StringVar()
interview_var = tk.IntVar()

# Name
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# JAMB Score
tk.Label(root, text="JAMB Score:").pack()
jamb_score_entry = tk.Entry(root)
jamb_score_entry.pack()

# Credits
tk.Label(root, text="Credits:").pack()
credits_entry = tk.Entry(root)
credits_entry.pack()

# Department
tk.Label(root, text="Department:").pack()
tk.Radiobutton(root, text="Computer Science", variable=department_var, value="Computer Science").pack()
tk.Radiobutton(root, text="Mass Communication", variable=department_var, value="Mass Communication").pack()

# Interview Passed
tk.Label(root, text="Interview Passed:").pack()
tk.Checkbutton(root, text="Yes", variable=interview_var).pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the application
root.mainloop()
