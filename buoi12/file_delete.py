import os
import shutil

scr = "D:\\New folder (4)\\buoi12\\a\\a.pst"

try:
    os.remove(scr)
except FileNotFoundError:
    print("File not found!")
else:
    print("File is deleted")
#xoa folder
path_dir="D:\\New folder (4)\\buoi12\\a"
try:
    os.rmdir(path_dir)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You do not have permission")
except OsError:
    print("Can not delete by this function")
    shutil.rmtree(path_dir)#delete folder with files
    print("Deleted files and folder")
else:
    print("File is deleted")
