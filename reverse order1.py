num=int(input("enter the no:"))
count=0 
while num!=0:
    num //=10
    count +=1
print("no of digits"+ str(count))