num=[5, 1, 8, 92, -1, 30]
a=''.join(map(str , num))
print("Original list:",a)
def sort(arr):
    b=len(arr)
    for i in range(b):
        for j in range(0,b-j-1):
            if arr[j]>arr[j+1]:
                arr[j]arr[j+1]=arr[j+1]arr[j]
sort(num)
print("Sorted list:",a)


