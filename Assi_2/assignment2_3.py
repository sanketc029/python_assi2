
def fact(no):
    i=1
    res=1
    while(i<=no):
        res=i*res
        i = i + 1

    print(res)

print("Enter the number");
no = int(input())
fact(no)
