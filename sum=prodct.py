n=int(input("enter a number"))
product=1
add=0
while n>0:
    rem=n%10
    product=product*rem
    add= add+rem
    n=n//10
if add==product:
    print("yes the product is equal to the sum")
else:
    print("product and sum was not equal")

