from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:

                self.conn = mysql.connector.connect(host='localhost',
                                         database='library_management_system',
                                         user='root',
                                         password='jerry')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",
                                      [u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'register.py'))
                else:
                    self.destroy()
                    os.system('%s %s'%(py, 'login.py'))
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
#label and input
        Label(self, text='User Details', bg='gray', fg='black', font=('Agency FB', 30, 'bold')).\
            place(x=165, y=15)
        Label(self, text='Username:', bg='gray', font=('Calibri', 15)).place(x=70, y=80)
        Entry(self, textvariable=u, width=30).place(x=200, y=87)
        Label(self, text='Name:', bg='gray', font=('Calibri', 15)).place(x=70, y=120)
        Entry(self, textvariable=n, width=30).place(x=200, y=127)
        Label(self, text='Password:', bg='gray', font=('Calibri', 15)).place(x=70, y=160)
        Entry(self, textvariable=p, width=30).place(x=200, y=167)
        Button(self, text="Submit", width=15, command=insert).place(x=268, y=220)
reg().mainloop()