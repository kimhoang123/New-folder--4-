# collection data types in PY :
# + List []: ordered , changeable ,allows duplicate members
# + Tuple (): ordered , unchangeable ,allows duplicate members
# + Set {}: unordered , unchangeable ( add , remove items) ,no duplicate members
# + dictionary {key : value}: ordered , changeable ,no duplicate members

# 1D list
food = ["sup cua","bun bo","tra dao"]
food = list(("sup cua","bun bo","tra dao"))
print(food)
print(type(food))
food[0] = "mi cay" #lay gtri tu vtri 
print(food)

#foreach
for item in food:
    print(item)

#for
for ind in range(len(food)):
    print(ind, end=" . ")
    print(food[ind])

# functions of list
food.append("mang cut")
food.remove("ca chien")
item = food.pop("ha cao")# lay cai cuoi roi xoa
print(item)
print(food)
food.insert(1,"banh canh cua")
food.sort()
food.clear()#xoa tca 

# 2D list------------------------
drinks = ["tra chanh","tra oi hong","tra dau"]
dessert = ["banh flan","kem"]

meal = [food,drinks,dessert]
print(meal[1][2])#item trong 1 list nho
print(meal[2])# in dessert list

# mutable & inmutable----------------
x = 

# clone list
list_clone = food.copy() # copy phan tu

#join 2 list
list1 = ["a",'b',7,True]
list2 = [1,4,1.7]
list3 = list1 + list2 # cach 1
list4 = list1.extend(list2) # cach 2