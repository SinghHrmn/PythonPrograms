num=int(input("enter the number"))
temp=0
count=0
while num>0:
    rem=num%10
    num=num//10
    if rem >= temp:
        temp=rem
    count=count+1
for i in range (0,count):
    ans=temp*10 + temp
    temp=temp*10


    

print(temp)
    
    

