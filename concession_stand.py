menu={
    "popcorn":2.50,
    "nachos":3.00,
    "pretzel":2.00,
    "fries":2.50,
    "drink":1.50,
    "candy":1.00
}

cart=[]
total=0

print("---MENU---")
for key , value in menu.items():
    print(f"{key:10} : ${value}")
print("-----------")

while True:
    food=input("Enter a food to buy: ")
    if food.lower()=='quit':
        break
    else:
        if food in menu:
            cart.append(food)
            total+=menu[food]
        else:
            print("Sorry, we don't have that item.")
print("Your cart:", cart)
print("Total: $", total) 
