
n=input("Enter the number to check pallindrome")
ans=""
for i in range(0,len(n)):
    ans=n[i]+ ans    
if n == ans:
    print(n,"is a pallindrome")
else:
    print(n,"is not a pallindrome")
