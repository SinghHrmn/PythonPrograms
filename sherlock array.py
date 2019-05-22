a=input("Enter the array in comma seperated form")
a=a.split(",")
a = list(map(lambda x:int(x),a))
a.sort()
flag = 0
for i in range(0,len(a)):
    if sum(a[:i])==sum(a[i+1:]):
        flag=1
if flag==1:
    print("YES")
else:
    print("NO")

    
