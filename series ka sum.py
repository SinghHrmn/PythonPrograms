n=int(input("Enter the value of n"))
x=int(input("Enter the value of x"))
ans=0.0
for i in range(1,n+1,2):
    ans=ans + (x**i)/i
print("the sum of the given series is ",ans)
