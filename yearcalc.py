a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b and a>c:
    if b>c:
        print (a,">",b,">",c)
    else:
        print(a,">",c,">",b)
if b>a and b>c:
    if a>c:
        print (b,">",a,">",c)
    else:
        print(b,">",c,">",a)
    
if c>a and c>b:
    if a>b:
        print (c,">",a,">",b)
    else:
        print(c,">",b,">",a)
