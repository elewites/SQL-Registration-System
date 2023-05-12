from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


# functions

# inserts employee into database with given id, name, and phone number
def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        connection = mysql.connect(host="localhost",user="root", password="password", database="registration_system")
        cursor = connection.cursor()
        cursor.execute("insert into employees values ('"+id+"','"+name+"','"+phone+"')")
        cursor.execute("commit")

        e_id.delete(0, "end")
        e_name.delete(0, "end")
        e_phone.delete(0, "end")
        show()
        MessageBox.showinfo('Insert Status', "Inserted Success")
        connection.close()

# deletes employee from database based on given ID
def delete():
    if (e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is required for delete")
    else:
        connection = mysql.connect(host="localhost",user="root", password="password", database="registration_system")
        cursor = connection.cursor()
        cursor.execute("delete from employees where id='"+e_id.get()+"'")
        cursor.execute("commit")

        e_id.delete(0, "end")
        e_name.delete(0, "end")
        e_phone.delete(0, "end")
        show()
        MessageBox.showinfo('Delete Status', "Delete Successful")
        connection.close()


# updates employee details on database, given ID, updates name and phone number
def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id == "" or name == "" or phone == ""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        connection = mysql.connect(host="localhost", user="root", password="password", database="registration_system")
        cursor = connection.cursor()
        cursor.execute("update employees set name='"+name+"',phone='"+phone+"'where id='"+id+"'")
        cursor.execute("commit")

        e_id.delete(0, "end")
        e_name.delete(0, "end")
        e_phone.delete(0, "end")
        show()
        MessageBox.showinfo('Update Status', "Update Success")
        connection.close()


# gets employee from database given ID
def get():
    if (e_id.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID is required for delete")
    else:
        connection = mysql.connect(host="localhost",user="root", password="password", database="registration_system")
        cursor = connection.cursor()
        cursor.execute("select * from employees where id='"+e_id.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])

        connection.close()


# fetches all employees from database to display in interface
def show():
    connection = mysql.connect(host="localhost", user="root", password="password", database="registration_system")
    cursor = connection.cursor()
    cursor.execute("select * from employees")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0]) + "     " + row[1] + "     " + row[2]
        list.insert(list.size()+1, insertData)

        connection.close()

# GUI INTERFACE

# creating tkinter window
window = Tk()
window.geometry('800x600')
window.title("Registration System")

title = Label(window, text='Add/Delete/Update Employee Details to Database', font=('bold', 10))
title.place(x=200, y=2)

# id label
id = Label(window, text='Enter ID', font=('bold', 10))
id.place(x=20, y=30)

# name label
name = Label(window, text='Enter Name', font=('bold', 10))
name.place(x=20, y=60)

# phone label
phone = Label(window, text='Enter Phone', font=('bold', 10))
phone.place(x=20, y=90)

# id entry
e_id = Entry()
e_id.place(x=150, y=30)

# name entry
e_name = Entry()
e_name.place(x=150, y=60)

# phone entry
e_phone = Entry()
e_phone.place(x=150, y=90)

# insert button with instructions
insert = Button(window, text='Insert Employee', font=('italic', 10), bg="white", command=insert)
insert.place(x=20, y=130)
insert_instructions = Label(window, text='Input all fields to insert', font=('bold', 10))
insert_instructions.place(x=250, y=130)

# delete button with instructions
delete = Button(window, text='Delete Employee Based on ID', font=('italic', 10), bg="white", command=delete)
delete.place(x=20, y=170)
delete_instructions = Label(window, text='Input ID of employee to delete', font=('bold', 10))
delete_instructions.place(x=250, y=170)

# update button with instructions
update = Button(window, text='Update Employee Based on ID', font=('italic', 10), bg="white", command=update)
update.place(x=20, y=210)
delete_instructions = Label(window, text='Input current ID of employee, plus updated values (name, phone)', font=('bold', 10))
delete_instructions.place(x=250, y=210)

# get button with instructions
get = Button(window, text='Get Employee Details Based on ID', font=('italic', 10), bg="white", command=get)
get.place(x=20, y=250)
get_instructions = Label(window, text='Input ID of employee to fetch data', font=('bold', 10))
get_instructions.place(x=250, y=250)

# list object that displays employees added to database
list = Listbox(window, width=60)
list.place(x=50, y=300)
show()


window.mainloop()
