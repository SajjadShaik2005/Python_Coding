foods=[]
prices=[]
total=0
while True:
    food=input("enter a food to buy:")
    if food.lower()=='quit':
        break
    else:
        price=float(input("enter the price of the food:"))
        foods.append(food)
        prices.append(price)
        
print("your shopping list:")
for food in foods:
    print(food, end=" ")
for price in prices:
    total+=price
    
print("\nyour total bill is: ",total)