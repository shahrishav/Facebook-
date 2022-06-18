from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.title("Facebook")
root.config(bg='blue')
conn=sqlite3.connect('user.db')# connecting to d Databses
c=conn.cursor() #helps to execute the query and fetch the records from the database
# Create table
# c.execute("""CREATE TABLE user(
#     first_name text,
#     last_name text,
#     address text,
#     age integer,
#     password text,
#     father_name text,
#     city text,
#     zipcode text
#     )""")
# print("Table created")

def submit(): #submit function 
    conn=sqlite3.connect('user.db')  #connecting to database
    c=conn.cursor()#helps to execute the query and fetch the records from the database
    c.execute("INSERT INTO user VALUES(:f_name,:l_name,:address,:age,:password,:father_name,:city,:zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'age':age.get(),
        'password':password.get(),
        'father_name':father_name.get(),
        'city':city.get(),
        'zipcode':zipcode.get()
    })
    messagebox.showinfo("Success","Record has been added")
    conn.commit() #commit our command
    conn.close() #close our connection

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    father_name.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

def query(): #for query function 
    conn=sqlite3.connect('user.db')
    c=conn.cursor() #helps to execute the query and fetch the records from the database
    c.execute("SELECT *,oid FROM user")
    records=c.fetchall() #to returns a list of tuples.
    print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0])+":-"+record[0]+" "+str(record[1])+","+"\t"+str(record[4])+"\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=8,column=0,columnspan=2)

def delete():
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    c.execute("DELETE FROM user WHERE oid="+ delete_box.get())
    print("Deleted")
    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("""Update user SET
    first_name=:first,
    last_name=:last,
    address=:address,
    age=:age,
    password=:password
    father_name=:father_name
    city=:city,
    zipcode=:zipcode
    WHERE oid=:oid""",
    {
        'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'address':address_editor.get(),
        'age':age_editor.get(),
        'password':password_editor.get(),
        'father_name':father_name_editor.get(),
        'city':city_editor.get(),
        'zipcode':zipcode_editor.get(),
        'oid':record_id
    })

    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    editor=Toplevel()
    editor.title("Editor")
    editor.geometry("300x200")
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE oid="+record_id)
    records=c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zipcode_editor


    # Create text boxes
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1,padx=20)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=3,column=1,padx=20)

    password_editor=Entry(editor,width=30)
    password.grid(row=4,column=1,padx=20)

    father_name_editor=Entry(editor,width=30)
    father_name_editor.grid(row=5,column=1,padx=20)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=4,column=1,padx=20)

    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1,padx=20)
    # Create textbox labels 
    f_name_editor_label=Label(editor,text="First Name")
    f_name_editor_label.grid(row=0,column=0,pady=(10,0))

    l_name_editor_label=Label(editor,text="Last Name")
    l_name_editor_label.grid(row=1,column=0)

    address_editor_label=Label(editor,text="Address")
    address_editor_label.grid(row=2,column=0)

    age_editor_label=Label(editor,text="Age")
    age_editor_label.grid(row=3,column=0)

    password_editor_label=Label(editor,text="Password")
    password_editor_label.grid(row=4,column=0)

    father_name_editor_label=Label(editor,text="Father Name")
    father_name_editor_label.grid(row=5,column=0)

    city_editor_label=Label(editor,text="City")
    city_editor_label.grid(row=6,column=0)

    zipcode_editor_label=Label(editor,text="zipcode")
    zipcode_editor_label.grid(row=7,column=0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        father_name_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zipcode_editor.insert(0,record[7])
    edit_btn=Button(editor,text="Update",command=update)
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
# Create text boxes
f_name=Entry(root,width=30,bg='white')
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

age=Entry(root,width=30)
age.grid(row=3,column=1)

password=Entry(root,width=30,show="*")
password.grid(row=4,column=1)

father_name=Entry(root,width=30)
father_name.grid(row=5,column=1)

city=Entry(root,width=30)
city.grid(row=6,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=7,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

# Create textbox labels
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,padx=20)
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)
age_label=Label(root,text="Age")
age_label.grid(row=3,column=0)
password_label=Label(root,text="Password")
password_label.grid(row=4,column=0)
father_name_label=Label(root,text="Father Name")
father_name_label.grid(row=5,column=0)
city_label=Label(root,text="City")
city_label.grid(row=6,column=0)
zipcode_label=Label(root,text="zipcode")
zipcode_label.grid(row=7,column=0)
delete_box_label=Label(root,text="Select ID to delete / update")
delete_box_label.grid(row=9,column=0,pady=5)

# Create submit button    
submit_btn=Button(root,text="Submit",command=submit)
submit_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# Create query button
query_btn=Button(root,text="Query",command=query)
query_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# Create delete button
delete_box_btn=Button(root,text="Delete",command=delete)
delete_box_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

# Create update button
edit_box_btn=Button(root,text="Update",command=edit)
edit_box_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=120)
# commit change
conn.commit()

# close connection
conn.close()

mainloop()