def printinfo(arg1, *vartuple):
   # This is a test
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return

# Call the function with a single argument
printinfo(10)
# Call the function with multiple arguments
printinfo(70, 60, 50)
