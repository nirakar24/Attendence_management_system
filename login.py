import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('green')

def add_student():
    global name,roll_no,depart,passwrd,conf,sign_window

    sign_window=ctk.CTkToplevel()
    sign_window.geometry("500x400")

    frame=ctk.CTkFrame(sign_window)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label=ctk.CTkLabel(frame,text="Add Student details  ",font=("Roboto", 24))
    label.pack(pady=12,padx=10)

    name=ctk.CTkEntry(frame,placeholder_text="Your name")
    name.pack(pady=12,padx=10)

    roll_no=ctk.CTkEntry(frame, placeholder_text="Roll no")
    roll_no.pack(pady=12,padx=10)

    depart=ctk.CTkEntry(frame, placeholder_text="Department")
    depart.pack(pady=12,padx=10)

    passwrd=ctk.CTkEntry(frame,placeholder_text="Password",show="*")
    passwrd.pack(pady=12,padx=10)

    conf=ctk.CTkEntry(frame,placeholder_text="Confirm Password")
    conf.pack(pady=12,padx=10)

    button=ctk.CTkButton(frame,text="Proceed",command=data_student)
    button.pack(pady=12,padx=10)
    root.withdraw()

def data_student():
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute("INSERT INTO Attendence VALUES (:name, :roll_no , :department, :password,:present,:absent)",
                    {
                        'name':name.get(),
                        'roll_no':roll_no.get(),
                        'department':depart.get(),
                        'password':passwrd.get(),
                        'present':0,
                        'absent':0
                    }
                    )

    db.commit()

    db.close()

    messagebox.showinfo("Authentication","Student have been successfully added\nChanges will appear after restart")
    sign_window.destroy() 

def data_modify():
    key=mroll_no.get()
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"""UPDATE Attendence SET name='{mstudent_name.get()}',
                        roll_no={mroll_no.get()},
                        department='{mdepart.get()}' WHERE roll_no = {key} """
                    )

    db.commit()

    db.close()

    messagebox.showinfo("Info","Student details have been modified\nChanges will be applied after restart")
    modify_window.destroy()

def delete_user():
    key=mroll_no.get()
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"DELETE from Attendence WHERE roll_no={key}")

    db.commit()

    db.close()
    messagebox.showinfo("Info","Student details has been deleted succesfully\nChanges will be applied after restart")
    modify_window.destroy()

def modify():
    # global name,roll_no,depart,passwrd,conf,sign_window,name_usr
    messagebox.showinfo("Info","Roll no can't be changed as they are the key elements but can be assigned to different Student")
    global name_usr,mstudent_name,mroll_no,mdepart,modify_window

    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"SELECT * FROM Attendence WHERE name='{name_usr.get()}'")

    student = cur_sor.fetchall()
    details=student[0]

    modify_window=ctk.CTkToplevel()
    modify_window.geometry("500x400")

    mframe=ctk.CTkFrame(modify_window)
    mframe.pack(pady=20,padx=60,fill="both",expand=True)

    label=ctk.CTkLabel(mframe,text="Modify Student Details",font=("Roboto", 24))
    label.pack(pady=12,padx=10)
    name_var=StringVar()
    mstudent_name=ctk.CTkEntry(mframe,placeholder_text="Your name",textvariable=name_var)
    name_var.set(name_usr.get())
    mstudent_name.pack(pady=12,padx=10)

    roll_var=IntVar()
    mroll_no=ctk.CTkEntry(mframe, placeholder_text="Roll no",textvariable=roll_var,state="disabled")
    roll_var.set(details[1])
    mroll_no.pack(pady=12,padx=10)

    depart_var=StringVar()
    mdepart=ctk.CTkEntry(mframe, placeholder_text="Department",textvariable=depart_var)
    depart_var.set(details[2])
    mdepart.pack(pady=12,padx=10)

    mbutton=ctk.CTkButton(mframe,text="Modify",command=data_modify)
    mbutton.pack(pady=12,padx=10)

    mbutton2=ctk.CTkButton(mframe,text="Delete User",command=delete_user,hover_color="red")
    mbutton2.pack(pady=12,padx=10)
    root.withdraw()

    modify_window.mainloop()

def detail():

    def disable_event():
        pass
    def present():
        db=sqlite3.connect("students.db")

        cur_sor = db.cursor()
        cur_sor.execute(f"UPDATE Attendence SET present=present+1 WHERE name='{name_usr.get()}'")
        db.commit()

        db.close()   
        messagebox.showinfo("Info","Your attendence have been recorded\nChanges will be applied after restart")

    def absent():
        db=sqlite3.connect("students.db")

        cur_sor = db.cursor()
        cur_sor.execute(f"UPDATE Attendence SET absent=absent+1 WHERE name='{name_usr.get()}'")
        db.commit()

        db.close()   
        messagebox.showinfo("Info","You have missed a class\nChanges will be applied after restart")
        
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"SELECT * FROM Attendence WHERE name='{name_usr.get()}'")

    student = cur_sor.fetchall()
    details=student[0]

    key=""
    
    for i in student:
        print(i)
        key=i[3]

        print(key)
        db.commit()

        db.close()
        window2=ctk.CTkToplevel()
        window2.geometry("400x600+0+0")
        window2.title("User Profile")
        # usr=user.get()
        frame=ctk.CTkFrame(window2)
        frame.pack(pady=20,padx=60,fill="both",expand=True)
        label=ctk.CTkLabel(frame,text="Profile",font=("Roboto", 24))
        label.pack(pady=12,padx=10)
        label2=ctk.CTkLabel(frame,text=f"Name : {details[0]} ")
        label2.pack(pady=12,padx=10)
        label3=ctk.CTkLabel(frame,text=f"Roll no : {details[1]} ")
        label3.pack(pady=12,padx=10)
        label4=ctk.CTkLabel(frame,text=f"Department : {details[2]} ")
        label4.pack(pady=12,padx=10)
        label5=ctk.CTkLabel(frame,text=f"Classes Attended : {details[4]} ")
        label5.pack(pady=12,padx=10)
        label6=ctk.CTkLabel(frame,text=f"Not attended : {details[5]} ")
        label6.pack(pady=12,padx=10)
        total=details[4]+details[5]
        try:
            label7=ctk.CTkLabel(frame,text=f"Overall Percentage : {round(((details[4]/(total))*100),2)} %")
            label7.pack(pady=12,padx=10)

            slider_1 = ctk.CTkSlider(master=frame, from_=0, to=100,state='disabled')
            slider_1.pack(pady=12, padx=10)
            slider_1.set(round(((details[4]/(total))*100),2))

        except(ZeroDivisionError):
            label7=ctk.CTkLabel(frame,text=f"Overall Percentage : 0 %")
            label7.pack(pady=12,padx=10)

            slider_1 = ctk.CTkSlider(master=frame, from_=0, to=100,state='disabled')
            slider_1.pack(pady=12, padx=10)
            slider_1.set(0)

        button2=ctk.CTkButton(frame,text="Present",command=present)
        button2.pack(pady=12,padx=10)
        button3=ctk.CTkButton(frame,text="Absent",command=absent)
        button3.pack(pady=12,padx=10)
        button1=ctk.CTkButton(frame,text="close",command=close,hover_color='red')
        button1.pack(pady=12,padx=10)
        root.withdraw()

        window2.protocol("WM_DELETE_WINDOW", disable_event)
        window2.mainloop()

        window2.mainloop()
    

def close():
    root.destroy()

def data():
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute("INSERT INTO Attendence VALUES (:name, :roll_no , :department, :password,:present,:absent)",
                    {
                        'name':name.get(),
                        'roll_no':roll_no.get(),
                        'department':depart.get(),
                        'password':passwrd.get(),
                        'present':0,
                        'absent':0
                    }
                    )

    db.commit()

    db.close()

    messagebox.showinfo("Authentication","You have successfully Signed up")
    root.deiconify()

    sign_window.destroy() 

def sign_up():
    global name,roll_no,depart,passwrd,conf,sign_window

    sign_window=ctk.CTkToplevel()
    sign_window.geometry("500x400")

    frame=ctk.CTkFrame(sign_window)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label=ctk.CTkLabel(frame,text="Sign Up",font=("Roboto", 24))
    label.pack(pady=12,padx=10)

    name=ctk.CTkEntry(frame,placeholder_text="Your name")
    name.pack(pady=12,padx=10)

    roll_no=ctk.CTkEntry(frame, placeholder_text="Roll no")
    roll_no.pack(pady=12,padx=10)

    depart=ctk.CTkEntry(frame, placeholder_text="Department")
    depart.pack(pady=12,padx=10)

    passwrd=ctk.CTkEntry(frame,placeholder_text="Password",show="*")
    passwrd.pack(pady=12,padx=10)

    conf=ctk.CTkEntry(frame,placeholder_text="Confirm Password")
    conf.pack(pady=12,padx=10)

    button=ctk.CTkButton(frame,text="Proceed",command=data)
    button.pack(pady=12,padx=10)
    root.withdraw()

def all():
    def disable_event():
        pass
    global name_usr
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"SELECT * from Attendence")
    students=cur_sor.fetchall()

    for name in students:
        print(name[0])
    db.commit()

    db.close()   

    window=ctk.CTkToplevel()
    window.geometry("500x550+0+0")
    window.title("All Students")
    root.withdraw()
        # usr=user.get()
    frame=ctk.CTkFrame(window)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label=ctk.CTkLabel(frame,text="List of all students",font=("Roboto", 24))
    label.pack(pady=12,padx=10)

    for i in students:
        if i[0]!='admin':
            print(i[0])
            button=ctk.CTkButton(frame,text=f"{i[0]}")
            button.pack(pady=12,padx=10)
        else:
            continue


    button0=ctk.CTkButton(frame,text="Add Students",command=add_student,hover_color="#059DC0")
    button0.pack(pady=12,padx=10)
        
    button1=ctk.CTkButton(frame,text="close",command=close,hover_color="red")
    button1.pack(pady=12,padx=10,side='bottom')

    button2=ctk.CTkButton(frame,text="Show details",command=detail)
    button2.pack(pady=12,padx=10,side='bottom')

    button=ctk.CTkButton(frame,text="Modify",command=modify)
    button.pack(pady=12,padx=10,side="bottom")

    name_usr=ctk.CTkEntry(frame,placeholder_text="Student name")
    name_usr.pack(pady=12,padx=10,side='bottom')


    root.withdraw()

    window.protocol("WM_DELETE_WINDOW", disable_event)

    window.mainloop

def login():
    def disable_event():
        pass
    # global frame
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"SELECT * FROM Attendence WHERE name='{user.get()}'")

    student = cur_sor.fetchall()
    details=student[0]

    key=""
    
    for i in student:
        print(i)
        key=i[3]

    print(details[0])
    print(key)
    db.commit()

    db.close() 

    given_key=passwd.get()

    if given_key=='0000' and details[0]=="admin":
        all()

    elif given_key==key:
        window=ctk.CTkToplevel()
        window.geometry("400x600+0+0")
        window.title("User Profile")
        # usr=user.get()
        frame=ctk.CTkFrame(window)
        frame.pack(pady=20,padx=60,fill="both",expand=True)
        label=ctk.CTkLabel(frame,text="Profile",font=("Roboto", 24))
        label.pack(pady=12,padx=10)
        label2=ctk.CTkLabel(frame,text=f"Name : {details[0]} ")
        label2.pack(pady=12,padx=10)
        label3=ctk.CTkLabel(frame,text=f"Roll no : {details[1]} ")
        label3.pack(pady=12,padx=10)
        label4=ctk.CTkLabel(frame,text=f"Department : {details[2]} ")
        label4.pack(pady=12,padx=10)
        label5=ctk.CTkLabel(frame,text=f"Classes Attended : {details[4]} ")
        label5.pack(pady=12,padx=10)
        label6=ctk.CTkLabel(frame,text=f"Not attended : {details[5]} ")
        label6.pack(pady=12,padx=10)
        total=details[4]+details[5]
        try:
            label7=ctk.CTkLabel(frame,text=f"Overall Percentage : {round(((details[4]/(total))*100),2)} %")
            label7.pack(pady=12,padx=10)

            slider_1 = ctk.CTkSlider(master=frame, from_=0, to=100,state='disabled')
            slider_1.pack(pady=12, padx=10)
            slider_1.set(round(((details[4]/(total))*100),2))

        except(ZeroDivisionError):
            label7=ctk.CTkLabel(frame,text=f"Overall Percentage : 0 %")
            label7.pack(pady=12,padx=10)

            slider_1 = ctk.CTkSlider(master=frame, from_=0, to=100,state='disabled')
            slider_1.pack(pady=12, padx=10)
            slider_1.set(0)

        button1=ctk.CTkButton(frame,text="close",command=close,hover_color="red")
        button1.pack(pady=12,padx=10)
        root.withdraw()

        window.protocol("WM_DELETE_WINDOW", disable_event)
        window.mainloop()

        window.mainloop()

    else:
        root.destroy()

root=ctk.CTk()
root.geometry("500x350")
root.title("Authentication")

frame=ctk.CTkFrame(root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=ctk.CTkLabel(frame,text="Login",font=("Roboto", 24))
label.pack(pady=12,padx=10)

user=ctk.CTkEntry(frame,placeholder_text="Student name")
user.pack(pady=12,padx=10)

passwd=ctk.CTkEntry(frame,placeholder_text="Password",show="*")
passwd.pack(pady=12,padx=10)

button=ctk.CTkButton(frame,command=login,text="Login")
button.pack(pady=12,padx=10)
button2=ctk.CTkButton(frame,command=sign_up,text="Sign up")
button2.pack(pady=12,padx=10)
root.mainloop()