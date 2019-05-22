import random
count=0
#-------------------------------------------------------------
def prime(n):
    x=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            x=1
    if x==0:
        return n
    if x!=0:
        return 0
#----------------------------------------------------------
while True:
    n=random.randint(1,1000)
    if n==prime(n):
        print(n)
        count=count+1
    if count==100:
        break;
