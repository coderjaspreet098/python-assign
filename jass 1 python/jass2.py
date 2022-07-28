from tkinter import*
from tkinter import messagebox
from mysql import connector

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

def register():
    conn=connector.connect(host='127.0.0.1',port='3306',user='root',password='#Jython@4567',database='demo')
    mycursor=conn.cursor()
    fname=a1.get()
    lname=b1.get()
    email=c1.get()
    contact=e1.get()
    mycursor.execute("insert into new_table values(%s,%s,%s,%s)",(fname,lname,email,contact))
    messagebox.showinfo("Registration","submitted")
    conn.commit()

d=Label(root,text="Registration form",font=("bold",16),bg='cadetblue').grid(row=0,column=0)
a=Label(root,text="First Name :",padx=10,pady=10, font=("bold",16),bg='cadetblue').grid(row=1,column=0)
b=Label(root,text="last Name :",padx=10,pady=10,font=("bold",16),bg='cadetblue').grid(row=2,column=0)
c=Label(root,text="Email Id :",padx=10,pady=10, font=("bold",16),bg='cadetblue').grid(row=3,column=0)
e=Label(root,text=" Contact Number : ",padx=10,pady=10, font=("bold",16),bg='cadetblue').grid(row=4,column=0)
btn=Button(root,text="Submit",command=register,width=15,fg='Yellow',bg='green',pady=10).grid(row=5,column=0)
a1=Entry(root)
a1.grid(row=1,column=1)
b1=Entry(root)
b1.grid(row=2,column=1)
c1=Entry(root)
c1.grid(row=3,column=1)
e1=Entry(root)
e1.grid(row=4,column=1)
root.mainloop()