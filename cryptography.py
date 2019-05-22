#wap to accept two strings and print the longest common substring
#wap to accept a string from user and remove the first letter then add it at the end and add "ay" along that

"""def function1(s1,s2):
    a=len(s1)
    b=len(s2)
    if a > b:
        for x in s2:
            




s1=input("Enter the first string:")
s2=input("Enter the second string:")"""




x=input("Enter a string with space seperation")
list1=x.split(" ")
ans=""
for x in list1:
    ans=ans + x[1:]+x[0]+"ay"
print(ans)
