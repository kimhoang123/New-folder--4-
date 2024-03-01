# print string has multi lines
s = 'there are\nmulti\nlines'
print(s)

s1="""this is
    multi
line"""
print(s1)
#operator fot str
x = input("type a number :")
print('you have' + x + 'bestfiends')
print(f'you have {x} bestfiends')
a="abc"
print(a*6)
#string methods
name = input("Your name: ")
print(len(name))
print(name.find("D"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.count("d"))
print(name.replace("d", "b"))
print(name.isalpha())
#
name = " Thien kim"
first_name = name[name.find("e"):4]
first_name = name[:4]
print(first_name)

last_name = name[name.find("m"):]
print(last_name)

reserve_name = name[::-1]
# doi vi tri cua ten thien kim => mik nieht
print(reserve_name)
#math func
import math
print(round(a))# lam tron
print(math.ceil(a))#lam tron len
print(math.floor(a))#lam tron xuong
print(math.sqrt(12))#can bac 2
#multiple assignment
x = y = z 20
h,j,k ="as23","44rr"
print(h)