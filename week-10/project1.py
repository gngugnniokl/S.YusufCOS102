import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class zenith(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zenith application")
        self.geometry("300x300")
        self.Name_label = ttk.Label(self,text = "Name", font = ("Bahnschrift light", 12))
        self.Name_label.pack()
        self.Name_entry = ttk.Entry(self,font = ("Bahnschrift light", 12))
        self.Name_entry.pack()
        #department option menu and label
        self.department_label = ttk.Label(self,text = "Division", font = ("Bahnschrift light", 12))
        self.department_label.pack()
        self.Selected_department = tk.StringVar(self)
        self.Selected_department.set("Retail Banking")
        self.op_menu = tk.OptionMenu(self,self.Selected_department,"Retail Banking","Commercial Banking", "Global Banking")
        self.op_menu.pack()
        #button
        self.Submit_button= tk.Button(self,text = "Proceed", font = ("Bahnschrift light",10), command=self.window_call)
        self.Submit_button.pack()
    def window_call(self):
        if self.Selected_department.get() == "Retail Banking":
            Case1_run = Retail_banking()
            Case1_run.unique_services()
            Case1_run.mutual_services()
        elif self.Selected_department.get() == "Global Banking":
            Case2_run = global_banking()
            Case2_run.unique_services()
            Case2_run.mutual_services()  
        elif self.Selected_department.get() == "Commercial Banking":
            Case1_run = commercial_banking()
            Case1_run.unique_services()
            Case1_run.mutual_services()
        else:
            messagebox.showerror("Idk man","Something went wrong")
    def unique_services(self):
        pass
    def mutual_services(self):
        pass
    
class Retail_banking(zenith):
    def unique_services(self):
        window = tk.Toplevel(self)
        window.title("retail banking unique services")
        window.geometry("300x300")
        task1 = ttk.Label(window,text = "Retirement and education accounts", font = ("Bahnschrift light", 12))
        task1.pack()
        task2 = ttk.Label(window,text = "Loans and mortgages", font = ("Bahnschrift light", 12))
        task2.pack()
        task3 = ttk.Label(window,text = "Checks and savings", font = ("Bahnschrift light", 12))
        task3.pack()
    def mutual_services(self):
        window = tk.Toplevel(self)
        window.title("mutual services")
        window.geometry("300x300")
        name = self.Name_entry.get()
        intro = ttk.Label(window, text = f"Hello {name} your services are", font = ("Bahnschrift light", 12))
        intro.pack()
        task1 = ttk.Label(window,text = "Lines of credit", font = ("Bahnschrift light", 12))
        task1.pack()
        task2 = ttk.Label(window,text = "investment management and accounts", font = ("Bahnschrift light", 12))
        task2.pack()
        task3 = ttk.Label(window,text = "insurance", font = ("Bahnschrift light", 12))
        task3.pack()
class global_banking(zenith):
    def unique_services(self):
        window = tk.Toplevel(self)
        window.title("retail banking unique services")
        window.geometry("300x300")
        task1 = ttk.Label(window,text = "Retirement and education accounts", font = ("Bahnschrift light", 12))
        task1.pack()
        task2 = ttk.Label(window,text = "Loans and mortgages", font = ("Bahnschrift light", 12))
        task2.pack()
        task3 = ttk.Label(window,text = "Checks and savings", font = ("Bahnschrift light", 12))
        task3.pack()
class commercial_banking(zenith): 
    def unique_services(self):
        window = tk.Toplevel(self)
        window.title("retail banking unique services")
        window.geometry("300x300")
        task1 = ttk.Label(window,text = "Multi-currency management services and products", font = ("Bahnschrift light", 12))
        task1.pack()
        task2 = ttk.Label(window,text = "Foreign currency accounts", font = ("Bahnschrift light", 12))
        task2.pack()
        task3 = ttk.Label(window,text = "Foreign currency credit cards", font = ("Bahnschrift light", 12))
        task3.pack()
        task2 = ttk.Label(window,text = "Transborder advisory services", font = ("Bahnschrift light", 12))
        task2.pack()
        task3 = ttk.Label(window,text = "Liquidity management", font = ("Bahnschrift light", 12))
        task3.pack()
    def mutual_services(self):
        window = tk.Toplevel(self)
        window.title("retail banking mutual services")
        window.geometry("300x300")
        task1 = ttk.Label(window,text = "Advisory services", font = ("Bahnschrift light", 12))
        task1.pack()
app = zenith()
app.mainloop()
        