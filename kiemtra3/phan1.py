#1----------
def a(number):
    if number % 2 == 0 :
        return True
    else :
        return False
input_number= int(input("Input a number:"))
if a(input_number):
    print("This number is even")
else:
    print("This number is not even")
#2--------------
import math
def cal_area(radius):
    return math.pi * radius**2
input_radius = float(input("Input radius:"))
a = cal_area(input_radius)
print("Circle’s area:",a)
#3-------------------
c = input("Input a text:")
print("Reversed text:",c[::-1])
#4-------------------------
def palindrome(text):
    if len(text)<1:
        return True
    else :
        if text[0] == text[-1]:
            return palindrome(text[1:-1])
        else:
            return False
            
if(palindrome(text) == True):
    print("This is a palindrome.")   
else:
    print("This is not a palindrome.")
