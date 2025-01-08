def binaryToDecimal(binary):
    decimal , i=0,0
    while (i!=0):
        dec=binary%10
        decimal=dec+decimal*pow(2,i)
        binary=binary//10
        i+=1
    print("decimal:",decimal)
binary=int(input("enter binary:"))
binaryToDecimal(binary)