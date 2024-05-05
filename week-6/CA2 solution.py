# GUI module importation
import tkinter as tk
from tkinter import messagebox
# SD stands for side dishes
# SS sttands for soups and swallow
# Beverages stands for beverages
# P stands for protein
# Rp stands for rice and pasta
#menu dictionaries
#The picture of the menu is blurry so prices and names may be wrong
RP_Dictionary = {'Jollof Rice': 350,'Coconut Fried Rice': 350,'Jollof Spaghetti' : 350}
P_Dictionary = {'Sweet chili chicken': 700, 'Grilled Chicken wings': 400, 'Fried Beef': 400, 'Fried Fish': 500, 'Boiled Egg': 200, 'Sauteed Sausages': 200}
SD_Dictionary = {'Savoury Beans': 350,'Roasted sweet potatoes': 300,'Fried plantains': 150, 'Mixed Vegetable salad': 150, 'Boiled yam': 150}
SS_Dictionary = {'Eba': 100, 'Pounded Yam': 100, 'Semo': 100, 'Atama Soup': 450, 'Egusi Soup':450}
Beverages_Dictionary = {'Water': 200,'Glass drink':750, 'PET Drink(35cl)':300,' PET Drink(50cl)':350, 'Glass/canned Malt': 500, 'Fresh Yo': 600, 'Pineapple Juice': 350, 'Mango Juice':350,'Zobo drink': 350}
#Function definitions
# Function to determine the correct dictionary
def get_menu_dictionary(item_name):
    if item_name in RP_Dictionary:
        return RP_Dictionary
    elif item_name in P_Dictionary:
        return P_Dictionary
    elif item_name in SD_Dictionary:
        return SD_Dictionary
    elif item_name in SS_Dictionary:
        return SS_Dictionary
    elif item_name in Beverages_Dictionary:
        return Beverages_Dictionary
    else:
        messagebox.showerror("Error", "Selected item not found in any menu.")
        return None
#Function to display the final price
def display_checkout(quantity, item_name):
    total = total_price(quantity, item_name)
    subtotal1 = total - (total * 0.10)
    subtotal2 = total - (total * 0.15)
    subtotal3 = total - (total * 0.25)
    window = tk.Toplevel(root)
    window.title("total price")
    window.geometry("300x300")
    #Quantity label and entry section
    Quantity_Label = tk.Label(window, text = f"Your subtotal price is {total}", font = ("Bahnschrift light", 10))
    Quantity_Label.pack()
    if total < 2500:
        disc1 = tk.Label(window, text = "With a 10 percent discount", font = ("Bahnschrift light",10))
        disc1.pack()
        disc1 = tk.Label(window, text = f"final price is {subtotal1} ", font = ("Bahnschrift light",10))
        disc1.pack()
    elif total > 2500 and total < 5000:
        disc1 = tk.Label(window, text = "With a 15 percent discount", font = ("Bahnschrift light",10))
        disc1.pack()
        disc1 = tk.Label(window, text = f"final price is {subtotal2} ", font = ("Bahnschrift light",10))
        disc1.pack() 
    elif total > 5000:
        disc1 = tk.Label(window, text = "With a 25 percent discount", font = ("Bahnschrift light",10))
        disc1.pack()
        disc1 = tk.Label(window, text = f"final price is {subtotal3} ", font = ("Bahnschrift light",10))
        disc1.pack() 
    elif total < 1000:
        disc1 = tk.Label(window, text = "With a no discount", font = ("Bahnschrift light",10))
        disc1.pack()
        disc1 = tk.Label(window, text = f"final price is {total} ", font = ("Bahnschrift light",10))
        disc1.pack()        
    else:
        messagebox.showerror("Something went wrong", "for further help see https://www.youtube.com/watch?v=dQw4w9WgXcQ")        
    order_label = tk.Label(window, text= "Would you like to make another order")
    order_label.pack()
    Submit_button= tk.Button(window,text = "yes", font = ("Bahnschrift light",10), command=root.mainloop)
    Submit_button.pack()
def total_price(quantity, item_name):
    menu_dictionary = get_menu_dictionary(item_name)
    if menu_dictionary is not None:
        return quantity * menu_dictionary[item_name]
    else:
        return 0
#Purchase button was messing me up. Kept dissapearing and stuff so introduced this function to fix the issue. Its called by the submit button
def purchase_button_click(quantity_str):
    #Strip() acts like trim() in rust.Removes trailing whitespace
    if quantity_str.strip():
        #Error handling
        try:
            quantity = int(quantity_str)
            item_name = selection.get()  # Get the selected item's name
            display_checkout(quantity, item_name)  # Pass the item's name to display_checkout
        except ValueError:
        #in the case that any quantity is entered that cant be converted to string
            messagebox.showerror("Error", "Please enter a valid quantity.")
    #In the case nothing is entered
    else:
        messagebox.showerror("Error", "Please enter a quantity.")
def proceed_RP():
    name = Name_Entry.get()
    window = tk.Toplevel(root)
    window.title("Checkout window")
    window.geometry("300x300")
    global selection
    selection = tk.StringVar(window)
    selection.set("Jollof Rice")
    Selected_item_label = tk.Label(window, text = f"Hello {name} please select an item", font = ("Bahnschrift light", 10))
    Selected_item_label.pack()
    Selected_item_options = tk.OptionMenu(window,selection,*RP_Dictionary.keys())
    Selected_item_options.pack()
    #Quantity label and entry section
    Quantity_Label = tk.Label(window, text = "Quantity entry", font = ("Bahnschrift light", 10))
    Quantity_Label.pack()
    global Quantity_Entry
    Quantity_Entry = tk.Entry(window, font = ("Bahnschrift light", 10))
    Quantity_Entry.pack()
    #Submit button label and button
    #unfortunately the command= at the end was originally just a call to the display function for checkout however it kept messing messing me up so i just created a new function that blah blah blah blah I'm tired of commenting abege
    Submit_button= tk.Button(window,text = "Purchase", font = ("Bahnschrift light",10), command=lambda: purchase_button_click(Quantity_Entry.get()))
    Submit_button.pack()
    #run the func
    root.mainloop()
#this function block is for if the decider function block calls protein
def proceed_P():
    name = Name_Entry.get()
    window = tk.Toplevel(root)
    window.title("Checkout window")
    window.geometry("300x300")
    global selection
    selection = tk.StringVar(window)
    selection.set("Sweet chili chicken")
    Selected_item_label = tk.Label(window, text = f"Hello {name} please select an item", font = ("Bahnschrift light", 10))
    Selected_item_label.pack()
    Selected_item_options = tk.OptionMenu(window,selection,*P_Dictionary.keys())
    Selected_item_options.pack()
    #Quantity label and entry section
    Quantity_Label = tk.Label(window, text = "Quantity entry", font = ("Bahnschrift light", 10))
    Quantity_Label.pack()
    global Quantity_Entry
    Quantity_Entry = tk.Entry(window, font = ("Bahnschrift light", 10))
    Quantity_Entry.pack()
    #Submit button label and button
    Submit_button= tk.Button(window,text = "Purchase", font = ("Bahnschrift light",10), command=lambda: purchase_button_click(Quantity_Entry.get()))
    Submit_button.pack()
#this function block is for if the decider function block calls side dishes
def proceed_SD():
    name = Name_Entry.get()
    window = tk.Toplevel(root)
    window.title("Checkout window")
    window.geometry("300x300")
    global selection
    selection = tk.StringVar(window)
    selection.set("Boiled yam")
    Selected_item_label = tk.Label(window, text = f"Hello {name} please select an item", font = ("Bahnschrift light", 10))
    Selected_item_label.pack()
    Selected_item_options = tk.OptionMenu(window,selection,*SD_Dictionary.keys())
    Selected_item_options.pack()
    #Quantity label and entry section
    Quantity_Label = tk.Label(window, text = "Quantity entry", font = ("Bahnschrift light", 10))
    Quantity_Label.pack()
    global Quantity_Entry
    Quantity_Entry = tk.Entry(window, font = ("Bahnschrift light", 10))
    Quantity_Entry.pack()
    #Submit button label and button
    Submit_button= tk.Button(window,text = "Purchase", font = ("Bahnschrift light",10), command=lambda: purchase_button_click(Quantity_Entry.get()))
    Submit_button.pack()
#this function block is for if the decider function block calls soups and swallows
def proceed_SS():
    name = Name_Entry.get()
    window = tk.Toplevel(root)
    window.title("Checkout window")
    window.geometry("300x300")
    global selection
    selection = tk.StringVar(window)
    selection.set("Eba")
    Selected_item_label = tk.Label(window, text = f"Hello {name} please select an item", font = ("Bahnschrift light", 10))
    Selected_item_label.pack()
    Selected_item_options = tk.OptionMenu(window,selection,*SS_Dictionary.keys())
    Selected_item_options.pack()
    #Quantity label and entry section
    Quantity_Label = tk.Label(window, text = "Quantity entry", font = ("Bahnschrift light", 10))
    Quantity_Label.pack()
    global Quantity_Entry
    Quantity_Entry = tk.Entry(window, font = ("Bahnschrift light", 10))
    Quantity_Entry.pack()
    #Submit button label and button
    Submit_button= tk.Button(window,text = "Purchase", font = ("Bahnschrift light",10), command=lambda: purchase_button_click(Quantity_Entry.get()))
    Submit_button.pack()
#this function block is for if the decider function block calls beverages
def proceed_Beverages():
    name = Name_Entry.get()
    window = tk.Toplevel(root)
    window.title("Checkout window")
    window.geometry("300x300")
    global selection
    selection = tk.StringVar(window)
    selection.set("Water")
    Selected_item_label = tk.Label(window, text = f"Hello {name} please select an item", font = ("Bahnschrift light", 10))
    Selected_item_label.pack()
    Selected_item_options = tk.OptionMenu(window,selection,*Beverages_Dictionary.keys())
    Selected_item_options.pack()
    #Quantity label and entry section
    Quantity_Label = tk.Label(window, text = "Quantity entry", font = ("Bahnschrift light", 10))
    Quantity_Label.pack()
    global Quantity_Entry
    Quantity_Entry = tk.Entry(window, font = ("Bahnschrift light", 10))
    Quantity_Entry.pack()
    #Submit button label and button
    Submit_button= tk.Button(window,text = "Purchase", font = ("Bahnschrift light",10), command=lambda: purchase_button_click(Quantity_Entry.get()))
    Submit_button.pack()
#depending on what the user chooses sha it calls from a variety of functions that display different menu options from separate menus depending on input sha
def decider():
    Menu_option = menu_selected.get()
    if  Menu_option == "RICE/PASTA":
        proceed_RP()
    elif  Menu_option == "PROTEINS":
        proceed_P()
    elif Menu_option == "SIDE DISHES":
        proceed_SD()
    elif Menu_option == "SOUPS & SWALLOWS":
        proceed_SS()
    elif Menu_option == "BEVERAGES":
        proceed_Beverages()
    else:
        messagebox.showerror("Error", "Entry read faliure. See https://www.youtube.com/watch?v=dQw4w9WgXcQ for further help")
#Main root initialization window
root = tk.Tk()
root.title("Pau cafeteria")
root.geometry("400x300")

#Label and entry declaration
#Name label and entry
Name_Label = tk.Label(root, text = "Input name", font = ("Bahnschrift light", 10))
Name_Label.pack()
Name_Entry = tk.Entry(root, font = ("Bahnschrift light", 10))
Name_Entry.pack()
#Menu label declaration and option declaration
#Menu variable declaration
menu_selected = tk.StringVar(root)
menu_selected.set("RICE/PASTA")
#Menu label and option
Menu_Label = tk.Label(root, text = "Menu choice", font = ("Bahnschrift light", 10))
Menu_Label.pack()
Menu_op = tk.OptionMenu(root,menu_selected,"RICE/PASTA","PROTEINS","SIDE DISHES", "SOUPS & SWALLOWS", "BEVERAGES")
Menu_op.pack()
#Submit button 
Submit_button= tk.Button(root,text = "Proceed", font = ("Bahnschrift light",10), command=decider)
Submit_button.pack()
#program GUI execution
root.mainloop()
#Drop down menus are just easier to manage tbh
# Being very real with whoever is reading this sha. I know this program can be like 80 lines and there are probably a lot of redundancies sha
#I am very aware that proceed_RP and proceed_p and all those functions are probably redundant and i could probably just pass the menu as an argument to those functions or something like that sha but look. I have two tests incoming
#one on friday one on thursday so i just dont havee time to figure out how to do that
#Im just brute forcing this program into working so please pity me. Im just putting global anywhere I can see to even get this program to work so please have mercy
