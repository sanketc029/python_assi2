
def prime(no):

    cnt=1
    for i in range(2,no):
        if no%i==0:
           cnt=0
           break
    if cnt == 1:
        print("Number is prime")
    else:
        print("Number is not prime")




print("Enter the number")
no=int(input())
prime(no)


