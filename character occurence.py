string = input("please enter ur string=")
char=input("please enter ur character=")
i=0 
count=0 
while(i<len (string)):
    if (string[i] == char):
        count=count+1
    i=i+1
print("total no of time=",char,"has occured",count)