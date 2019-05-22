#wap to accept a string from user and remove the first letter then add it at
#the end and add "ay" along that
x=input("Enter a string with space seperation")
list1=x.split(" ")
ans=""
for x in list1:
    ans=ans + x[1:]+x[0]+"ay"+" "
print(ans)
