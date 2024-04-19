# employee = ('Jane', 22, 'Engineer')
# new_employee = list(employee)
# new_employee[1] = 23
# employee = tuple(new_employee)
# print(employee)
# for i in range(2, len(arr)):
#     temp = arr[i]
#     arr.remove(arr[i])
#     arr.insert(i -2, temp)
# #3
# user_range = int(input("range: "))
# arr=[1,1]
# def printList(arr):
#     result = "Fibonacci number(s):"
#     for item in arr:
#         result += str(item)+""
#     return result

# if user_range<3:
#     print(arr[:user_range])
# else:
#     c(len(arr),user_range):
#         new_item = arr[i-1]+ arr[i-2]
#         arr,insert(i,new_item)
#     print(printList(arr))
#4-------------------------------
num_of_item = int(input("number of item in menu :"))
menu = []
for i in range(num_of_item):
    name = float(input(f" name of item ",{i}))
    price = float(input(f" price of item ",{i}))
    menu.append((name,price))
def avgPrice(arr):
    my_sum=0
    for i in arr:
        sum+=i[1]
    return round((my_sum/num_of_item)*100)/100

avg = avgPrice(menu)
print("Average price:", avg)
result = "Item(s) above average price: "
for i in menu:
    if i[1] > avg:
        result += str(i) + ", "

print(result)
#5-------------------------------------------
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
unique_words = []

for i in range(len(words)):
    if not words[i] in unique_words:
        unique_words.append(words[i])

print(len(unique_words))




