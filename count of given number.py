# write a program that can count the number of digits and print the count. eg 3456 is having count = 4

#initialised a count variable that holds the number of digit counts 
count=0

# taking input from the user and type casting that to 'int' beacuse default input is String   
n=int(input("Enter the number"))

# While loop testing for greater than zero
# 'rem' contains remainder when n is divided by 10
# n now contains the quotient when divided by 10
# increment the count by one
while n>0:
    rem=n%10
    n=n//10
    count+=1

# after the total count is calculated print the count
print(count)
