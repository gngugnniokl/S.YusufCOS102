#task Write a program to solve a quartic and cubic equation
#Module importation1
import math
#function definition
def cubic(a,b,c,d):
    discriminant = (b ** 2) - (3 * a * c)
    delta = (2 * b ** 3) - (9 * a * b * c) + (27 * (a ** 2) * d)
    d0 = delta + (delta ** 2 - 4 * discriminant ** 3) ** 0.5
    d1 = delta - (delta ** 2 - 4 * discriminant ** 3) ** 0.5
    C = ((d0 + d1) / 2) ** (1 / 3)
    if C == 0:
        root1 = -b / (3 * a)
        root2 = root3 = -(b + C) / (3 * a)
    else:
        root1 = -(b + C + discriminant / C) / (3 * a)
        root2 = -(b + (1 + 1j * math.sqrt(3)) * C + discriminant / ((1 + 1j * math.sqrt(3)) * C)) / (3 * a)
        root3 = -(b + (1 - 1j * math.sqrt(3)) * C + discriminant / ((1 - 1j * math.sqrt(3)) * C)) / (3 * a)
    return root1, root2, root3

def quartic(a,b,c,d,e):
    roots = []
    for i in range(-10000, 10000):
        definer = (a * pow(i, 3)) + (b * pow(i, 2)) + (c * pow(i, 1)) + d
        if definer == 0:
            root_1 = i
            root_2 = root_3 = root_4 = None  # Placeholder for additional roots
            roots.append((root_1, root_2, root_3, root_4))
    return roots
#program execution and prompting
name = input("Hello what is your name?")
print(f"Hello {name}, Would you like to find the roots of a (1)cubic or (2)quartic equation?")
user_choice = int(input("Select option 1 for cubic and option 2 for quartic:"))
if user_choice == 1:
    a = float(input("Enter the coefficient of your first term:"))
    b = float(input("Enter the coefficient of your second term:"))
    c = float(input("Enter the coefficient of your third term:"))
    d = float(input("Enter your last term"))
    roots = cubic(a, b, c, d)
    print("Roots of the cubic equation:", roots)
elif user_choice ==2:
    a = float(input("Enter the coefficient of your first term:"))
    b = float(input("Enter the coefficient of your second term:"))
    c = float(input("Enter the coefficient of your third term:"))
    d = float(input("Enter the coefficient of your fourth term:"))
    e = float(input("Enter your last term:"))
    roots = quartic(a, b, c, d, e)
    print("Roots of the quartic equation:", roots)

    