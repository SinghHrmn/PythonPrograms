import math
#--------------------------------------------------------------
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
#---------------------------------------------------------------
num=int(input("Enter the count of prime numbers"))
ans=0
count=0
variable=2
while True:
    print(count)
    if count == num:
        break
    if prime(variable)== 1:
        ans=ans + math.factorial(variable)
        count=count+1
    variable=variable+1       
print (ans)
    
    
    
    
