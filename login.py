from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
py=sys.executable


#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")




#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library_management_system',
                                         user='root',
                                         password='jerry')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'main.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

        def check():
            self.Frame1 = Frame(self, bd=4, relief=RIDGE, bg="grey")
            self.Frame1.place(x=280, y=150, width=600, height=350)

            self.label = Label(self, text="LOGIN", bg = 'gray' , fg = 'black', font=("Agency FB", 30,'bold'))
            self.label.place(x=550, y=170)

            self.label1 = Label(self, text="User ID" , bg = 'gray' , fg = 'black', font=("calibri", 18, 'bold'))
            self.label1.place(x=370, y=250)

            self.user_text = Entry(self, textvariable=self.a, width=45)
            self.user_text.place(x=495, y=255)

            self.label2 = Label(self, text="Password" , bg = 'gray' , fg = 'black', font=("calibri", 18, 'bold'))
            self.label2.place(x=340, y=320)

            self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
            self.pass_text.place(x=495, y=325)

            self.butt = Button(self, text="Login",bg ='white', font=10, width=8, command=chex)
            self.butt.place(x=670, y=400)

            self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='gray', fg='black',
                                font=("calibri", 30, 'bold'))
            self.label3.place(x=315, y=40)


        check()

Lib().mainloop()