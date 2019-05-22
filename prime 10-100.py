def prime(variable):
    x=0
    for i in range(2,variable//2+1):
        if variable%i == 0:
            x=1
            break
    if x == 0:
        return 1
    else:
        return 0
ans=0
for i in range(10,100):
    if prime(i) == 1:
        ans= ans + i
    
print (ans)
