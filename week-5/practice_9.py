total = 50  # This is a global variable.

# Function to add two numbers and print the local total
def sum(arg1, arg2):
   # Add both the parameters and assign to local total
   total = arg1 + arg2
   print("Inside the function local total: ", total)
   return total

# Now you can call the sum function
sum(10, 20)

# Print the global total outside the function
print("Outside the function global total: ", total)
