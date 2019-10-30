
def pat(no):
    i=0
    for i in range(no-i):
        for i in range(1,no-i):
            print("*",end=" ")
        print(" ")

print("Enter the number of stars")
no=int(input())
pat(no)
