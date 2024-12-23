print("enetr marks obtained in subs:")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())
tot=markone+marktwo+markthree+markfour+markfive
avg=tot/5
if avg>=91 and avg>=100:
    print("ur grade is A1")
if avg>=81 and avg>=91:
    print("ur grade is A2")
if avg>=71 and avg>=81:
    print("ur grade is b1")
if avg>=61 and avg>=71:
    print("ur grade is b2")
if avg>=51 and avg>=61:
    print("ur grade is c1")
if avg>=41 and avg>=51:
    print("ur grade is c2")
if avg>=33 and avg>=41:
    print("ur grade is d")
if avg>=21 and avg>=33:
    print("ur grade is e1")
if avg>=0 and avg>=21:
    print("ur grade is e2")
else:
    print("invalid input!!")