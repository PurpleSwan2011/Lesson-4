num=int(input("enter no"))
t=num 
numLen=0 
while t>0:
    numLen=numLen+1
    t=int(t/10)
    if numLen>=4:
        numLen=int(numLen/2)
        chk=0
        while num>0:
            rem=num%10
        if chk==numLen:
            midOne=rem
        elif chk==(numLen-1):
            midTwo=rem
        num=int(num%10)
        chk=chk+1
        prod=midOne*midTwo
        print("\nproduct of mid no ("+str (midOne)+"*"+str(midTwo)+")=",prod)  
    else:
        print("\nits nota 4 or more than 4 no") 
        
            
    