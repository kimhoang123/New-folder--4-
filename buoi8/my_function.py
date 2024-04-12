def my_sum(a,b):
    print("sum", a+b)

def my_sum1(a,b):
    if a.isdigit():
        return "error"
    return a+b
# call func
my_sum(15,3)
print(my_sum1("15","3"))