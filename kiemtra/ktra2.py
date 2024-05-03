#phan3
computer = {
    "HP": "600",
    "DELL": "650",
    "MACBOOK": "1200",
    "ASUS": "400",
}
print("Price of ASUS:",computer["ASUS"] )
input = input("Input a brand:")
if input in computer :
    print("Price of HP:",computer[input])
else :
    print("error")
#phan4-------------------
#b1
price = computer["ASUS"]*5
print(price)
#b2
input1 = (input("Input a brand:"))
input2 = int(input("Input amount to buy:"))
price1 = computer[input1]*input2
print("Total price:",price1)
#b3
update=input("Input a brand:")
buy = int(input("Input amount to buy:"))
computer[update]-=buy
print("Total price:",computer[update]*buy)
for brand,quantity in computer.items():
    print("-",brand,":",quantity)
#phan5------------------------------
Phần 5

print("Total value of available brands:")
for brand, quantity in computers.items():
    total_value = quantity * prices[brand]
    print("-", brand + ":", total_value)
a = sum(quantity * prices[brand] for brand, quantity in computers.items())
print("Total value of available items:", a)




