import tkinter as tk
from tkinter import messagebox
def fivek():
    window = tk.Toplevel(root)
    window.geometry("300x300")
    window.title("Retail price")
    #Window label
    Notif = tk.Label(window,text = "Your total fee is 5000")
    Notif.pack()
    window.mainloop()
def threefiv():
    window = tk.Toplevel(root)
    window.geometry("300x300")
    window.title("Retail price")
    #Window label
    Notif = tk.Label(window,text = "Your total fee is 3500")
    Notif.pack()
    window.mainloop()
def tenk():
    window = tk.Toplevel(root)
    window.geometry("300x300")
    window.title("Retail price")
    #Window label
    Notif = tk.Label(window,text = "Your total fee is 10000")
    Notif.pack()
    window.mainloop()
def conditionals():
    Package_weight = int(Package_weight_Entry.get())
    Location = Location_Entry.get()
    if Package_weight >= 10 and Location == "Ibeju-Lekki":
        fivek()
    elif Package_weight < 10 and Location == "Ibeju-Lekki":
        threefiv()
    elif Package_weight >= 10 and Location == "Epe" : 
        tenk()
    elif Package_weight < 10 and Location == "Epe":
        fivek()
    else:
        messagebox.showerror("Error", "Error in text entered")
root = tk.Tk()
root.title("Simi services")
root.geometry("300x300")
#Package weight
Package_weight_label = tk.Label(root,text = "Hello please input the package weight")
Package_weight_label.pack()
Package_weight_Entry = tk.Entry(root)
Package_weight_Entry.pack()
#Location
Location_label = tk.Label(root,text = "Hello please input location")
Location_label.pack()
Location_Entry = tk.Entry(root)
Location_Entry.pack()
#Button
submit_button = tk.Button(root, text = "Submit",command=conditionals)
submit_button.pack()
root.mainloop()