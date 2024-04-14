# Python program to swap 2 cities

#To take inputs from the user
city_1 = input('Enter the name of City 1:')
city_2 = input('Enter name of City 2: ')

#create a temporary variable to swap the cities
temp = city_1
city_1 = city_2
city_2 = temp

print(f"The name of City 1 after swapping is {city_1}")
print(f"The name of City 1 after swapping is {city_2}")