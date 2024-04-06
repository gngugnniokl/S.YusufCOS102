def Tabular_form(Name,Age,Height,Score):
    print("| {:<14} | {:<14} | {:<14} |   {:<14} |".format(Name,Age,Height,Score,))
#Actual program execution
records = []
Num_people = int(input("How many people will be using this program?"))
for  i in range (Num_people):
    print("Input the data of the " + str((i+1)) + " person: ")
    Name = input("What is their name?")
    Age = int(input("What is their height?"))
    Height = float(input("What is their age?"))
    Score = float(input("What is their score?"))
    records.append((Name,Age,Height,Score))
print("|      Name      |        Age     |      Height    |        Score     |")
for record in records:
    Tabular_form(*record)


    
                  