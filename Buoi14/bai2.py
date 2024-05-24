import math
number1 = float(input("Input a:"))
number2 = float(input("Input b:"))
number3 = float(input("Input c:"))
denta = number1**2-4*number2*number3
if denta > 0 :
    x1 = (-number2-math.sqrt(denta))/((2*number1))
    x2 = (-number2+math.sqrt(denta))/((2*number1))
    print("The equation has 2 solutions:",f"x={x1} or x={x2}")
elif denta == 0 :
    x = -b/(2*a)
    print("The equation has 1 solutions",f"x={x}")
else :
     print("The equation has no solutions")