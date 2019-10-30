
def numpat(no):
    i=j=1
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")


print("Enter the number for increasing pattern")
no=int(input())

numpat(no)

