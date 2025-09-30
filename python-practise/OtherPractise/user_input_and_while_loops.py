print("Welcome to the Pizzaria.")
print("Please type 'done' when you've added your toppings.\n")
quit = ""
while quit != 'done':
    user_topping = input("Please enter the topping you would like: ")
    if user_topping != 'done':
        print(f"{user_topping} added!")
    quit = user_topping
    if quit == 'done':
        print("Your pizza will be ready in a few minutes!")

print("")
print("---------------------------------------------------------------------------------------------------------------------------\n")

print("Welcome to Savage Cinema.")
print("Please enter your age to see the ticket prices for your movie.")
active = True
while active:
    age = input("Enter age: ")
    age = int(age)
    if age <= 3:
        print("price: Free")
    elif age > 3 and age <= 12:
        print("price: $10")
    elif age > 12:
        print("price: $15")
    another = input("Would you like to see for another person('yes' or 'no'): ")
    if another == 'yes':
        True
    else:
        active = False

        print("Enjoy your movie!")     

print("")
print("---------------------------------------------------------------------------------------------------------------------------\n")

sandwich_orders = ['red leicester', 'cheddar cheese', 'chicken tikka', 'tuna', 'egg and mayo']

#code below adds 3 pastramis to the sandwich_orders list
for i in range(3):
    i = sandwich_orders.append('pastrami')

print(sandwich_orders) #to check if 'pastrami' is in there
print("The deli has run out of pastrami.")

#code below removes all occurences of pastrami from sandwich_orders list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders) #to check if 'pastrami' was removed

finished_sandwiches = []
for sandwich in sandwich_orders:
    made = (f"I made your {sandwich} sandwhich.")
    print(made)
    finished_sandwiches.append(sandwich)

print("")

for sandwiches in finished_sandwiches:
    print(f"A {sandwiches} sandwich was made.")

print("")
print("---------------------------------------------------------------------------------------------------------------------------\n")

responses = {}
active = True 
while active:
    name = input("Name: ")
    place = input("If you could visit one place in the world, where would you go?\n")
    
    responses[name] = place

    repeat = input("Would you like to let another person respond? ('yes' or 'no'): ")
    if repeat == 'no':
        active = False

print("\n---------- Poll results ----------")
for name, place in responses.items():
    print(f"{name.title()} would like to go to {place.capitalize()}.")
