import tkinter as tk
from tkinter import messagebox
import random

class Employee:
    def __init__(self):
        self.employees = [
            "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
            "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones",
            "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"
        ]
        self.attendance = []

    def check_employee(self, name):
        if name in self.employees:
            return True
        else:
            return False

    def take_attendance(self, name):
        if name not in self.attendance:
            self.attendance.append(name)
            return True
        else:
            return False

    def assign_task(self, name):
        tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]
        task = random.choice(tasks)
        return f"Task assigned to {name}: {task}"

    def refuse_access(self):
        messagebox.showerror("Access Denied", "Employee not found in the system!")

#Employee attendance whatever is a subclass of the tk class due to inherritance.
class EmployeeAttendanceSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Attendance System")
        self.geometry("400x200")
        self.employee_manager = Employee()

        self.label = tk.Label(self, text="Enter your name:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.button.pack()

    def submit(self):
        name = self.entry.get().strip()
        if name:
            if self.employee_manager.check_employee(name):
                if self.employee_manager.take_attendance(name):
                    task_assigned = self.employee_manager.assign_task(name)
                    messagebox.showinfo("Attendance Taken", f"Welcome, {name}!\n{task_assigned}")
                else:
                    messagebox.showwarning("Already Attended", f"{name} has already attended for today.")
            else:
                self.employee_manager.refuse_access()
        else:
            messagebox.showwarning("Empty Field", "Please enter your name.")
app = EmployeeAttendanceSystem()
app.mainloop()
