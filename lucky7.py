import tkinter
import tkinter.messagebox
import random
#-------------------------------------------------------------------------------
def lucky():
    n1=random.randint(4,7)
    n2=random.randint(4,7)
    n3=random.randint(4,7)
    list1=[n1,n2,n3]
    
    if n1==7 and n2==7 and n3==7:
        p=str(list1)+"congratulations you have won jackpot"
        tkinter.messagebox.showinfo("",p)
    elif n1==n2 or n2==n3 or n1==n3:
        q=str(list1)+("congratulations you have won bonus")
        tkinter.messagebox.showinfo("",q)
        
    else:
        r=str(list1)+("you lost")
        tkinter.messagebox.showinfo("",r)
#-------------------------------------------------------------------------------
root=tkinter.Tk()
bt1=tkinter.Button(root,text="play",command=lucky)
lb1=tkinter.Label(root,text="Press play to run Lucky Seven")
lb1.pack()
bt1.pack()
root.mainloop()


       
#-------------------------------------------------------------------------------
    
