ans=0.0
x=0
print("The given set of operators are +,-,*,/  for total leave the operator empty")
while True:
    if x == 1:
        num1=0
    if x == 0:
        num1=float(input("enter the number"))
        x+=1
    
    operator=input("enter the operator")
    if operator == "":
        break
    num2=float(input("enter the number"))
    if operator == "+":
        ans= ans + num1 +num2
    elif operator == "*":
        if x==1:
            num1=1
        ans=ans*num1*num2
    elif operator == "/":
        if x==1:
            num1=1
        ans=(ans/num1)/num2
    elif operator == "-":
        ans=ans+(num1-num2)
print("Total is ",ans)

    
