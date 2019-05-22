#wap to accept two strings and print the longest common substring
s1=input("Enter the first string:")
s2=input("Enter the second string:")
lcsl=0
lcs=""
if len(s1)>= len(s2):
    for i in range(0,len(s2)):
        for j in range(i+1,len(s2)+1):
            temp=s2[i:j]
            if temp in s1:
                if len(temp)>lcsl:
                    lcsl=len(temp)
                    lcs=temp
print("Laergest commom string is ",lcs)
