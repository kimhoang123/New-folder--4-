#age
age = int(input("Your age :"))
if(age < 0):
    print("not born")
elif(age < 18):
    print('teen')
elif(age < 60):
    print('adult')
else:
    prinht('old')
#boolean
a = True 
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
#keobuabao
import random
list_str = ["keo", "bua", "bao"]

def randomSkill(list_skill):
    return random.choice(list_skill)

userInput = input("keo,bua or bao?")
machineInput = randomSkill(list_str)
def checkResult(user,machine):
   if (user == "keo"):
        if (machine == "bao"):
            print("thang")
        elif(machine == "bua"):
            print("thua")
        else:
            print("hoa")
    if (user == "bao"):
        if (machine == "bao"):
            print("hoa")
        elif(machine == "bua"):
            print("thang")
        else:
            print("thua")
        
print(machineInput)
checkResult(machine=machineInput,user=userInput)
        