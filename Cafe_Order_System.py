menu = {
    'Pizza': 100,
    'Burger': 50,
    'Pasta': 90,
    'Maggi': 25,
    'Sandwich': 45,
    'Coffee': 40,
    'Tea': 20,
    'Pop': 20
}
print("Welcome to our cafe ")
print("Please see our menu for order")
print("Food\nPizza: Rs 100\nPasta: Rs 50\nBurger: Rs 90\nMaggi: Rs25\nSandwich: Rs45\nBeverage\nCoffee: Rs 40\nTea: Rs20\nPop: Rs20")
Totalorder = 0
item1 = input("What would you like to order? ")
if item1 in menu:
    Totalorder += menu[item1]
else:
    print("Sorry, we don't have that item\nEnter from the menu")
print("Your total order is:", Totalorder)
while True:
    option = input("Do you want to add anything else? yes/no ")
    if option == "yes":
       item2 = input("What would you like to add? ")
       if item2 in menu:
           Totalorder += menu[item2]
           print("Your total is: ", Totalorder)
           print("Thanks for ordering!")
       else:
           print("Sorry, we don't have that item\nEnter from the menu")
    elif option == "no":
           print("Your total is: ", Totalorder)
           print("Thanks for ordering!")
           break#





