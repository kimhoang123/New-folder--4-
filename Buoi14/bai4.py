print("== Welcome to MindX Restaurant ==")
food=[]
while True :
    order = input("Please choose a dish:")
    if order in food :
        print("You chose this already. Anything else? (y/n):")
    else :
       food.append(order)
       print("Great choice! Anything else? (y/n):")
    other = input("You chose this already. Anything else? (y/n):")
    if other !="y" :
        break
print("Well done! Your order:")
for order in food :
    print(f"-{food}")

