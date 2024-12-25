medical_cause=input("did u have a medical cause y on n?")
atten=int(input("enter the attendace of a student:"))
if medical_cause=='y':
    print("u are allowed")
else:
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")