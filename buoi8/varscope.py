x = 12 # global var 

def my_func ():
    global x
    x = 10 

print(x)
my_func()
print(x)

if 3<4:s
    a=10
    print(a)
else:
    print(1)
print(a)
print(x)

def square (w,h):
    global s #declare
    s = w * h

square(2,3)
print(s)