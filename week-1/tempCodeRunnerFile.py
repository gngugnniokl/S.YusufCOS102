#Ok so like basically. Im importing this math module thing to handle stuff like exponents and crap
import math
#Defined functions
def simple_interest_calculation(P,R,T):
     return P * (1+ ((R/100)*T))
def compound_interest_calculation(P,R,n,t):
     return P * pow((1 + (R/n)),  n*t) 
def annuity_plan_calculation(P, M, T, R, n, t):
     return (P * M * T) * ((pow((1 + (R / n)), n*t) - 1)/(R / n))
#Program prompt
user_choice = input("Would you like to calculate (1)simple interest or (2)annuity plan or (3)compound interest?")
if user_choice == 1:
        P = int(input("Enter an your P"))
        R = float(input("Enter an your R"))  
        T = int(input("Enter an your T")) 
        simp = simple_interest_calculation(P,R,T)
        print("Your compound interest final calculation is ",simp)
elif user_choice == 2:
        P = int(input("Enter an your P"))
        M = int(input("Enter an your M"))
        T = int(input("Enter an your T"))
        R = float(input("Enter an your R")) 
        n = int(input("Enter an your n")) 
        t = int(input("Enter an your t"))   
        annuity = annuity_plan_calculation(P, M, T, R, n, t)
        print("Your annuity plan final calculation is ",annuity)
elif user_choice == 3:
        P = int(input("Enter an your P"))
        R = float(input("Enter an your R")) 
        n = int(input("Enter an your n")) 
        t = int(input("Enter an your t"))
        comp = compound_interest_calculation(P,R,n,t)
        print("Your compound interest final calculation is ",comp)