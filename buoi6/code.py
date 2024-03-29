# def dubble_sort(arr):
#     a = len(arr)
#     for i in range(a):
#         for j in range(0,a-i-1) :
#             if arr[j] > arr[j+1] :
#                 arr[j],arr[j+1] =
# arr[j+1],arr[j]

# numbers= (22,3,4,5,8,15,22,34)
# dubble_sort(numbers)
# print(numbers)

# sắp xếp danh sách theo thứ tự tăng dần mà không dùng hàm sort/ sorted

l1=[76, 23, 45, 12, 54, 9, 54, 76, 76]  
# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
print("Sorted List", l1)
keep
Đã ghim
# Không cho danh sách trùng dữ liệu
for item in l1:
    if(l1.count(item) > 1):
        l1.remove(item)

print("No duplicate item", l1)


