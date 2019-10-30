
def fact(no):
    i=1
    res=0
    for i in range(1,no):
        if no%i==0:
            res=res + i
    print("Sum of factors",res)

print("enter the number")
no=int(input())
fact(no)

