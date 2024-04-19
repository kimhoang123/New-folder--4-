#1----
def factorial(n):
    giai_thua = 1
    if n == 0:
        return "0! = 1"
    else:
        for i in range(1, n + 1):
            giai_thua *= i
        return f"{n}! = {giai_thua}"

number = int(input("Nhập một số nguyên: "))
print(factorial(number))
#2----------
list = [5, 1, 8, 92, -1, 30]
def sap_xep_tang_dan(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
print("Original list:"," ".join(map(str,list)))
sap_xep_tang_dan(list)
print("Sorted list:"," ".join(map(str, list)))
#3-------------------
def print_fibo(n):
    fibo_list = [1, 1]
    for i in range(2, n):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    print("First", n, "Fibonacci numbers:", ' '.join(map(str, fibo_list)))




