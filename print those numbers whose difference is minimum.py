x=[2,4,6,7,1]
length=len(x)
ans=100000000000000
show=""
for i in range(0,length):
    a=i
    while a+1 < length:
        sub=x[i]-x[a+1]
        
        if sub < ans:
            ans = sub
            show=str(x[i])+","+str(x[a+1])
        a+=1
            
            
print("minimum difference bw numbers",show,"is",ans)

    
    
    
    
