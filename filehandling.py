"""file=open("D:\\test.txt","a")
name=input("Enter Your Name:")
age=input("Enter Your Age:")
course=input("Enter Your Course:")
file.write(name)
file.write("\n")
file.write(age)
file.write("\n")
file.write(course)
file.write("\n")
file.write("**************\n")
file.close()"""
file = open("D:\\test.txt","r")
for x in file:
    w=file.readlines()
    print(w)

    

