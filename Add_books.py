from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book')
        self.canvas = Canvas(width=500, height=500, bg='gray')
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        #verifying Input
        def b_q():
            if len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Pleas Enter Book ID")
            elif len(b.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Book Name")
            elif len(c.get()) <1:
                messagebox.showinfo("Oop's","Please Enter Book Author Name")
            elif len(d.get()) < 1:
                messagebox.showinfo("Oops","Please Enter Availability")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library_management_system',
                                         user='root',
                                         password='jerry')
                    self.myCursor = self.conn.cursor()
                    book_id = a.get()
                    book_name = b.get()
                    author = c.get()
                    availability = d.get()
                    self.myCursor.execute("Insert into book(book_id,book_name,author,availability) values "
                                          "(%s,%s,%s,%s)",[a.get(),b.get(),c.get(),d.get()])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")
        #creating input box and label

        Label(self, text='Book Details:',bg='gray',fg='white',font=('Agency FB', 30, 'bold')).place(x=155, y=30)

        Label(self, text='Book ID:', bg='gray', fg='black', font=('Calibri', 15)).place(x=60, y=100)
        Entry(self, textvariable=a, width=30).place(x=190, y=107)

        Label(self, text='Book Name:',bg='gray',fg='black', font=('Calibri', 15)).place(x=60, y=150)
        Entry(self, textvariable=b, width=30).place(x=190, y=155)

        Label(self, text='Book Author:',bg='gray',fg='black', font=('calibri', 15)).place(x=60, y=200)
        Entry(self, textvariable=c, width=30).place(x=190, y=203)

        Label(self, text='Availability:', bg='gray', fg='black', font=('calibri', 15)).place(x=60, y=250)
        Entry(self, textvariable=d, width=30).place(x=190, y=251)

        Button(self, text="Submit", command=b_q).place(x=320, y=300,width=100)

Add().mainloop()