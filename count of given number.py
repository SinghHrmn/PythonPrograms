count=0
n=int(input("Enter the number"))
while n>0:
    rem=n%10
    n=n//10
    count+=1
print(count)
