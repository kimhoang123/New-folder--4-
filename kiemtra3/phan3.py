import os
import random
def generate_map(row, cols):
    map = [["-"]*cols for i in range(rows)]
    map[0][0]="P"
    return map

def generate_object(map,rows,cols,obj_char):
    while True :
        r_K = random.randint(0,rows-1)
        c_K = random.randint(0,cols-1)
        if map[r_k][c_K] == "-":
            map[r_k][c_K]= obj_char
        break
def print_map(map,rows,cols):
    print()
    for r in range(rows):
        for c in range(cols):
            print(map[r][c],end="")
        print()
def move(map,rows,cols,ch,r_P,c_P):
    r_P_new = r_P
    c_P_new = c_P
    if ch == "W":
        r_P_new = max(0,r_P-1)
    elif ch == "S":
        r_P_new = min(rows-1,r_P+1)
    elif ch == "A":
        c_P_new = max(0,c_P-1)
    elif ch == "D":
        c_P_new = min(cols-1,c_P+1)
        
    value = map[r_P_new][c_P_new]
    map[r_P][c_P] = "-"
    map[r_P_new][c_P_new] = "P"
    return r_P_new,c_P_new,value
#------------------------
rows = 5 
cols = 10
map generate_map(rows, cols)
generate_object(map,rols,cols, 'K')
generate_object(map, rols,cols, 'D')

#----------------------
r_P = 0 
c_P = 0
found_key = False 
#------------------------
os.system('cls')
print_map(map,rows, cols)
