height=float(input("enter ur height in cm:"))
weight=float(input("enter ur weight in kg:"))
BMI=weight/(height/100)**2
print("ur bmi is",BMI)
if BMI<=18.4:
    print("ur underweight")
elif BMI<=24.9:
    print("ur healthy")
elif BMI<=29.9:
    print("ur overweight")
elif BMI<=34.9:
    print("ur severely overweight")
elif BMI<=39.9:
    print("ur obese")
else:
    print("ur severely obese")
