def repeat(a,b):
    ans=""
    for i in range(1,b+1):
        ans=ans+a+""
    print(ans)



a=input("Enter the String to be repeated:")
b=int(input("Enter the number of times the string to be repeated"))
repeat(a,b)
