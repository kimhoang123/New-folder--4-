file_path='D:\\New folder (4)\\lap12\\a.txt'

with open(file_path,"r")as file :
    list_name = [("-"+ item.replace("\n","")) for item in file.readlines()]
    print("List of name:")
    for i in list_name:
        print(i)
