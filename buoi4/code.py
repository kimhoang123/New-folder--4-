# print("your input: ", end="")
# name = input()

# def my_uppercase(str):
#     distance = ord('A') - ord('a')
#     for ch in str:
#         if ch > 'a' and ch < 'z':
#             print(chr(ord(ch) + distance), end="")
#         else:
#             print(ch, end="")
# # for
# import random
# my_list = ["apple","orange","banana"]
# randommy_list = random.choices(my_lít, k= 2)
# print(randommy_list)
# for ind,item in enumerate(random_list,start=1):
#     print(f"{ind}.{item}")
# #
from turtle import *

n = 5
angle = 180 - 180 * (n - 2) / n
for edge in range(n):
    right(angle)
    forward(100)

mainloop()
