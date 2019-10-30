
def pattern(row,col):
    i=1
    for i in range(row):
        j=i
        for j in range(col):
            print("* ",end=" ")
        print()

print("Enter the number no of rows");
row = int(input())
print("Enter the number no of columns");
col = int(input())
pattern(row,col)
