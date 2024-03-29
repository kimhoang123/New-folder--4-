from random import
score = 0
result = true 
while(result):
    # tao bieu thuc ( a,b,phep toan,kqua dung sai)
    a = ranint(0,10) # random ra 1 so tu 0-10
    b = ranint(1,10) # so b ko dc nho hon 0
    operator = choice (["*","/","+","-"])#random cac dau trong ngoac
    ans_false = ranint(-50,50)
#ktra phep toan => tinh kqua dung
    if (operator == "*"):
        ans_true = a*b
    else if (operator == "/"):
        ans_true = a/b
    else if (operator == "+"):
        ans_true = a+b
    else:
        ans_true = a-b
#in ra man hinh
print(str(a) + operator + str(b) + "=" + (choice[ans_false,ans_true]))
user_ans = int(input(" 0 is True , 1 False :"))
# xet kqua cua ng dung
if(user_ans == 0):
    if(ans == ans_true):
        score+=1
        print(F"Score:{score}")
        continue
    else:
        print("Game over")
        result=False
        break

if(user_ans == 1):
    if(ans == ans_false):
        score+=1
        print(F"Score:{score}")
        continue
    else:
        print("Game over")
        result=False
        break
