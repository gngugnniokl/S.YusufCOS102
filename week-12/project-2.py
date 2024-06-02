import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# Define the base class for External Vendors
class External_Vendors(ABC):
    @abstractmethod
    def menu(self):
        pass

# Define subclasses for each vendor
class CooperativeCafeteria(External_Vendors):
    def menu(self):
        return {
            "Jollof Rice and Stew": 200,
            "White Rice and Stew": 200,
            "Fried Rice": 200,
            "Salad": 100,
            "Plantain": 100
        }

class FaithHostelCafeteria(External_Vendors):
    def menu(self):
        return {
            "Fried Rice": 400,
            "White Rice and Stew": 400,
            "Beans": 200,
            "Chicken": 1000
        }

class StudentCentreCafeteria(External_Vendors):
    def menu(self):
        return {
            "Chicken Fried Rice": 800,
            "Pomo Sauce": 300,
            "Spaghetti Jollof": 500,
            "Amala/Ewedu": 500,
            "Semo with Eforiro Soup": 500
        }

# Create the main application window
root = tk.Tk()
root.title("PAU External Food Vendors Management")

# Function to display menu for selected vendor
def display_menu(vendor_instance):
    menu_items = vendor_instance.menu()
    menu_text = "\n".join(f"{meal}: ₦{price}" for meal, price in menu_items.items())
    messagebox.showinfo(f"{vendor_instance.__class__.__name__} Menu", menu_text)

# Add buttons for each vendor
cooperative_button = tk.Button(root, text="Cooperative Cafeteria", command=lambda: display_menu(CooperativeCafeteria()))
cooperative_button.pack()

faith_button = tk.Button(root, text="Faith Hostel Cafeteria", command=lambda: display_menu(FaithHostelCafeteria()))
faith_button.pack()

student_button = tk.Button(root, text="Student Centre Cafeteria", command=lambda: display_menu(StudentCentreCafeteria()))
student_button.pack()

# Run the application
root.mainloop()
