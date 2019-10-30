def sumdigit(no):
    i = 0
    res = 0
    while (i < no):

        rem = no % 10
        res=res+rem
        no=no//10
    i=i+1

    print("Sum of digit", res)


print("Enter multi-digit number ");
no = int(input())
sumdigit(no)