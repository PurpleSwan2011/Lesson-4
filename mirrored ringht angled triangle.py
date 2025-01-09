r=int(input("enter:"))
print("mirrored right angled triangle star pattern")
for i in range (1,r+1):
    for j in range(1,r+1):
        if (j<=r-i):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()