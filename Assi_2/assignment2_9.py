
def cntdigit(no):
    i=cnt=0
    while(i<no):
        rem=no%10
        cnt=cnt+1
        no=no//10
    i=i+1
    print("There is no of digit",cnt)


print("Enter multi-digit number ");
no = int(input())
cntdigit(no)


