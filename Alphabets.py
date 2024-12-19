print(" enter a character:")
c=input()
if c>='0' and c<='9':
    print("\nits a number")
elif c>='a' and c<='z':
    print("\nits an alphabet")
elif c>='A' and c<='Z':
    print("\nits an alphabet")
else:
    print("\nits neither an alphabet nor a number")