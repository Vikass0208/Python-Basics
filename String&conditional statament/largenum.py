a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))

if(a>=b and a>=c):
    print("A is largest Number")
elif(b>=c):
    print("B is Largest Number")
else:
    print("C is largest Number")