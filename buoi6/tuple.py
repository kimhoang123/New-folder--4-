student = ("kim",15,"female","kim")
print(student)

# dem so lan phan tu xuat hien trong danh sach
print(student.count("kim"))
#ktra phan tu o vtri thu may
print(student.index("female"))

for i,val in student enumerate(student, start = 1) : # vua lay index + value
    print(f"{i}, {val}")

if "kim" in student : # phan tu "kim" co trong student ko
    print("True")

# slicing-----------------------
numbers= (22,3,4,5,8,15,22,34)
numbers[1:3]
numbers[:2]
numbers[2:]# lay tu vtri 2 den cuoi
numbers[:]# lay tu dau den cuoi
numbers[::2]# 2 don vi lay 1 lan
numbers[-4:-2]
numbers[::-1]#dao nguoc dsach
numbers[-4]# => 8