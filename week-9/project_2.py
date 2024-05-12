import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#something something something inherritance from the tk class
class Main_application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Delivery_service_00789")
        self.geometry("400x400")
        #Package weight Label and entry creation 
        self.package_weight_label = ttk.Label(self,text = "Package weight", font = ("Bahnschrift light", 12))
        self.package_weight_label.pack()
        self.package_weight_entry = ttk.Entry(self,font = ("Bahnschrift light", 12))
        self.package_weight_entry.pack()
        #Package location label and entry creation
        self.Selected_Location = tk.StringVar(self)
        self.Selected_Location.set("Pau")
        self.package_location_label = ttk.Label(self,text = "Package location options", font = ("Bahnschrift light", 12))
        self.package_location_label.pack()
        self.op_menu = tk.OptionMenu(self,self.Selected_Location,"Pau","Epe")
        self.op_menu.pack()
        #button
        self.Submit_button= tk.Button(self,text = "Proceed", font = ("Bahnschrift light",10), command=self.Order)
        self.Submit_button.pack()
    def twook(self):
        window = tk.Toplevel(self)
        window.geometry("300x300")
        window.title("Retail price")
        Notif = tk.Label(window, text="Your total fee is 2000")
        Notif.pack()
        window.mainloop()

    def threefiv(self):
        window = tk.Toplevel(self)
        window.geometry("300x300")
        window.title("Retail price")
        Notif = tk.Label(window, text="Your total fee is 1500")
        Notif.pack()
        window.mainloop()

    def tenk(self):
        window = tk.Toplevel(self)
        window.geometry("300x300")
        window.title("Retail price")
        Notif = tk.Label(window, text="Your total fee is 5000")
        Notif.pack()
        window.mainloop()
    def fivek(self):
        window = tk.Toplevel(self)
        window.geometry("300x300")
        window.title("Retail price")
        Notif = tk.Label(window, text="Your total fee is 4000")
        Notif.pack()
        window.mainloop()
    def Order(self):
        Package_weight = int(self.package_weight_entry.get())
        Location = self.Selected_Location.get()
        if Package_weight >= 10 and Location == "Pau":
            self.twook()
        elif Package_weight < 10 and Location == "Pau":
            self.threefiv()
        elif Package_weight >= 10 and Location == "Epe" : 
            self.tenk()
        elif Package_weight < 10 and Location == "Epe":
            self.fivek()
        else:
            messagebox.showerror("Error", "Error in text entered")
#program actually runs here
application = Main_application()
application.mainloop()