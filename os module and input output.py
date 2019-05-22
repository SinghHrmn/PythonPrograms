#chetan sir's lecture on OS module
import os

os.getcwd()                     #get the current directory
os.chdir()                      #to change the direc
os.listdir()                    #list all the directories
#to make a directory
os.mkdir("PYTOHN")

#================================================================================
#how to read lines and get the length
f=open('''file location''')
lines=f.readlines()
cnt=len(lines)
print(cnt)


#if we change the dir then we dont need to specify the location just name is enough
#other topics which got coverd were file opening in read and write
