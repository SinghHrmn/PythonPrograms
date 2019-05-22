import tkinter
import tkinter.messagebox

class calc():
    def calculate():
        x1=Sub1.get()
        x2=Sub2.get()
        x3=Sub3.get()
        x4=Sub4.get()
        x5=Sub5.get()
        x6=Sub6.get()
        
    def __init__(self):
        form=tkinter.Tk()
        Sub1=tkinter.Entry(form)
        Sub2=tkinter.Entry(form)
        Sub3=tkinter.Entry(form)
        Sub4=tkinter.Entry(form)
        Sub5=tkinter.Entry(form)
        Sub6=tkinter.Entry(form)
        lb1=tkinter.Label(form,text="Enter the Numbers of subject\"***\"")
        lb2=tkinter.Label(form,text="Enter the Numbers of subject\"***\"")
        lb3=tkinter.Label(form,text="Enter the Numbers of subject\"***\"")
        lb4=tkinter.Label(form,text="Enter the Numbers of subject\"***\"")
        lb5=tkinter.Label(form,text="Enter the Numbers of subject\"***\"")
        lb6=tkinter.Label(form,text="Enter the Numbers of subject\"***\"")
        bt1=tkinter.Button(form,text="calculate",command=calculate)
        
        lb1.pack()
        Sub1.pack()
        lb2.pack()
        Sub2.pack()
        lb3.pack()
        Sub3.pack()
        lb4.pack()
        Sub4.pack()
        lb5.pack()
        Sub5.pack()
        lb6.pack()
        Sub6.pack()
def test():
    x=calc()
root=tkinter.Tk()
bt1=tkinter.Button(root,text="SEM 1",padx=13,pady=13,command=test)
bt2=tkinter.Button(root,text="SEM 2",padx=13,pady=13,command=test)
bt3=tkinter.Button(root,text="SEM 3",padx=13,pady=13,command=test)
bt4=tkinter.Button(root,text="SEM 4",padx=13,pady=13,command=test)
bt5=tkinter.Button(root,text="SEM 5",padx=13,pady=13,command=test)
bt6=tkinter.Button(root,text="SEM 6",padx=13,pady=13,command=test)
bt7=tkinter.Button(root,text="SEM 7",padx=13,pady=13,command=test)
bt8=tkinter.Button(root,text="SEM 8",padx=13,pady=13,command=test)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()
bt6.pack()
bt7.pack()
bt8.pack()



root.mainloop()
