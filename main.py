from tkinter import *
from tkinter import messagebox
import os
import sys
py=sys.executable

def pc():
    self.destroy()
    os.system('%s %s' %(py, 'login.py'))

class main:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap('library.ico')

    

        title=Label(self.root,text="Library Management System",font=("calibri",40,"bold"),bg="grey")
        title.pack(side=TOP,fill=X)

        Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="grey")
        Frame1.place(x=280,y=150,width=700,height=400)

        button1=Button(self.root,text="Login",command=pc,font=("Agency FB",30,"bold"))
        button1.place(x=480,y=220,width=300,height=70)

        button2=Button(self.root,text="Register",font=("Agency FB",30,"bold"))
        button2.place(x=480,y=350,width=300,height=70)

        button3=Button(self.root,text="Exit",command=root.quit,font=("calibri",12))
        button3.place(x=820,y=480,width=100,height=40)

    
    



root=Tk()
obj=main(root)
root.mainloop()