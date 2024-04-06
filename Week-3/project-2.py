for i in range(2500):
    Name = input("Hello, what is your name?")
    experience = int(input(f"Hello {Name}, how many years of experience do you have?"))
    age = int(input("What is your age?"))
    if  experience > 25 and age >=55:
        print("You have been awarded 5600000 naira in ATR")
    elif  experience > 20 and age >=45:
        print("You have been awarded 4480000 naira in ATR")
    elif  experience >= 10 and age >=35:
        print("You have been awarded 1500000 naira in ATR")
    elif  experience < 10 and age <35:
        print("You have been awarded 550000 naira in ATR")
    else:
        print("You messed up somewhere")
    
    

