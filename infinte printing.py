import os
import sys
import csv

'''x = os.listdir("D:\\")
for i in x:
    print(i)
    sorc = os.path.isdir("D:\\"+i)
    if sorc == True:
        y = os.listdir("D:\\"+i)
        for k in y:
            print("    "+k)
'''
file = open("D:\\test.txt","r")
for x in file:
    name = file.readline()
    age = file.readline()
    course = file.readline()
    delimitor = file.readline()
    print("name ==> ",name,"\n","Age ==> ",age,"\n","Course ==> ",course)