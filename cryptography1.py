#wap to accept a string from user and remove the first letter then add it at
#the end and add "ay" along that


# Getting input from user
x=input("Enter a string with space seperation")

# spiliting the string on the basis of space into a list  
list1=x.split(" ")

#initializing a empty string
ans=""

#At each iteration through the list
#we add the declared variable 'ans' 
# Then, add the string starting from index 1 till end of index 
# Then, adding first element x[0]
# Then, adding 'ay '
for x in list1:
    ans=ans + x[1:]+x[0]+"ay "


print(ans)
