def swap(x, y):
    global a
    a = "Lawal"
    x, y = y, x
    b = "Chris"
    b = "Edward"
    c = "Lola"
    print(a, b, x, y)
    a = "Mary"

# Call the swap function with arguments "Tina" and "Tolu"
swap("Tina", "Tolu")

# Print the value of 'a' after the function call
print(a)
